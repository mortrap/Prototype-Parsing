import pprint
pp = pprint.PrettyPrinter(indent=0)
# Needs urllib3 2, https://github.com/urllib3/urllib3#installing
import urllib3
import extruct




#import extruct
#from fastwarc.stream_io import *
from fastwarc.warc import ArchiveIterator, WarcRecordType, WarcRecord, is_http
#from fastwarc.stream_io import BufferedReader
# fastwarc: test the streaming parsing

url ='https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2021-10/segments/1614178347293.1/warc/CC-MAIN-20210224165708-20210224195708-00004.warc.gz'
#req=requests.get(url, stream = True)
# use urllib3 to open an URL stream
req = urllib3.request("GET", url, preload_content=False)
#print(req.content)
#head = WarcHeaderMap()
def exne (html):
    metadata = extruct.extract(html ,uniform=True)#, syntaxes=['microdata', 'json-ld', 'opengraph'])     
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
# Открыть, если нету, создать и открыть файл для записи, дабы протестировать контент , читаемый fastwarc
#with open('test', 'w') as file:
count = 0
for record in ArchiveIterator(req, record_types=WarcRecordType.response, func_filter=lambda r: r.headers.get('WARC-Identified-Payload-Type') == 'text/html', max_content_length = 512000):
    pp.pprint(record.content_length)
    if record.content_length>0:
        metadata = exne(record.reader.read(record.content_length).decode('utf-8', 'ignore'))
    if uses_metadata_type(metadata, 'json-ld') or uses_metadata_type(metadata, 'microdata'):
               # if key_exists(metadata['microdata'], 'Product') or key_exists(metadata['json-ld'], 'Product'):
                #    product = get_dictionary_by_key_value(metadata, "@type", "Product")
                    pp.pprint(str(metadata))
    else:
        continue
            # count+=1
            # if count ==3:
            #     break
     #if str(record.http_headers.status_code) in record.http_headers.status_line:
     #if record.http_headers.get('Content-Type').startswith('text/html'): 

#     stream = GZipStream(FileStream('warcfile.warc.gz', 'rb'))

# for record in ArchiveIterator(stream, record_types=WarcRecordType.request | WarcRecordType.response):
#     pass
# from fastwarc.stream_io import *

# # GZip:
# stream = GZipStream(open('warcfile.warc.gz', 'rb'))

# # LZ4:
# stream = LZ4Stream(open('warcfile.warc.lz4', 'rb'))
# string html 
# def extract_metadata(text):




# if key_exists(metadata['microdata'], 'Product') or key_exists(metadata['json-ld'], 'Product') or key_exists(metadata['opengraph'], 'Product'):
#     pp.pprint (metadata)
# uses_metadata_type(metadata, 'json-ld')
# uses_metadata_type(metadata, 'opengraph')
# uses_metadata_type(metadata, 'microdata')    
# uses_metadata_type(metadata, 'rdfa')
# key_exists(metadata['microdata'], 'Product')
# key_exists(metadata['opengraph'], 'Product')
# key_exists(metadata['json-ld'], 'Product')

# df = pd.DataFrame(columns = ['url', 'microdata', 'json-ld', 'opengraph'])

# for url in sites:    
#     metadata = extract_metadata(url)
#     urldata = urlparse(url)

#     row = {
#         'url': urldata.netloc, 
#         'microdata': uses_metadata_type(metadata, 'microdata'),
#         'json-ld': uses_metadata_type(metadata, 'json-ld'),
#         'opengraph': uses_metadata_type(metadata, 'opengraph'),               
#     }

#     df = df.append(row, ignore_index=True)

# df.head(10).sort_values(by='microdata', ascending=False)
