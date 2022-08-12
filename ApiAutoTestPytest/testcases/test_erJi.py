import allure
import pytest
from util.requestDataUtil import RequestDataUtil
from util.requestUtil import RequestUtil

# 获取网络请求工具对象
ru = RequestUtil()

# 获取请求数据对象
rdu = RequestDataUtil('erJi')
list = rdu.getRequestData()

@pytest.fixture(scope='function',params=list)
def getData(request):
    return request.param

@allure.feature('商品信息')
class TestErJi:
    @allure.story('二级分页接口')
    def test_erJi(self,getData):
        # 发送请求
        result = ru.doRequest(method=getData['method'],url=getData['url'],params=getData['params'],data=getData['data'],json=getData['json'],headers=getData['headers'])

        ru.assertResult(result,getData['validate']['statusCode'],getData['validate']['errorCode'],getData['validate']['msg'])