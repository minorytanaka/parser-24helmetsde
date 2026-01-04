# Scrapy settings for helmets project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "helmets"

SPIDER_MODULES = ["helmets.spiders"]
NEWSPIDER_MODULE = "helmets.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "helmets (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "helmets.middlewares.HelmetsSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "helmets.middlewares.HelmetsDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "helmets.pipelines.HelmetsPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"


COOKIES = {
    'session-1': 'f92266d78682b839d2a429bade72e22363e0c3ae70d8cce4c0cb0c968b4aa45d',
    '__csrf_token-1': 'PSc9H6xmUlHV1pq2j4SOTKCj2sVeXW',
    'cookiePreferences': '{"groups":{"technical":{"name":"technical","cookies":{"cookieDeclined":{"name":"cookieDeclined","active":true},"allowCookie":{"name":"allowCookie","active":true},"shop":{"name":"shop","active":true},"csrf_token":{"name":"csrf_token","active":true},"cookiePreferences":{"name":"cookiePreferences","active":true},"x-cache-context-hash":{"name":"x-cache-context-hash","active":true},"slt":{"name":"slt","active":true},"nocache":{"name":"nocache","active":true},"technical":{"name":"technical","active":true},"paypal-cookies":{"name":"paypal-cookies","active":true},"session":{"name":"session","active":true},"currency":{"name":"currency","active":true}},"active":true},"comfort":{"name":"comfort","cookies":{"sUniqueID":{"name":"sUniqueID","active":true}},"active":true},"statistics":{"name":"statistics","cookies":{"x-ua-device":{"name":"x-ua-device","active":true},"dis_gads":{"name":"dis_gads","active":true},"dis_ga":{"name":"dis_ga","active":true},"dis_gtag":{"name":"dis_gtag","active":true},"dis_meta":{"name":"dis_meta","active":true},"dis_mads":{"name":"dis_mads","active":true},"partner":{"name":"partner","active":true},"dis_pinterest":{"name":"dis_pinterest","active":true},"dis_tiktok":{"name":"dis_tiktok","active":true}},"active":true}},"hash":"WyJhbGxvd0Nvb2tpZSIsImNvbWZvcnQiLCJjb29raWVEZWNsaW5lZCIsImNvb2tpZVByZWZlcmVuY2VzIiwiY3NyZl90b2tlbiIsImN1cnJlbmN5IiwiZGlzX2dhIiwiZGlzX2dhZHMiLCJkaXNfZ3RhZyIsImRpc19tYWRzIiwiZGlzX21ldGEiLCJkaXNfcGludGVyZXN0IiwiZGlzX3Rpa3RvayIsIm5vY2FjaGUiLCJwYXJ0bmVyIiwicGF5cGFsLWNvb2tpZXMiLCJzVW5pcXVlSUQiLCJzZXNzaW9uIiwic2hvcCIsInNsdCIsInN0YXRpc3RpY3MiLCJ0ZWNobmljYWwiLCJ0ZWNobmljYWwiLCJ4LWNhY2hlLWNvbnRleHQtaGFzaCIsIngtdWEtZGV2aWNlIl0="}',
    'nocache': 'detail-1',
    '_gcl_au': '1.1.977193928.1765702239',
    '_ga': 'GA1.1.2081315380.1765702240',
    '_ga_KPV2TQSJBG': 'GS2.1.s1765702239$o1$g1$t1765702317$j60$l0$h0',
    '_ga_Y4ZVYEMXLR': 'GS2.1.s1765702239$o1$g1$t1765702317$j60$l0$h0',
    'x-ua-device': 'tablet',
}

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.24helmets.de/helme/visiere/flat-visiere?p=6',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    # 'cookie': 'session-1=f92266d78682b839d2a429bade72e22363e0c3ae70d8cce4c0cb0c968b4aa45d; __csrf_token-1=PSc9H6xmUlHV1pq2j4SOTKCj2sVeXW; cookiePreferences={"groups":{"technical":{"name":"technical","cookies":{"cookieDeclined":{"name":"cookieDeclined","active":true},"allowCookie":{"name":"allowCookie","active":true},"shop":{"name":"shop","active":true},"csrf_token":{"name":"csrf_token","active":true},"cookiePreferences":{"name":"cookiePreferences","active":true},"x-cache-context-hash":{"name":"x-cache-context-hash","active":true},"slt":{"name":"slt","active":true},"nocache":{"name":"nocache","active":true},"technical":{"name":"technical","active":true},"paypal-cookies":{"name":"paypal-cookies","active":true},"session":{"name":"session","active":true},"currency":{"name":"currency","active":true}},"active":true},"comfort":{"name":"comfort","cookies":{"sUniqueID":{"name":"sUniqueID","active":true}},"active":true},"statistics":{"name":"statistics","cookies":{"x-ua-device":{"name":"x-ua-device","active":true},"dis_gads":{"name":"dis_gads","active":true},"dis_ga":{"name":"dis_ga","active":true},"dis_gtag":{"name":"dis_gtag","active":true},"dis_meta":{"name":"dis_meta","active":true},"dis_mads":{"name":"dis_mads","active":true},"partner":{"name":"partner","active":true},"dis_pinterest":{"name":"dis_pinterest","active":true},"dis_tiktok":{"name":"dis_tiktok","active":true}},"active":true}},"hash":"WyJhbGxvd0Nvb2tpZSIsImNvbWZvcnQiLCJjb29raWVEZWNsaW5lZCIsImNvb2tpZVByZWZlcmVuY2VzIiwiY3NyZl90b2tlbiIsImN1cnJlbmN5IiwiZGlzX2dhIiwiZGlzX2dhZHMiLCJkaXNfZ3RhZyIsImRpc19tYWRzIiwiZGlzX21ldGEiLCJkaXNfcGludGVyZXN0IiwiZGlzX3Rpa3RvayIsIm5vY2FjaGUiLCJwYXJ0bmVyIiwicGF5cGFsLWNvb2tpZXMiLCJzVW5pcXVlSUQiLCJzZXNzaW9uIiwic2hvcCIsInNsdCIsInN0YXRpc3RpY3MiLCJ0ZWNobmljYWwiLCJ0ZWNobmljYWwiLCJ4LWNhY2hlLWNvbnRleHQtaGFzaCIsIngtdWEtZGV2aWNlIl0="}; nocache=detail-1; _gcl_au=1.1.977193928.1765702239; _ga=GA1.1.2081315380.1765702240; _ga_KPV2TQSJBG=GS2.1.s1765702239$o1$g1$t1765702317$j60$l0$h0; _ga_Y4ZVYEMXLR=GS2.1.s1765702239$o1$g1$t1765702317$j60$l0$h0; x-ua-device=tablet',
}

