import re
from bs4 import BeautifulSoup


def get_scheme(value):
    str_val = value
    words = str_val.split("piintu-", 1)[1]
    sc_words = str_val.split("sc-", 1)[1]
    str_data_div = ''
    str_data_i = ''
    arr = []
    # test case a on progress :D
    # test case b
    for item in words:
        if item == '>' or item == " ":
            break
        str_data_div += item
    for items in sc_words:
        if items == '>' or items == " ":
            break
        str_data_i += items
    if str_data_i is None:
        arr.append(str_data_div)
    else:
        arr.extend([str_data_div, str_data_i])

    return arr


input_tag_html = input('Input your tag HTML here: ')
print(get_scheme(input_tag_html))
