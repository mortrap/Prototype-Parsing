import sys
import os

from warcio.archiveiterator import ArchiveIterator
#urllib3.disable_warnings()
half_exchanges = {}
print (os.environ['WARC_FILE'])
with open(os.environ['WARC_FILE'], 'rb') as stream:
    for record in ArchiveIterator(stream):
        if record.rec_type == 'response':
            # print(record.rec_headers.get_header('WARC-Target-URI'))
            if record.http_headers.get_header('Content-Type').startswith('text/html'):
                id = record.rec_headers.get_header('WARC-Target-URI')
                #html_text = requests.get(id).text
                print (f"payload_length: {record.payload_length}");
                html_text=record.content_stream()
                # html_text is ChunkedDataReader | BufferedReader
                # let's read html_text into a string
                html_str = html_text.read().decode('utf-8', 'ignore')

                print (f"html_text len: {len(html_str)}")
                #soup = BeautifulSoup(html_text, 'html.parser')
                #print((soup.get_text()))

            if id:
                if id not in half_exchanges:
                    half_exchanges[id] = record
                else:
                    if record.rec_type == 'request':
                        req = record
                        res = half_exchanges[id]
                    else:
                        req = half_exchanges[id]
                        res = record
                    # Remove temporary record that is paired and yield the pair
                    del half_exchanges[id]
print(half_exchanges.keys())

#