XPATH = {
    "product_link": "//div[@class='product--info']//a[@class='product--title']/@href",
    "title": "//h1[@class='product--title']//text()",
    "price": "//span[contains(@class, 'price--content')]/meta[@itemprop='price']/@content",
    "sku": "",
    "product_configurator": "//div[@class='product--configurator']//p[@class='configurator--label']"
}

ROTATING_PROXY_LIST = ["http://jUvPyT:JS0y2C@178.171.42.166:9491"]
DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 110,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 120,
}



# <select name="group[5]" data-ajax-select-variants="true">
#     <option value="">Bitte wählen</option>
#     <option value="107"> Transparent (ECE) </option>
#     <option selected="selected" value="771"> Grau (ECE) </option>
#     <option value="76"> Dunkelgrau </option> <option value="53"> Silber verspiegelt </option>
#     <option value="83"> Gold verspiegelt </option>
# </select>

# GRAU https://www.24helmets.de/agv-tourmodular-visier-flat-shield?group[5]=771&group[4]=515&template=ajax
# GOLD https://www.24helmets.de/agv-tourmodular-visier-flat-shield?group[5]=83&group[4]=515&template=ajax


# <select name="group[5]" data-ajax-select-variants="true">
#     <option value="" selected="selected">Bitte wählen</option>
#     <option value="76"> Dunkelgrau </option>
# </select>

# DUNKELGRAU https://www.24helmets.de/bell-visier-3-snap-flat-shield?group[5]=76&template=ajax&c=138


# <select name="group[5]" data-ajax-select-variants="true">
#     <option value="" selected="selected">Bitte wählen</option>
#     <option disabled="" value="646"> Rainbow verspiegelt (GEN 2) - Nicht mehr lieferbar </option>
#     <option value="651"> Gelb (GEN 2) </option> <option disabled="" value="665"> Transparent (GEN 2, ECE) - Nicht mehr lieferbar </option>
# </select>

# GELB https://www.24helmets.de/biltwell-lane-splitter-visier-flat-shield-ece-22.05?group[5]=651&template=ajax&c=138