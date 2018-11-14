import os

import toolkit_file

DB_FILE = 'xcs_data.db'

XCS_LIB = r'C:\Users\chdu\Desktop\Portal\Other\xshell_theme_preview\Xshell-ColorScheme-lib'
TABLE_NAME = 'xcs_profile'
TABLE_COLONM = '''
NAME
BACKGROUND
BLACK
BLACK(BOLD)
BLUE
BLUE(BOLD)
CYAN
CYAN(BOLD)
GREEN
GREEN(BOLD)
MAGENTA
MAGENTA(BOLD)
RED
RED(BOLD)
TEXT
TEXT(BOLD)
WHITE
WHITE(BOLD)
YELLOW
YELLOW(BOLD)
FILE_PATH
'''

# xshell_theme_preview
FONT_PATH = 'fonts'
# FONT = FONT_PATH + os.sep + 'fixedsys.ttf'
FONT = FONT_PATH + os.sep + 'DejaVuSansMono.ttf'

PREVIEW_PATH = 'preview' + os.sep
TABLE_COLONM_ORDER_LIST = [ i for i in TABLE_COLONM.split('\n') if i ]

toolkit_file.create_folder(FONT_PATH)
toolkit_file.create_folder(PREVIEW_PATH)