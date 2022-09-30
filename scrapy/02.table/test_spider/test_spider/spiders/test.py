import scrapy
import pandas as pd


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['learn.microsoft.com']
    start_urls = ['https://learn.microsoft.com/ja-jp/azure/virtual-machines/dplsv5-dpldsv5-series']

    def parse(self, response):
        table = response.xpath('//*[@id="main"]/div[3]/div[2]')[0]

        trs = table.xpath('//table/tbody/tr')

        for tr in trs:
            x1 = tr.xpath('//td[1]/text()')
            x2 = tr.xpath('//td[2]/text()')
            x3 = tr.xpath('//td[3]/text()')
            out_dict = {
                'x1': x1,
                'x2': x2,
                'x3': x3
            }
        
        print('BBBBBBBBBBBBBBB')
        print(out_dict)
        df = pd.DataFrame(out_dict)
        df.to_csv('test.csv')
