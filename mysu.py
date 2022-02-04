
import pprint
pp = pprint.PrettyPrinter(indent=0, width=50)
# Needs urllib3 2, https://github.com/urllib3/urllib3#installing
import urllib3
import extruct
import numpy as np
from extruct2products import extruct2products as ex
import requests
import urllib3
import yaml
#import extruct
#from fastwarc.stream_io import *
from fastwarc.warc import ArchiveIterator, WarcRecordType, WarcRecord, is_http
#from fastwarc.stream_io import BufferedReader
# fastwarc: test the streaming parsing

url ='https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2021-10/segments/1614178347293.1/warc/CC-MAIN-20210224165708-20210224195708-00004.warc.gz'
#req=requests.get(url, stream = True)
# use urllib3 to open an URL stream

#req =  requests.request(method="get",url=url) # its not working


req = urllib3.request("GET", url, preload_content=False)# its working

    
        
#print(req.content)

def exne (html):
    metadata = extruct.extract(html , uniform=True, errors='ignore')     
    return metadata

def uses_metadata_type(metadata, metadata_type):
    if (metadata_type in metadata.keys()) and (len(metadata[metadata_type]) > 0):
        return True
    else:
        return False 

def read_cl(record , cl):
     return record.reader.read(cl)

def get_dictionary_by_key_value(dictionary, target_key, target_value):
    for key in dictionary:
        if len(dictionary[key]) > 0:
            for item in dictionary[key]:
                if item[target_key] == target_value:
                    return item

def key_exists(dict, key):
    if not any(item['@type'] == key for item in dict):
        return False
    else:
        return True 
        #lambda r: r.headers.get('WARC-Identified-Payload-Type') == 'text/html'
# !Открыть, если нету, создать и открыть файл для записи, дабы протестировать контент , читаемый fastwarc
#with open('test', 'w') as file:

count = 0
for record in ArchiveIterator(req, record_types = WarcRecordType.response, func_filter = lambda r: r.headers.get('WARC-Identified-Payload-Type') == 'text/html', max_content_length = 512000):
    
    #mb forgot lxml.etree
    if record.content_length>0:
        # !Записываем в словарь что считали при помощи extruct
        
        reccl = record.content_length
        metadata = exne((record.reader.read(reccl)).decode('utf-8', 'ignore'))
        
        # !Если тип метаданных json-ld or microdata извлекаем, 
        # if uses_metadata_type(metadata, 'json-ld') or uses_metadata_type(metadata, 'microdata'):
        #     # Не понимаю как отсеять нужные мне значения, работа со словарем
        #         if'@type' in str(metadata.values()):
        #                 array = np.array(list(metadata.values()))
        #                 array2 = np.array_split(array, 3)
        #                 if np.isin ('@type', array2, 0, -1) & np.isin ('Product', array2, 0,-1) & np.isin ('offers', array2, 0, -1):
        #                                             ixgrid = np.ix_([3, -1])
        #                                             print(array[ixgrid])

                #metadata.clear()
                #product = get_dictionary_by_key_value(metadata, "microdata", "Product")
                #if key_exists(metadata['json-ld'], 'Product') or key_exists(metadata['microdata'], 'Product'):
                            #product = get_dictionary_by_key_value(metadata, "@type", "Product")
                            #print(product)
                            # array = np.array(list(metadata.values()))
                            # array2 = np.array_split(array, 3)
                            # if np.isin ('@type', array2, 0, -1) & np.isin ('Product', array2, 0,-1) & np.isin ('offers', array2, 0, -1):
                            #                             array3 = np.where(array2, '@type', 'Product')
                            #                             print(metadata.items)
                    # results = metadata.items()
                    # data = list (results)
                    # npArray = np.array(data)
                    # arr = np.isin('@type', npArray)
                    # print(arr)
#     import http.client
# c = http.client.HTTPSConnection('shops.mercatos.net')
# c.request("GET", "/ru/")
# r = c.getresponse()
# print(r.status)                