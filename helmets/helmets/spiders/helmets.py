from scrapy import Request, Spider
from scrapy.http import Response
from helmets.settings import COOKIES, HEADERS, XPATH


class HelmetsSpider(Spider):
    name = "helmets"
    allowed_domains = ["www.24helmets.de"]
    start_urls = ["https://www.24helmets.de/helme/visiere/flat-visiere"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cookies = COOKIES
        self.headers = HEADERS

    async def start(self):
        for url in self.start_urls:
            url += "?p=1"
            yield Request(
                url=url,
                callback=self.parse_category,
                cookies=self.cookies,
                headers=self.headers,
            )

    def parse_category(self, response: Response):
        product_links = response.xpath(XPATH["product_link"]).getall()
        if not product_links:
            return
        for product_link in product_links:
            yield Request(
                url=product_link,
                callback=self.parse_product,
                cookies=self.cookies,
                headers=self.headers,
            )
        url = f"{response.url[:len(response.url)-1]}{int(response.url[-1]) + 1}"
        yield Request(
            url=url,
            callback=self.parse_category,
            cookies=self.cookies,
            headers=self.headers,
        )

    def parse_product(self, response: Response):


        product_item = {
            "link": self.get_link(response),
            "title": self.get_title(response),
            "price": self.get_price(response),
        }
        yield product_item

    def get_link(self, response: Response):
        sku = response.xpath()

    def get_title(self, response: Response):
        return response.xpath(XPATH["title"]).getall()[0].rstrip().lstrip()

    def get_price(self, response: Response):
        return response.xpath(XPATH["price"]).getall()[0].rstrip().lstrip()
