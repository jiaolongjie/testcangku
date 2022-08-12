import pytest
'''
1.执行main函数 进行pytest单元测试
2.执行allure执行 生成报告
    allure generate ./json -o ./report --clean
3.启动allure服务
    allure open report --host 192.168.1.165 --port 8800
    输入地址 查看报告
'''
if __name__ == '__main__':
    pytest.main(['-v', '-s', '../testcases', '--alluredir=../json'])