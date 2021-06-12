import scrapy
from ..items import Quote1Item

class quotespider(scrapy.Spider):
    name = 'quote'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        items = Quote1Item()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('small.author::text').extract()
            tag = quotes.css('a.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items