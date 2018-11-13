'''
Retrun the config in dict
'''

import configparser, os.path

config_file = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'config.ini'


def read_config_general(configFile=config_file):
    try:
        print('Read config file: ' + configFile)
        configRead = configparser.ConfigParser()
        configRead.read(configFile)

        config = {}
        for sectionName in configRead.sections():
            config[sectionName] = {}
            options = [i.upper() for i in configRead.options(sectionName)]
            for j in options:
                config[sectionName][j] = configRead[sectionName][j]

    except Exception as e:
        print("Error read config file, check config.ini")
        print(e)
        raise
    return config


def read_config_mail(configFile=config_file):
    try:
        print('Read config file: ' + configFile )
        configRead = configparser.ConfigParser()
        configRead.read(configFile)

        sectionName = 'mail'
        options = [ i.upper() for i in configRead.options(sectionName) ]
        config = {}
        for j in options:
            config[j] = configRead[sectionName][j]

    except Exception as e:
        print("Error read config file, check config.ini")
        print(e)
        raise
    return config


def read_config_mysql(configFile=config_file):
    try:
        print('Read config file: ' + configFile )
        configRead = configparser.ConfigParser()
        configRead.read(configFile)
        config = {
            'host': configRead['database']['host'],
            'port': int(configRead['database']['port']),
            'user': configRead['database']['user'],
            'passwd': configRead['database']['passwd'],
            'db': configRead['database']['db'],
            'charset': 'utf8'
        }
    except Exception as e:
        print("Error read config file, check config.ini")
        print(e)
        raise
    return config


if __name__ == '__main__':
    config = read_config_general('example/Chalk.xcs')
    print(config[config['Names']['NAME0']])