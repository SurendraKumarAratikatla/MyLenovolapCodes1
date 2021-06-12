import scrapy
from ..items import Quote2Item

class quote2(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        all_div_quotes = response.css('div.quote')
        items = Quote2Item()
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tags = quote.css('a.tag::text').extract()
        items['title'] = title
        items['author'] = author
        items['tags'] = tags
        yield items
