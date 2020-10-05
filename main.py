from scrapy.spiders import SitemapSpider

filename = "result.txt"
try:
    file = open(filename, "a")
    file.close()
except FileNotFoundError:
    file = open(filename, "c")
    file.close()


class MySpider(SitemapSpider):
    name = "djinni"
    allowed_domains = ["djinni.co"]
    sitemap_urls = ["https://djinni.co/sitemap.xml"]

    def parse(self, response):
        with open(filename, 'r') as rf:
            if response.url not in rf.readlines():
                with open(filename, 'a') as f:
                    f.write(response.url + "\n")
                    self.log('Saved file %s' % filename)
