import allure
import requests

from util.log import logger


class RequestUtil:
    def __doGet(self, url, params=None, **kwargs):
        result = requests.get(url=url, params=params, **kwargs)

        logger.info('请求路径:' + str(result.request.url))
        logger.info('请求方式:' + str(result.request.method))
        logger.info('请求头:' + str(result.request.headers))
        logger.info('请求体:' + str(result.request.body))
        logger.info('响应状态码:' + str(result.status_code))
        logger.info('响应头:' + str(result.headers))
        logger.info('响应文本内容:' + str(result.text))

        return result

    def __doPost(self, url, data=None, json=None, **kwargs):
        result = requests.post(url=url, data=data, json=json, **kwargs)

        logger.info('请求路径:' + str(result.request.url))
        logger.info('请求方式:' + str(result.request.method))
        logger.info('请求头:' + str(result.request.headers))
        logger.info('请求体:' + str(result.request.body))
        logger.info('响应状态码:' + str(result.status_code))
        logger.info('响应头:' + str(result.headers))
        logger.info('响应文本内容:' + str(result.text))

        return result

    def doRequest(self, method, url, params=None, data=None, json=None, **kwargs):
        if method == 'GET':
            return self.__doGet(url=url, params=params, **kwargs)
        elif method == 'POST':
            return self.__doPost(url=url, data=data, json=json, **kwargs)
        else:
            logger.info('暂时不支持的请求方式')

    # 断言判断函数
    def assertResult(self, result, statusCode, errorCode, msg):
        with allure.step('发送请求'):
            allure.attach(str(result.request.url),'请求路径')
            allure.attach(str(result.request.method),'请求方式')
            allure.attach(str(result.request.headers),'请求头')
            allure.attach(str(result.request.body),'请求体')

        with allure.step('获取响应'):
            allure.attach(str(result.status_code),'响应状态码')
            allure.attach(str(result.headers),'响应头')
            allure.attach(str(result.text),'响应文本内容')

        with allure.step('断言'):
            allure.attach(str(statusCode),'预期响应状态码')
            allure.attach(str(errorCode),'预期返回错误码')
            allure.attach(str(msg),'预期返回错误信息')

            assert result.status_code == int(statusCode)
            assert result.json()['status'] == int(errorCode)
            assert result.json()['msg'] == msg




