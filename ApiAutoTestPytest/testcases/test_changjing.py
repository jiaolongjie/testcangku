import allure

from util.changJingRequestUtil import ChangJingRequestUtil
from util.requestUtil import RequestUtil

@allure.feature('场景')
class TestChangJing:

    @allure.story('场景测试01')
    def test_changjing_01(self):
        ru = RequestUtil()
        cjru = ChangJingRequestUtil('changjing_01', ru)
        cjru.yamlAndRequest()

    @allure.story('场景测试02')
    def test_changjing_02(self):
        ru = RequestUtil()
        cjru = ChangJingRequestUtil('changjing_02', ru)
        cjru.yamlAndRequest()