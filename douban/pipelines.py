# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
from scrapy.conf import settings


class DoubanPipeline(object):
    def __init__(self):
        # self.filename = open('douban.json', 'wb')
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        db_name = settings['MONGO_DBNAME']
        sheet_name = settings['MONGO_SHEETNAME']

        # 创建数据库连接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[db_name]
        # 存放数据的表名
        self.sheetname = mydb[sheet_name]

    def process_item(self, item, spider):
        # jsontext = json.dumps(dict(item), ensure_ascii=False) + '\n'
        # self.filename.write(jsontext.encode('utf-8'))

        data = dict(item)
        self.sheetname.insert(data)

        return item

    # def close_spider(self, spider):
        # self.filename.close()