import pprint
pp = pprint.PrettyPrinter(indent=0)
import pandas as pd
import extruct
import requests
from w3lib.html import get_base_url
from urllib.parse import urlparse

sites = []
def extract_metadata(url):
    """Extract all metadata present in the page and return a dictionary of metadata lists. 
    
    Args:
        url (string): URL of page from which to extract metadata. 
    
    Returns: 
        metadata (dict): Dictionary of json-ld, microdata, and opengraph lists. 
        Each of the lists present within the dictionary contains multiple dictionaries.
    """
    
    r = requests.get(url)
    base_url = get_base_url(r.text, r.url)
    metadata = extruct.extract(r.text, 
                               base_url=base_url,
                               uniform=True,
                               syntaxes=['json-ld',
                                         'microdata',                                
                                         'opengraph'])
    return metadata
metadata= extract_metadata('https://www.notik.ru/goods/notebooks-lenovo-ideapad-3-14itl05-blue-83247.htm')
metadata
def uses_metadata_type(metadata, metadata_type):
    if (metadata_type in metadata.keys()) and (len(metadata[metadata_type]) > 0):
        return True
    else:
        return False

def get_dictionary_by_key_value(dictionary, target_key, target_value):
    """Return a dictionary that contains a target key value pair. 
    
    Args:
        dictionary: Metadata dictionary containing lists of other dictionaries.
        target_key: Target key to search for within a dictionary inside a list. 
        target_value: Target value to search for within a dictionary inside a list. 
    
    Returns:
        target_dictionary: Target dictionary that contains target key value pair. 
    """
    
    for key in dictionary:
        if len(dictionary[key]) > 0:
            for item in dictionary[key]:
                if item[target_key] == target_value:
                    return item

def key_exists(dict, key):

    if not any(item['@type'] == key for item in dict):
        print(False)
        return False
    else:
        print (True)
        return True                      
Product = get_dictionary_by_key_value(metadata, "@type", "Product")
#pp.pprint(pd.DataFrame(Product, columns=['name', 'offers'], index = ['price', 'priceCurrency', 'url']))
#pp.pprint(pd.DataFrame(Product)) 
# if key_exists(metadata['microdata'], 'Product'): 
#     pp.pprint (pd.DataFrame(metadata['microdata']))
# if key_exists(metadata['json-ld'], 'Product'):
#     print (pd.DataFrame(metadata['json-ld']))
# if key_exists(metadata['opengraph'], 'Product'):
#     print(pd.DataFrame(metadata['opengraph']))
#print(pd.DataFrame(metadata))
#print(pd.Series(metadata['opengraph']))
#print(pd.DataFrame(metadata['json-ld']))
print(pd.DataFrame(metadata['microdata']))
# print(pd.DataFrame(metadata['opengraph']))
    
    # print(pd.DataFrame(metadata['json-ld']['@context'].keys()))

        
#
