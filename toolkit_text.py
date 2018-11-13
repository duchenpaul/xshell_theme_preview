import re
import base64
import csv
import pandas as pd

#######################################################################


def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += '=' * (4 - missing_padding)
    return base64.urlsafe_b64decode(data).decode('utf-8')


def encode_base64(data):
    """
    base64 encode
    """
    return base64.urlsafe_b64encode(data.encode()).decode('utf-8')

########################################################################
# Regex


def regex_find(pattern, text):
    '''
    return list
    '''
    match_return = re.compile(pattern, re.IGNORECASE).findall(text)
    return match_return


def regex_replace(pattern, string, text):
    '''
    Replace pattern with string in text
    '''
    return re.sub(pattern, string, text, flags=re.IGNORECASE)


def regex_replace_file(FILENAME, pattern, string, exception=None):
    '''
    Replace the regex pattern with string of a file, except exceptions
    '''
    with open(FILENAME, 'r') as f:
        text = f.read()

    if exception and re.compile(exception, re.IGNORECASE).findall(text):
        print(" - Skip " + exception)
        return
    with open(FILENAME, 'w') as f:
        f.write(re.sub(pattern, string, text, flags=re.IGNORECASE))

########################################################################


########################################################################
# csv <-> list

def csv2list(FILE):
    '''Import csv to list'''
    csv_list = []
    with open(FILE, encoding='utf-8') as csvfile:
        # Detect header, remove if exists
        has_header = csv.Sniffer().has_header(csvfile.read(1024))
        csvfile.seek(0)  # Rewind.
        reader = csv.reader(csvfile)
        if has_header:
            # print("Header detected, skip.")
            next(reader)  # Skip header row
        return list(csv.reader(csvfile, delimiter=','))


def list2csv(list, FILE):
    listHeader = ['col1', 'col2']
    with open(FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        f.write(', '.join(listHeader))
        f.write('\n')
        writer.writerows(list)

########################################################################


########################################################################
# csv <-> dict

def dict2csv(dictList, fileName):
    '''
    Input: dictList
    Output: csv file
    '''
    keys = dictList[0].keys()
    with open(fileName, 'w', encoding='utf-8', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dictList)


def csv2dict(csv_file):
    '''
    Iutput: csv file
    Onput: dictList
    '''
    dataFrame = pd.read_csv(csv_file, encoding='utf-8', header=0)
    # print(data.to_dict())
    dict_list = []
    for i in dataFrame.index:
        data_dict = {}
        for column in dataFrame.columns:
            data_dict[column] = dataFrame[column][i]
        dict_list.append(data_dict)
    return dict_list

########################################################################


def csv2table(fileName, table):
    pass


def fwf2dict(FILE, widthList):
    '''Transform fixed width file into dict'''

    # Specify header = 0 to set the first line as header
    # Specify "names = [col1, col2, ...]" to set the header from [col1, col2, ...]
    dataFrame = pd.read_fwf(FILE, header=None, widths=widthList, )
    print(dataFrame)
    return dataFrame.to_dict()


########################################################################


def convert_to_Byte(value):
    '''Convert KB, MB, GB into Byte'''
    UNIT_SET = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    for i, c in enumerate(value):
        if c not in '0123456789-.':
            break
    number = float(value[:i])
    unit = value[i:]
    inByte = number * 1024 ** UNIT_SET.index(unit)
    return int(inByte)


def convert_Bytes(size):
    '''Convert Byte into KB, MB, GB'''
    power = 2**10
    n = 0
    Dic_powerN = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return '{}{}'.format(round(size, 2), Dic_powerN[n])


if __name__ == '__main__':
    x = fwf2dict('test.txt', [8, 16, 16, 12, 14, 16, 7, ])
    print(x)

    # _ = csv2dict('FL_insurance_sample.csv')
    # print(_)
#  'Account', 'LastName', 'FirstName', 'Balance', 'CreditLimit', 'AccountCreated', 'Rating',
