import pandas as pd
import json
import numpy as np

df_input_path = 'https://raw.githubusercontent.com/grantaguinaldo/grc/master/misc/grc_2019_file_index.csv'
json_input_path = 'grc_doc_001.json'
json_output_path = 'grc_doc_002.json'

df = pd.read_csv(df_input_path)

with open(json_input_path) as f:
    data = json.load(f)
    blobUrlRaw = [each['metadata_storage_path'] for each in data['value']]
    print(blobUrlRaw[0])

blobUrlRaw
blobUrlTrim = [each.split('/')[-1] for each in blobUrlRaw]
blobUrlClean = [' '.join(each.split('%20')) for each in blobUrlTrim]

df_new = df[df['file_name'].isin(blobUrlClean)]
df_sorted = df_new.sort_values('file_name', axis=0)

blobUrlRaw.sort()

df_sorted['blob_url'] = blobUrlRaw

nameDict = dict(zip(df_sorted['blob_url'], df_sorted['file_url']))

for each in data['value']:
    if each['metadata_storage_path'] in nameDict.keys():
        each['metadata_storage_path'] = nameDict[each['metadata_storage_path']]
        print(each['metadata_storage_path'])
    else:
        print('Error at Index: {}'.format(each))

with open(json_output_path, 'w') as f:
    json.dump(data, f)