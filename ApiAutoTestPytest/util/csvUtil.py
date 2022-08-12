import csv

from util.log import logger


class CsvUtil:
    def __init__(self,file):
        self.file = file

    def getCsvData(self):
        f = open(file=self.file,mode='r',encoding='utf-8-sig')
        reader = list(csv.reader(f))
        # [{'csid':1,'page':1},{}]
        dictList = []
        for i in range(1,len(reader)):
            dict = {} # 一条数据的字典
            data = reader[i] #一条csv数据
            keys = reader[0] #key数据
            for j in range(len(keys)):
                dict[keys[j]] = data[j] # 组装一条字典

            dictList.append(dict) #添加到列表

        logger.info('读取csv格式化内容:'+str(dictList))
        return dictList


# if __name__ == '__main__':
#     cu = CsvUtil('../data/erJi.csv')
#     cu.getCsvData()