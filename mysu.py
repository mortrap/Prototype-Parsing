import pprint
pp = pprint.PrettyPrinter(indent=0)
import extruct
from e import e
from exhtml import html


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



