# -*- encoding: utf-8 -*-

s_units = ('km km² km³ m m² m³ dm dm² dm³ cm cm² cm³ mm mm² mm³ ha µm nm yd in ft '
           'kg g mg µg t lb oz m/s km/h kmh mph hPa Pa mbar mb MB kb KB gb GB tb '
           'TB T G M K % км км² км³ м м² м³ дм дм² дм³ см см² см³ мм мм² мм³ нм '
           'кг г мг м/с км/ч кПа Па мбар Кб КБ кб Мб МБ мб Гб ГБ гб Тб ТБ тб'
           'كم كم² كم³ م م² م³ سم سم² سم³ مم مم² مم³ كم غرام جرام جم كغ ملغ كوب اكواب')

s_currency = r'\$ £ € ¥ ฿ US\$ C\$ A\$ ₽ ﷼'

s_punct = r'… …… , : ; \! \? ¿ ؟ ¡ \( \) \[ \] \{ \} < > _ # \* & 。 ？ ！ ， 、 ； ： ～ · । ، ؛ ٪'

s_quotes = r'\' \'\' " ” “ `` ` ‘ ´ ‘‘ ’’ ‚ , „ » « 「 」 『 』 （ ） 〔 〕 【 】 《 》 〈 〉'

s_hyphens = r'- – — -- --- —— ~'

# https://www.compart.com/en/unicode/category/So
r_other_symbols = r'[\p{So}]'

r_emoji = r'\\[[0-9a-zA-Z\\u4e00-\\u9fa5]+\\]'

# 正整数
r_positive_int = r'^[0-9]*[1-9][0-9]*$'
# 负整数
r_negtive_int = r'^ -[0 - 9] * [1 - 9][0 - 9] *$'
# 正浮点数
r_positive_float = r'^ (([0 - 9] +\.[0 - 9] * [1 - 9][0 - 9] *) | ([0 - 9] * [1 - 9][0 - 9] *\.[0 - 9] +) | ([0 - 9] * [1 - 9][0 - 9] *))$'
# 负浮点数
r_negtive_float = r'^ (-(([0 - 9] +\.[0 - 9] * [1 - 9][0 - 9] *) | ([0 - 9] * [1 - 9][0 - 9] *\.[0 - 9] +) | ([0 - 9] * [1 - 9][0 - 9] *)))$'
# 浮点数
r_float = r'^ (-?\d +)(\.\d +)?$'
# email地址
r_email = r'^ [\w -]+(\.[\w -]+) * @ [\w -]+(\.[\w -]+)+$'
# url地址
r_url = '^ [a - zA - z] +: // (\w + (-\w +) * )(\.(\w + (-\w +) * ))*(\?\S *)?$'
# 年 / 月 / 日（年 - 月 - 日、年.月.日）
r_date = r'^ (19 | 20)\d\d[- /.](0[1 - 9] | 1[012])[- /.](0[1 - 9] | [12][0 - 9] | 3[01])$'
# 匹配中文字符
r_chinese_char =r'[\u4e00 -\u9fa5]'
# 匹配IP地址
r_ip = r'((2[0 - 4]\d | 25[0 - 5] | [01]?\d\d?)\.){3}(2[0 - 4]\d | 25[0 - 5] | [01]?\d\d?)'
# 匹配HTML标记的正则表达式
r_html = r'< (\S *?)[ ^ >] * >.* ? | <.* ? / >'
#sql语句
r_sql = r'^ (select | drop | delete | create | update | insert). *$'
