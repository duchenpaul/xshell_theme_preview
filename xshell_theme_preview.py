from PIL import Image, ImageColor, ImageFont, ImageDraw

import toolkit_sqlite
import config


def query_result():
    with toolkit_sqlite.SqliteDB(config.DB_FILE) as db:
        query_sql = '''SELECT * FROM {tablename} WHERE NAME='{name}';'''.format(
            tablename=config.TABLE_NAME, name='Solarized Dark')
        # result = db.query(query_sql)
        db_cursor = db.conn.cursor()
        db_cursor.execute(query_sql)
        row = db_cursor.fetchone()
        rowDict = dict(zip([c[0] for c in db_cursor.description], row))
    for i in rowDict.keys():
        if i != 'NAME':
            rowDict[i] = '#' + rowDict[i]
    return rowDict


def preview_gen(NAME, BACKGROUND, BLACK, BLACK_BOLD, BLUE, BLUE_BOLD, CYAN, CYAN_BOLD, GREEN, GREEN_BOLD, MAGENTA, MAGENTA_BOLD, RED, RED_BOLD, TEXT, TEXT_BOLD, WHITE, WHITE_BOLD, YELLOW, YELLOW_BOLD):
    color = '#d2d8d9'
    img = Image.new('RGB', (1090, 380), ImageColor.getrgb(BACKGROUND))
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype(config.FONT, 20)
    # draw.text((x, y),"Sample Text",(r,g,b))
    text = open('sample.txt').read()
    draw.text((0, 0), text, (255, 255, 255), font=font)
    img.save("image.png", "PNG")


if __name__ == '__main__':
    result = query_result()
    preview_gen(**result)
