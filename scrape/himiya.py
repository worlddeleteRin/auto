import scrapy
from urllib.parse import urljoin
import os


PATH = os.getcwd()

main_path = 'https://avs-auto.ru/catalog/avtohimiya-i-kosmetika/'
p = 15
site_path = []
for i in range(1, p):
    path = main_path + '?p=' + str(i)
    site_path.append(path)



class AvtoHimiya(scrapy.Spider):
    name = 'avto_himiya'
    start_urls = site_path

    def parse(self, r):
        for item in r.css('.product-view_wrap'):
            imgurl = 'https://avs-auto.ru' + item.css('img::attr(src)').extract_first()
            name = item.css('.product-name a::text').extract_first()
            product_href = 'https://avs-auto.ru' + item.css('.product-name a::attr(href)').extract_first()

            yield scrapy.Request(product_href, callback = self.parse_product, meta = {
                'imgurl': imgurl,
                'name': name,
            })

    def parse_product(self, r):
        name = r.meta.get('name')
        imgurl = r.meta.get('imgurl')
        category = r.css('.item')[-1].css('a::text').extract_first()
        sku = r.css('.rs-product-barcode::text').extract_first().strip()
        description = r.css('.characteristics::text').extract_first().strip()
        item = {
            'sku': sku,
            'name': name, 
            'imgurl': imgurl,
            'category': category,
            'description': description
        }
        yield item

        

