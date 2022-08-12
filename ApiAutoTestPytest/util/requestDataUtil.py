from data.apiUrl import HOST_URL
from util.csvUtil import CsvUtil
from util.log import logger
from util.yamlUtil import YamlUtil


class RequestDataUtil:
    def __init__(self, fileName):
        self.yamlFile = '../config/' + fileName + '.yml'
        self.csvFile = '../data/' + fileName + '.csv'

    def getRequestData(self):
        # 1.获取yaml工具对象
        yu = YamlUtil(self.yamlFile)
        # 2.获取csv工具对象
        cu = CsvUtil(self.csvFile)

        requestDataList = []

        # 遍历csv列表数据 dict表示一行数据
        for dict in cu.getCsvData():
            yamlDict = yu.getYamlData()  # 一条请求数据
            # 1.url拼接
            yamlDict['url'] = HOST_URL + yamlDict['url']
            # 2.判断headers
            headers = yamlDict['headers']
            if headers != None:
                for key in headers.keys():
                    headers[key] = dict[key]
            # 3.判断params
            params = yamlDict['params']
            if params != None:
                for key in params.keys():
                    params[key] = dict[key]
            # 4.判断data
            data = yamlDict['data']
            if data != None:
                for key in data.keys():
                    data[key] = dict[key]
            # 5.判断json
            json = yamlDict['json']
            if json != None:
                for key in json.keys():
                    json[key] = dict[key]
            # 6.判断validate
            validate = yamlDict['validate']
            if validate != None:
                for key in validate.keys():
                    validate[key] = dict[key]

            # 添加到列表
            requestDataList.append(yamlDict)

        logger.info('组装请求数据:'+str(requestDataList))
        return requestDataList


if __name__ == '__main__':
    rdu = RequestDataUtil('erJi')
    rdu.getRequestData()
