from PIL import Image, ImageColor, ImageFont, ImageDraw

import toolkit_sqlite
import config


def query_result(fileName):
    with toolkit_sqlite.SqliteDB(config.DB_FILE) as db:
        query_sql = '''SELECT * FROM {tablename} WHERE NAME='{name}';'''.format(
            tablename=config.TABLE_NAME, name=fileName)
        # result = db.query(query_sql)
        db_cursor = db.conn.cursor()
        db_cursor.execute(query_sql)
        row = db_cursor.fetchone()
        rowDict = dict(zip([c[0] for c in db_cursor.description], row))
    for i in rowDict.keys():
        if i != 'NAME' and i != 'index' and i != 'FILE_PATH':
            rowDict[i] = '#' + str(rowDict[i])
    return rowDict


def preview_gen(index, NAME, BACKGROUND, BLACK, BLACK_BOLD, BLUE, BLUE_BOLD, CYAN, CYAN_BOLD, GREEN, GREEN_BOLD, MAGENTA, MAGENTA_BOLD, RED, RED_BOLD, TEXT, TEXT_BOLD, WHITE, WHITE_BOLD, YELLOW, YELLOW_BOLD):
    img = Image.new('RGB', (1090, 380), ImageColor.getrgb(BACKGROUND))
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype(config.FONT, 15)
    # draw.text((x, y),"Sample Text",(r,g,b))
    # text = open('sample.txt').read()

    cursor_loc = [0, 0]
    # generate demo

    filelist = [['-rwxr-xr-x  1 pi   pi    370 Feb 17  2018 ','sys_backup.sh'],
['drwxr-xr-x  2 pi   pi   4096 Feb 17  2018 ','sys_config'],
['drwxr-xr-x  2 pi   pi   4096 Feb 17  2018 ','sys_mng_script'],
['-rwxr-xr-x  1 pi   pi    226 Feb 17  2018 ','temp.py'],
['drwxr-xr-x  6 pi   pi   4096 Sep 10 23:32 ','test'],
['drwxr-xr-x  3 pi   pi   4096 Jun 24 10:38 ','text_process'],
['drwxr-xr-x  3 pi   pi   4096 Nov 12 00:30 ','venus_scripts'],
['-rwxr-xr-x  1 pi   pi     67 Feb 17  2018 ','vnc_ssh_rev.sh'],
['-rwxr-xr-x  1 pi   pi   1719 Feb 17  2018 ','vnstat_DB_chk.sh'],
['-rwxr-xr-x  1 pi   pi   1429 Feb 17  2018 ','vnstat_DB_chk.sh.bak'],
['drwxr-xr-x  4 root root 4096 Jun 18 08:23 ','vps'],
['-rwxr-xr-x  1 pi   pi   2195 Feb 17  2018 ','wake_on_lan.sh'],
['drwxr-xr-x  3 pi   pi   4096 Nov 13 00:30 ','www_backup'],
['drwxr-xr-x  3 pi   pi   4096 Feb 25  2018 ','xiaoqiang_network_mon'],]
    
    for prop, fn in filelist:
        propcolor = TEXT
        if prop.startswith('d'):
            fncolor=GREEN_BOLD
        else:
            fncolor=BLUE_BOLD
        draw_text(img, cursor_loc, propcolor, prop, font)
        cursor_rightshift(img, cursor_loc, prop, font)
        draw_text(img, cursor_loc, fncolor, fn, font)
        cursor_newline(img, cursor_loc, prop, font)

    head = '[ 23:58 - 192.168.31.179  ]'
    headcolor = MAGENTA_BOLD
    draw_text(img, cursor_loc, headcolor, head, font)
    cursor_newline(img, cursor_loc, prop, font)

    userinfo = 'pi@Mercury '
    userinfocolor = GREEN_BOLD
    pathinfo = '~/run $ '
    pathinfocolor = BLUE_BOLD
    draw_text(img, cursor_loc, userinfocolor, userinfo, font)
    cursor_rightshift(img, cursor_loc, userinfo, font)
    draw_text(img, cursor_loc, pathinfocolor, pathinfo, font)

    img.save(config.PREVIEW_PATH + str(index) + '_' + NAME + ".png", "PNG")
    # img.save(NAME + ".png", "PNG")


def draw_text(img, cursor_loc, color, text, font):
    draw = ImageDraw.Draw(img)
    draw.text(cursor_loc, text, color, font=font)
    return img

def cursor_newline(img, cursor_loc, text, font):
    '''shift the cursor to the next line'''
    draw = ImageDraw.Draw(img)
    cursor_loc[1] += draw.textsize(text, font=font)[1]
    cursor_loc[0] = 0
    return cursor_loc

def cursor_rightshift(img, cursor_loc, text, font):
    '''shift the cursor to the end of the text'''
    draw = ImageDraw.Draw(img)
    cursor_loc[0] += draw.textsize(text, font=font)[0]
    return cursor_loc

if __name__ == '__main__':
    fileName = 'Belafonte Day'
    # result = query_result(fileName)
    # preview_gen(**result)

    with toolkit_sqlite.SqliteDB(config.DB_FILE) as db:
        query_sql = '''SELECT NAME FROM {tablename};'''.format(tablename=config.TABLE_NAME)
        nameList = [i[0] for i in db.query(query_sql)]
    for i in nameList:
        result = query_result(i)
        preview_gen(**result)
