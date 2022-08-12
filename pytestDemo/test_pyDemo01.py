import pytest
from pytest_assume.plugin import assume


@pytest.fixture(scope='module',autouse=False)
def getData():
    print('这是一句话')

class TestDmo:

    def add(self, a, b):
        return a + b

    # @pytest.mark.skip('不执行')
    # def test_add(self):
    #     s = self.add(2, 3)
    #     print('--------这里' + str(s) + '-----')
    #     assert 5 == s

    # @pytest.mark.smoke
    def test_add2(self,getData):
        print('-----------------能执行到------------')
        assume(5 == 5)
        assume(3 == 3)


    list = [(1, 2), (3, 4), (5, 6)]

    # @pytest.mark.parametrize("a,b", list)
    # def test_add3(self, a, b):
    #     sum = self.add(a, b)
    #     print(sum, a, b)

class TestDmo2:

    def test_add(self,getData):
        print('-=======')