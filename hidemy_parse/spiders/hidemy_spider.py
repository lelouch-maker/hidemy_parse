import scrapy
from urllib.parse import urljoin
from hidemy_parse import items
class HidemySpider(scrapy.Spider):
    name = "hidemy"
    allowed_domain=['hidemy.name']
    start_urls = ['https://hidemy.name/ru/proxy-list/']


    def parse(self, response):
        for table in response.xpath('//div[@class="table_block"]//table//tbody//tr'):
            data=table.xpath('td//text()').extract()
            Proxy=items.proxy()
            Proxy['protocol'] = data[-3]
            Proxy['ip'] = data[0]
            Proxy['port'] = data[1]
            yield Proxy
        next_page = response.xpath('//li[@class="next_array"]/a/@href').extract_first()
        if next_page is not None:
            next_page_url = urljoin(response.url, next_page)
            print('############################################################################')
            print('############################################################################')
            print('############################################################################')
            print(scrapy.Request(url=next_page_url, callback=self.parse))
            print('############################################################################')
            print('############################################################################')
            print('############################################################################')
            yield scrapy.Request(url=next_page_url, callback=self.parse, dont_filter=True)
