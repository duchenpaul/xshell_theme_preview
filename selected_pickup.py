import shutil

import toolkit_sqlite
import toolkit_file

import config

target_folder = 'selected'
toolkit_file.create_folder(target_folder)

query_sql = '''SELECT a.name,
                       a.file_path
                FROM xcs_profile a
                JOIN xcs_fav b ON a.`index` = b.`index`
                WHERE is_fav=1
                ORDER BY a.name;'''

with toolkit_sqlite.SqliteDB(config.DB_FILE) as db:
    result = db.query(query_sql)
    # print(result)
    selected_xcsList = [i[1] for i in result]

for i in selected_xcsList:
    shutil.copy(i, target_folder)