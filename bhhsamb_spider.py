import scrapy
from ..items import BhhsambItem


class BhhsambSpiderSpider(scrapy.Spider):
    name = 'bhhsamb_spider'
    page_number = 2
    start_urls = ['https://www.bhhsamb.com/agents']

    def parse(self, response):
        items = BhhsambItem()
        name = response.css('a::text').extract()
        image_url = response.css('img::attr(src)').extract()
        contact_details = response.css('.non-link::text').extract()

        items['name'] = name
        items['image_url'] = image_url
        items['contact_details'] = contact_details


        yield items

        next_page = 'https://www.bhhsamb.com/agents?page=' + str(BhhsambSpiderSpider.page_number) +''
        if BhhsambSpiderSpider.page_number <= 43:
            yield response.follow(next_page, callback = self.parse)
