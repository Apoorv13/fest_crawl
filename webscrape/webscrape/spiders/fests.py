import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem

class MySpider(BaseSpider):
    name = "fests"
    allowed_domains = ["knowafest.com"]
    start_urls = ["http://www.knowafest.com/college-fests/events"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//span[@class='pl']")
        items = []
        for titles in titles:
            item = CraigslistSampleItem()
            item["title"] = titles.select("a/text()").extract()
            item["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items