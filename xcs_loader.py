import pandas as pd
import sqlite3

import toolkit_file
import toolkit_config
import config

exampleFile = 'example/Chalk.xcs'


def read_xcs(xcsFile):
    '''Read xcs color scheme, return in dict'''
    xcs_profile = toolkit_config.read_config_general(xcsFile)
    profile = xcs_profile[xcs_profile['Names']['NAME0']]
    profile['NAME'] = xcs_profile['Names']['NAME0']
    return profile


def load_xcs(profileList):
    '''Load xcs into database'''
    tableName = config.TABLE_NAME
    profileDataframe = pd.DataFrame(
        profileList, columns=config.TABLE_COLONM_ORDER_LIST)
    # profileDataframe = []
    for i in profileDataframe.columns:
        profileDataframe.rename(
            columns={i: i.replace('(BOLD)', '_BOLD')}, inplace=True)
    # print(profileDataframe)
    conn = sqlite3.connect(config.DB_FILE)
    profileDataframe.to_sql(name=tableName, if_exists='replace',
                            con=conn, index=True)


if __name__ == '__main__':
    xcsList = [ i for i in toolkit_file.get_file_list(config.XCS_LIB) if i.lower().endswith('.xcs')]
    profileList = list(map(read_xcs, xcsList))
    load_xcs(profileList)
