import pandas as pd
import extruct
import requests
from w3lib.html import get_base_url
from urllib.parse import urlparse


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
metadata_box = extract_metadata('https://market.yandex.ru/catalog--muzhskaia-sportivnaia-odezhda/22489037/list?rs=eJwlzs1SglAYxvGpXSxdeAO1bYbz8Z6PJSKghwFGUMqVmSWZxhnpiOQtdNNxbP-b__Pg31v14AxVB_zI2zh4U2vjNpstRh8_54GDKDDGqZDMqsm2zOrjJZpL7xmpSE91DPPKKskkUMqFuneGfnYyKMhWTbiWqqByf4iW42pwJwRGgiJBbOrTH6e7-PtUeclu09Z1Z1KYzPoUg35OuEha9eVq7T3JQ2MaUqBzGoReU__fElyQ3lnVmRHwJeQLpUeLffYOWZ5HV2Vj4HKwihQlp48rStpkNk1CVL7WPr8qISl2JccvN39pRkcq&onstock=0&local-offers-first=0')
print(pd.Series(metadata_box))
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
Product = get_dictionary_by_key_value(metadata_box, "@type", "Product")


df = pd.DataFrame(Product)
print(df)
        
#
