import yaml

from util.log import logger


class YamlUtil:
    def __init__(self,file):
        self.file = file

    def getYamlData(self):
        f = open(file=self.file,mode='r',encoding='utf-8')
        j = yaml.load(stream=f,Loader=yaml.FullLoader)
        logger.info('读取yaml配置内容:'+str(j))
        return j

if __name__ == '__main__':
    yu = YamlUtil('../config/erJi.yml')
    yu.getYamlData()