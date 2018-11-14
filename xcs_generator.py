import pandas as pd
import configparser
import sqlite3

import config


def value_cleanse(profileDict):
    '''Remove extra keys, restore the original key name'''
    for x in ['NAME', 'FILE_PATH', 'index']:
        if profileDict.get(x):
            profileDict.pop(x)
    # for key in i.keys():
    #     pass
    return profileDict


xcs = configparser.RawConfigParser()

query_sql = '''SELECT a.*
                FROM xcs_profile a
                JOIN xcs_fav b ON a.`index` = b.`index`
                WHERE is_fav=1
                ORDER BY a.name;'''

con = sqlite3.connect(config.DB_FILE)
df = pd.read_sql_query(query_sql, con=con)

xcs_profile_list = df.to_dict(orient='records')


for i in xcs_profile_list:
    profileName = i['NAME']
    xcs.add_section(profileName)
    for key in value_cleanse(i).keys():
        xcs.set(profileName, key.replace('_BOLD', '(BOLD)'), i[key])


# # Generate meta info in xcs
xcs.add_section('Names')
count = 0
for idx, name in enumerate(df['NAME']):
    # orderedList.append('name{}={}'.format(idx, name))
    xcs.set('Names', 'name' + str(idx), name)
    count += 1
xcs.set('Names', 'count', count)


# Writing our configuration file to 'example.cfg'
with open('export_selected.xcs', 'w') as xcsFile:
    xcs.write(xcsFile, space_around_delimiters=False)
