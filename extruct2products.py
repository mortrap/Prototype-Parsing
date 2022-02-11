#!/usr/bin/env python

from curses import keyname
import extruct
from llog import log
import datetime
import yaml


def extruct2products(html):
  products = []
  dick = extruct.extract(html, uniform=True, errors='ignore')

  if False:
    with open('delme.yaml', 'wb') as f:
      f.write(yaml.dump(dick, encoding='utf-8', allow_unicode=True))
    exit(1)

  if 'microdata' in dick:

    for item in dick['microdata']:
      if item['@type'] != 'Product':
        continue
      if not 'name' in item:
        continue
      if not 'offers' in item:
        continue
      product = {}
      for key in ['name', 'brand', 'description', 'gtin8', 'sku', 'image']:
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
# copied out microdata
  if 'json-ld' in dick:
    for item in dick['json-ld']:
      if item['@type'] != 'Product':
        continue
      if not 'name' in item:
        continue
      if not 'offers' in item:
        continue
      product = {}
      for key in ['name', 'brand', 'description', 'gtin8', 'sku', 'image']:
        if key in item:
          product[key] = item[key]

      if item['offers']:
        offers = item['offers']
        in_stock = 'availability' in offers and offers['availability'] == 'https://schema.org/InStock'
        new = 'itemCondition' in offers and offers['itemCondition'] == 'https://schema.org/NewCondition'
        used = 'itemCondition' in offers and offers['itemCondition'] == 'https://schema.org/UsedCondition'
        priceCurrency = offers['priceCurrency'] if offers['priceCurrency'] else ''
        price = offers['price'] if offers['price'] else ''
        if price and priceCurrency and in_stock and new or used:
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

  # tbd, not tested yet
  if 'rdfa' in dick:
    product = {}
    for item in dick['rdfa']:
      for [key, kʹ] in [['http://ogp.me/ns#title', 'name'], ['http://ogp.me/ns#description', 'description'],
                        ['http://ogp.me/ns#image:', 'image'], ['product:price:currency', 'currency'],
                        ['product:price:amount', 'price']]:
        if key in item:
          for map in item[key]:
            if not '@value' in map:
              continue
            product[kʹ] = map['@value']

        if not product['name'] in [i['name'] for i in products]:
          if 'price' in product and 'currency' in product and 'name' in product:
            products.append(product)

  # tbd, needs an example with price
  # if 'dublincore' in dick:
  #   for item in dick['duplincore']:
  #     print(item)
  # ⌥ consider merging different formats into a single results,
  #    or removing product duplicates by name

  return products


# периодически возвращаясь к файлу, под который это было написано изначально
def test_extruct2products():
  for [fn, price] in [['jsonld.html', None], ['schema-org.html', 399]]:
    html = open(f"test-data/{fn}", 'r', encoding='utf-8', errors='ignore').read()
    start = datetime.datetime.now()
    got = extruct2products(html)
    delta = datetime.datetime.now() - start
    #log(delta)
    log(yaml.dump(got))
    # ⌥ check whether the `price` matches the one we've got


if __name__ == "__main__":
  test_extruct2products()
# @value python with output from "rdfa
