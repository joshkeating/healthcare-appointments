from bs4 import BeautifulSoup as bs
from bs4 import Tag
import requests
import csv
import re

# name
# instructions
# recommended_dose


def get_medication_names():

    base_url = 'https://www.drugs.com/drug_information.html'
    target_page = requests.get(base_url)
    html = bs(target_page.text, "html.parser")
    container = html.find("ul", class_="column-span column-span-4").contents

    drug_list = []

    for elem in container:
        if type(elem) == Tag:
            drug_list.append(elem.text)

    return drug_list


def get_info():
    '''get info for meds'''

    # url = 'https://www.drugs.com/' + test + '.html'

    url = 'https://www.drugs.com/meloxicam.html'

    target_page = requests.get(url)
    html = bs(target_page.text, "html.parser")

    first_five = html.find_all("p", limit=5)
    target_desc = first_five[2:]

    cur_desc = ""

    for elem in target_desc:
        cur_desc += elem.text + " "

    print(cur_desc)

    pass


get_info()
