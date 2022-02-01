import re
result = re.match(r'fe', 'offers')
# Искомая подстрока найдена. Чтобы вывести её содержимое, применим метод group() 
# (мы используем «r» перед строкой шаблона, чтобы показать, что это «сырая» строка в Python):
print (result)
print (result.group(0))
# import pprint
# pp = pprint.PrettyPrinter(indent=0)
# # Needs urllib3 2, https://github.com/urllib3/urllib3#installing
# import urllib3





# #import extruct
# from fastwarc.stream_io import *
# from fastwarc.warc import ArchiveIterator, WarcRecordType, WarcRecord, is_http
# from fastwarc.stream_io import BufferedReader
# # fastwarc: test the streaming parsing

# url ='https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2021-10/segments/1614178347293.1/warc/CC-MAIN-20210224165708-20210224195708-00004.warc.gz'
# #req=requests.get(url, stream = True)
# # use urllib3 to open an URL stream
# req = urllib3.request("GET", url, preload_content=False)
# #print(req.content)
# #head = WarcHeaderMap()

# def read_cl(record , cl):
#      return record.reader.read(cl)
# is_eof = False
# records = []
# with open('test', 'w') as file:

#      for record in ArchiveIterator(req, record_types=WarcRecordType.response, func_filter=lambda r: r.headers.get('WARC-Identified-Payload-Type') == 'text/html', max_content_length = 512000):
#           print('Payload digest OK:', record.verify_payload_digest())
#           if record.content_length>0:
#               file.write(record.reader.read(record.content_length).decode('utf-8'))
#           pp.pprint(record.content_length)
#           file.close()
#           break