import re
import requests as r
import json
import pandas as pd
from key import *

endpoint = 'https://grcdocs-search.search.windows.net'
headers = {'Content-Type': 'application/json',
           'api-key': key}

api_version = 'docs?api-version=2019-05-06'
index = '/indexes/demoindex/'
search_term = "&search=grc%20application" + '&$top=' + str(10)
conn_str =  endpoint + index + api_version + search_term

print('Making GET request ...')

data_json = r.get(conn_str, headers=headers).json()

#https://stackoverflow.com/questions/25735644/python-regex-for-splitting-text-into-sentences-sentence-tokenizing/25735848
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', data_json['value'][0]['content'])
sentence_list = [" ".join(each.replace('\r', '').replace('\n', '').strip().split()) for each in sentences]

df1 =  pd.DataFrame({'content': sentence_list})

df1['document_no'] = 100
df1['sentence_no'] = df1.index

df = df1[['document_no', 'sentence_no', 'content']]

print('Saving CSV file ...')

df.to_csv('grc_text_001.csv', index=False)

print('Saving JSON ...')

with open('grc_doc_001.json', 'w') as file:
    json.dump(data_json, file)

print('Done...')