import extruct
#from llog import log
import datetime
import yaml
#import json

# не прошла на другом файле из примера, причину искал print statement
def extruct2products(html):
  products = []
  dick = extruct.extract(html, uniform=True, errors='ignore')
  ## Hier ok
  #microdata
  if 'microdata' in dick:
    for item in dick['microdata']:
      ## Hier not
      #print(item)
      if item['@type'] != 'Product' and item['@type'] != 'Offer' and item['@type'] != 'Brand': # or ?
        continue
      #ok
      #print(item)
      ## Hier not
      product ={}
      if not 'name' in item and not 'price' in item:# and not 'Brand' in item: #or ?
        continue
      #ok
      #print(item)
      for key in ['name']:
        if key in item:
          product[key] = item[key]
      # Протащить имя из Brand
      if not 'offers' in item and 'name' in item:
        continue
      #ok
      #print(item)
      
      for key in ['name', 'brand', 'description', 'gtin8', 'image', 'sku', 'url']:
        if key in item:
          product[key] = item[key]
      
      #print(product)
      #print(yaml.dump(dick))
      if item['offers']:
        offers = item['offers']
      
        in_stock = 'availability' in offers and offers['availability'] == 'http://schema.org/InStock'
        new = 'itemCondition' in offers and offers['itemCondition'] == 'http://schema.org/NewCondition'
        priceCurrency = offers['priceCurrency'] if offers['priceCurrency'] else ''
        price = offers['price'] if offers['price'] else ''
        #print(price, priceCurrency)#ok 1190.00 RUB #and
        if price and priceCurrency or in_stock and new:
          product['price'] = price
          product['currency'] = priceCurrency
          products.append(product)

   #opengraph       
  if 'opengraph' in dick:
    for item in dick['opengraph']:
      if item['@type'] != 'product':
        continue
      
      if not 'og:title' in item  and not 'og:url' in item:
        continue
      
      if not 'product:price:currency' and not 'product:price:amount':
        continue
      #print(item)
      
      product = {}
      for [key, kʹ] in [['og:title', 'name'], ['og:description', 'description'], ['og:image', 'image'],
                        ['product:price:currency', 'currency'], ['product:price:amount', 'price']]:
        if key in item:
          product[kʹ] = item[key]
        #print(products) 
      #print(product['name']) Ok
# @value?
#rdfa
  if 'rdfa' in dick:
    for item in dick['rdfa']:
      if not 'http://ogp.me/ns#title' in item: continue
      
      if not 'http://ogp.me/ns#type' in item: continue
      
      if not 'product:price:amount' in item: continue
      print(item)
      if not 'product:price:currency' in item: continue 
      
      if not '@value' in item: continue
      product = {}
      for [key, kʹ] in [['http://ogp.me/ns#title', 'name'], ['http://ogp.me/ns#description', 'description'], ['http://ogp.me/ns#image:', 'image'],
                        ['product:price:currency', 'currency'], ['product:price:amount', 'price']]:
        if key in item:
          product[kʹ] = item[key]
  # if 'dublincore' in dick:
  #   for item in dick['duplincore']:
  #     print(item)
      # ⌥ consider merging different formats into a single results,
      #    or removing product duplicates by name
      
      if product['name'] in [i['name'] for i in products]:
        continue
      
      products.append(product)

  return products
  

# периодически возвращаясь к файлу, под который это было написано изначально
def test_extruct2products():
  html = open('test-data/Наушники JBL T210, чёрный купить в Красноярске _ Технопарк.html', 'r').read()
  start = datetime.datetime.now()
  got = extruct2products(html)
  delta = datetime.datetime.now() - start
  #log(delta)
  print(yaml.dump(got))
  #print(json.dumps(got, indent=2))


if __name__ == "__main__":
  test_extruct2products()
# @value python with output from "rdfa

