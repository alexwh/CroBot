#
# regex.py
# Contains all of the regex strings to allow the main scripts to be less cluttered
#

id_parse = r'/(\d+)sort.js'
jacket = r'(/\d+/jacket/\d+[em]....)'


## Regex to be used for parse_chart
title = r'(\d+)\s+(.+)' # Group 1 is sdvx.in's id for the song; Group 2 is the song name
artist = r'ARTIST\d*.*2>.*/\s(.*)<'
sort_exclude = r'SORT\d*' # Used to filter out the sort line which the dif regex catches

dif_general = r'LV\d+[NAEIGHM]'
dif_nov = r'LV\d+N'
dif_adv = r'LV\d+A'
dif_exh = r'LV\d+E'
dif_max = r'LV\d+[IGHM]'
dif_link = r'/\d.*htm'
dif_level = r'(\d+)</div>'

japanese = r'[\u3040-\u309F]|[\u30A0-\u30FF]|[\uFF00-\uFFEF]|[\u4E00-\u9FAF]|[\u2605-\u2606]|[\u2190-\u2195]|\u203B' # https://gist.github.com/sym3tri/980083 (slight modifications)

video_play = r'MV\d+[EIGHM]'
video_music = r'SD\d+[FO]'
video_nofx = r'SD\d+F'
video_og  = r'SD\d+O'
video_link = r'href=(\S+youtube\S+)'