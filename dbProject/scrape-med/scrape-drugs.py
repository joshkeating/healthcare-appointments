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




get_medication_names()
