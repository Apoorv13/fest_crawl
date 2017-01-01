import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "scrape_know"
    start_urls = [
        'http://www.knowafest.com/college-fests/upcomingfests',
    ]

    def parse(self, response):
        for scrape in response.css("div.blog-thumb"):
            yield {
                'text': scrape.css(".headline.h2::text").extract_first(),
                'Type': scrape.css("dd.fa-fa-calendar::text").extract_first(),
                'Date': scrape.css("dd.fa-fa-calendar::text"),
                'IMG': scrape.css(".pull-right.h4::text").extract(),
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
             yield scrapy.Request(response.urljoin(next_page_url))