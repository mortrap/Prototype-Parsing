import pprint

# Needs urllib3 2, https://github.com/urllib3/urllib3#installing
import urllib3

pp = pprint.PrettyPrinter(indent=0)
import extruct
from fastwarc.stream_io import *
from fastwarc.warc import ArchiveIterator, WarcRecordType, is_http

# fastwarc: test the streaming parsing

url = 'https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2021-10/segments/1614178347293.1/warc/CC-MAIN-20210224165708-20210224195708-00004.warc.gz'

# use urllib3 to open an URL stream
req = urllib3.request("GET", url, preload_content=False)

for record in ArchiveIterator(req):
    print(record.record_id)

# from e import e
# from exhtml import html

#     stream = GZipStream(FileStream('warcfile.warc.gz', 'rb'))

# for record in ArchiveIterator(stream, record_types=WarcRecordType.request | WarcRecordType.response):
#     pass
# from fastwarc.stream_io import *

# # GZip:
# stream = GZipStream(open('warcfile.warc.gz', 'rb'))

# # LZ4:
# stream = LZ4Stream(open('warcfile.warc.lz4', 'rb'))
# string html 
def extract_metadata(text):

    # r = requests.get(url)
    #base_url = get_base_url(r.text, r.url)
    metadata = extruct.extract(text, # r.text, base_url=base_url 
                               uniform=True,
                               syntaxes=['microdata'], return_html_node=True)
    #pp.pprint(metadata)                                         
    return metadata
metadata = extract_metadata(e)  
pp.pprint(metadata)  
def uses_metadata_type(metadata, metadata_type):
    if (metadata_type in metadata.keys()) and (len(metadata[metadata_type]) > 0):
        print(True)
        return True
    else:
        print(False)
        return False 

def key_exists(dict, key):

    if not any(item['@type'] == key for item in dict):
        print(False)
        return False
    else:
        print(True)
        return True 
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



