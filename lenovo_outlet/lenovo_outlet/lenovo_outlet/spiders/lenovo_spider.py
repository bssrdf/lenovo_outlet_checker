from scrapy.spiders import CrawlSpider, Spider
from scrapy import Selector
import time

class LenovoSpider(Spider):
    name = "lenovo"
    allowed_domains = ["www3.lenovo.com", "www.lenovo.com"]
    start_urls = ["https://www3.lenovo.com/us/en/outletus/laptops/c/\
    LAPTOPS?q=%3Aprice-asc%3AfacetSys-Brand%3AThink&uq=&text=#"]

    def parse(self, response):
        pagesource = Selector(response)
        entries = pagesource.xpath('//div[@id="results-area"]')
        for laptop in entries.xpath('.//div[@class=\
        "facetedResults-item only-allow-small-pricingSummary"]'):
            yield {
                'date': time.strftime("%x"),
                'name': laptop.xpath('.//h3[@class=\
                "facetedResults-title"]/a/text()').extract()[0].strip(),
                'stock': laptop.xpath('.//span[@class=\
                "rci-msg"]/text()').extract()[0].strip()
            }
