import pytest


list =[ {'name':'zhangsan','pwd':'123'},{'name':'wangwu','pwd':'456'}]
@pytest.fixture(scope='function',params=list)
def getData(request):

    print('这是fixture')
    return request.param

class TestDmo:

    def add(self, a, b):
        return a + b
    
    # list = [(1, 2), (3, 4), (5, 6)]
    #
    # @pytest.mark.parametrize("a,b", list)
    # def test_add3(self, a, b):
    #     sum = self.add(a, b)
    #     print(sum, a, b)

class TestDmo2:

    def test_add(self,getData):
        print('add',getData)
        print('-=======')