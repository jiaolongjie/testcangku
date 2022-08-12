import allure
from jsonpath_rw import parse

from data.apiUrl import HOST_URL
from data.variable import var
from util.log import logger
from util.requestUtil import RequestUtil
from util.yamlUtil import YamlUtil


class ChangJingRequestUtil:
    def __init__(self, yamlFileName, requestUtil):
        self.yamlUtil = YamlUtil('../config/changjing/' + yamlFileName + '.yml')
        self.requestUtil = requestUtil

    def yamlAndRequest(self):

        for dict in self.yamlUtil.getYamlData():  # 一个dict表示一条请求
            with allure.step('发送请求:' + dict['name']):

                logger.info('发送请求:' + dict['name'])
                # 拼接url路径
                dict['url'] = HOST_URL + dict['url']

                # 判断依赖depend
                depend = dict['depend']
                if depend != None:
                    # 判断请求头依赖
                    headers = depend['headers']
                    if headers != None:
                        for key,value in headers.items():
                            if dict['headers'] == None:
                                dict['headers'] = {}
                            # 把依赖添加到请求头
                            dict['headers'][key] = var.get(value)

                    # 判断params依赖
                    params = depend['params']
                    if params != None:
                        for key,value in params.items():
                            if dict['params'] == None:
                                dict['params'] = {}
                            # 把参数添加到params上
                            dict['params'][key] = var.get(value)

                    # 判断data依赖
                    data = depend['data']
                    if data != None:
                        for key,value in data.items():
                            if dict['data'] == None:
                                dict['data'] = {}
                            dict['data'][key] = var.get(value)

                    # 判断json依赖
                    json = depend['json']
                    if json != None:
                        for key,value in json.items():
                            if dict['json'] == None:
                                dict['json'] = {}
                            # 添加到json请求数据
                            dict['json'][key] = var.get(value)

                # 发送请求
                result = self.requestUtil.doRequest(method=dict['method'], url=dict['url'], params=dict['params'],data=dict['data'], json=dict['json'], headers=dict['headers'])
                # 断言
                self.requestUtil.assertResult(result, dict['validate']['statusCode'], dict['validate']['errorCode'],dict['validate']['msg'])

                # 判断是否导出数据extract
                extract = dict['extract']
                if extract != None:
                    # 判断是否导出body内容
                    body = extract['body']
                    if body != None:
                        for key,value in body.items():
                            # 存储键值对 result.json()
                            var.set(key,self.getDeptParmas(result.json(),value))
                    # 判断是否导出响应头
                    headers = extract['headers']
                    if headers != None:
                        for key,value in headers.items():
                            var.set(key,self.getDeptParmas(result.headers,value))

    # 提取数据函数 dict给一个字典数据 regex提取规则data.code
    def getDeptParmas(self, dict, regex):
        json_exe = parse(regex)
        result = json_exe.find(dict)
        params = [match.value for match in result][0]
        logger.info('源数据:' + str(dict) + ',提取规则:' + str(regex) + ',提取结果:' + str(params))
        return params



if __name__ == '__main__':
    ru = RequestUtil()
    cjru = ChangJingRequestUtil('changjing_01', ru)
    cjru.yamlAndRequest()
