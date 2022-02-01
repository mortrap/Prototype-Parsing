import extruct
from llog import log
import datetime
import yaml
import json


def extruct2products(html):
  products = []
  dick = extruct.extract(html, uniform=True, errors='ignore')

  if 'microdata' in dick:
    for item in dick['microdata']:
      if item['@type'] != 'Product':
        continue
      if not 'name' in item:
        continue
      if not 'offers' in item:
        continue
      product = {}
      for key in ['name', 'brand', 'description', 'gtin8', 'image']:
        if key in item:
          product[key] = item[key]

      if item['offers']:
        offers = item['offers']
        in_stock = 'availability' in offers and offers['availability'] == 'http://schema.org/InStock'
        new = 'itemCondition' in offers and offers['itemCondition'] == 'http://schema.org/NewCondition'
        priceCurrency = offers['priceCurrency'] if offers['priceCurrency'] else ''
        price = offers['price'] if offers['price'] else ''
        if price and priceCurrency and in_stock and new:
          product['price'] = price
          product['currency'] = priceCurrency
          products.append(product)

  if 'opengraph' in dick:
    for item in dick['opengraph']:
      if item['@type'] != 'product':
        continue
      if not 'og:title' in item:
        continue
      if not 'product:price:amount' in item:
        continue
      if not 'product:price:currency' in item:
        continue
      product = {}
      for [key, kʹ] in [['og:title', 'name'], ['og:description', 'description'], ['og:image', 'image'],
                        ['product:price:currency', 'currency'], ['product:price:amount', 'price']]:
        if key in item:
          product[kʹ] = item[key]

      # ⌥ consider merging different formats into a single results,
      #    or removing product duplicates by name
      if product['name'] in [i['name'] for i in products]:
        continue

      products.append(product)

  return products


def test_extruct2products():
  html = open('test-data/schema-org.html').read()
  start = datetime.datetime.now()
  got = extruct2products(html)
  delta = datetime.datetime.now() - start
  #log(delta)
  log(yaml.dump(got))
  log(json.dumps(got, indent=2))


if __name__ == "__main__":
  test_extruct2products()
