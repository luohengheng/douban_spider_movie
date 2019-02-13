# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanProjectSpider(scrapy.Spider):
    name = 'douban_project'
    allowed_domains = ['movie.douban.com']

    url = 'https://movie.douban.com/top250?start='
    start_num = 0
    start_urls = [url + str(start_num)]

    def parse(self, response):
        li_list = response.xpath('//ol[@class="grid_view"]/li')
        print(li_list)
        for each in li_list:
            item = DoubanItem()

            item['name'] = each.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['content'] = each.xpath('.//div[@class="bd"]/p/text()').extract()[0]
            item['star'] = each.xpath('.//div[@class="bd"]/div[@class="star"]/span[2]/text()').extract()[0]

            yield item
        if self.start_num < 225:
            self.start_num += 25

        yield scrapy.Request(self.url + str(self.start_num), callback=self.parse)
