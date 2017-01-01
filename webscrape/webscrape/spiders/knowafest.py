import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'knowafest'

    start_urls = ['http://www.knowafest.com/college-fests/upcomingfests']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('.author+a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_author)

        # follow pagination links
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        

        yield {
            'name': extract_with_css('.headline.h2::text'),
            'date': extract_with_css('dd.fa-fa-calendar::text'),
            'mail': extract_with_css('.pull-right.h4::text'),
            'emails': re.findall(r'[\w\.-]+@[\w\.-]+', response.body),
            
        }