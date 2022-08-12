'''
全局变量 存储 获取
'''
from util.log import logger


class Variable:
    def set(self,key,value):
        logger.info('保存键值对:key='+str(key)+',value='+str(value))
        # 保存键值对
        setattr(self,key,value)

    # 通过key键 获取值
    def get(self,key):
        logger.info('获取键值对:key='+str(key))
        if hasattr(self,key):
            return getattr(self,key)
        else:
            return None

# 初始化对象供外面存取数据
var = Variable()