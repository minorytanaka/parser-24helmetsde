from scrapy import Request, Spider, Selector
from scrapy.http import Response
from helmets.settings import COOKIES, HEADERS, XPATH
from w3lib.url import add_or_replace_parameter
from collections import defaultdict
from random import choice


class HelmetsSpider(Spider):
    name = "helmets"
    allowed_domains = ["www.24helmets.de"]
    start_urls = ["https://www.24helmets.de/helme/visiere/flat-visiere"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cookies = COOKIES
        self.headers = HEADERS

    def start_requests(self):
        for url in self.start_urls:
            url = add_or_replace_parameter(url, "p", "1")
            yield Request(
                url=url,
                callback=self.parse_category,
                cookies=self.cookies,
                headers=self.headers,
                meta={"page": 1},
            )

    def parse_category(self, response: Response):
        if response.status != 200:
            self.logger.warning(f"Хуевый (плохой) статус код: {response.status} для ссылки (ну вдруг пригодится) {response.url}")
            return

        product_links = response.xpath(XPATH["product_link"]).getall()
        if not product_links:
            self.logger.info(f"Ебать ну нету товаров на странице с номером: {response.meta['page']}")
            return

        for product_link in product_links:
            yield Request(
                url=product_link,
                callback=self.parse_product,
                cookies=self.cookies,
                headers=self.headers,
            )
        page = str(response.meta["page"] + 1)
        url = add_or_replace_parameter(response.url, "p", page)
        yield Request(
            url=url,
            callback=self.parse_category,
            cookies=self.cookies,
            headers=self.headers,
            meta={"page": int(page)}
        )

    def parse_product(self, response: Response):
        variants = self.get_all_variants(response)
        if not variants:
            # Если нет вариантов парсим как есть
            yield self.parse_single_product(response)
            return

        product_configurator = response.xpath(XPATH["product_configurator"]).get()
        product_conf = Selector(text=product_configurator)
        select_fields = product_conf.xpath('//select[@name]')
        for select in select_fields:
            param_name = select.xpath('./@name').get()
            if param_name:
                values = select.xpath('./option/@value').getall()
                non_empty_values = [v for v in values if v.strip()]
                if non_empty_values:
                    variants[param_name] = non_empty_values
        print(variants)
        product_item = {
            "link": self.get_link(response),
            "title": self.get_title(response),
            "price": self.get_price(response),
        }
        yield product_item

    def get_all_variants(self, response: Response):
        ...

    def parse_single_product(self, response: Response):
        ...

    def get_link(self, response: Response):
        sku = response.xpath()

    def get_title(self, response: Response):
        return response.xpath(XPATH["title"]).getall()[0].rstrip().lstrip()

    def get_price(self, response: Response):
        return response.xpath(XPATH["price"]).getall()[0].rstrip().lstrip()
