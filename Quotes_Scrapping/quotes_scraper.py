import scrapy


class QuotesScraperSpider(scrapy.Spider):
    name = "quotes_scraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes:
            yield {
                'Quote': quote.css('span.text::text').get(),
                'Author': quote.css('small.author::text').get(),
                'About': quote.css('span a::attr("href")').get()
            }
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow("https://quotes.toscrape.com/"+next_page, callback=self.parse)