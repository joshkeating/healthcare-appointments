from bs4 import BeautifulSoup as bs
from bs4 import Tag
import requests
import csv
import re

# name
# instructions
# recommended_dose


def get_medication_names():
    '''get top 40 drugs from drugs.com'''

    base_url = 'https://www.drugs.com/drug_information.html'
    target_page = requests.get(base_url)
    html = bs(target_page.text, "html.parser")
    container = html.find("ul", class_="column-span column-span-4").contents

    drug_list = []

    for elem in container:
        if type(elem) == Tag:
            drug_list.append(elem.text)

    return drug_list


def get_info(meds):
    '''get info for meds'''

    desc_list = []

    for med in meds:

        url = 'https://www.drugs.com/' + med + '.html'

        target_page = requests.get(url)
        html = bs(target_page.text, "html.parser")

        first_five = html.find_all("p", limit=5)
        target_desc = first_five[2:]

        cur_desc = ""

        for elem in target_desc:
            cur_desc += elem.text + " "

        desc_list.append(cur_desc)

    return desc_list


def get_dosage(meds):
    '''TODO'''

    dosage_list = []

    for med in meds:

        url = 'https://www.drugs.com/dosage/'  + med + '.html'

        target_page = requests.get(url)
        html = bs(target_page.text, "html.parser")

        first_two = html.find_all("p", limit=2)
        target = first_two[1:]
        cur_dosage = target[0].text

        dosage_list.append(cur_dosage)

    return dosage_list


def main():

    # scrape all needed info
    med_list = get_medication_names()
    desc_list = get_info(med_list)
    dosage_list = get_dosage(med_list)

    # create tuples from lists
    rows = zip(med_list, desc_list, dosage_list)

    # write to file
    with open('./medications.csv', "w") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

    pass


if __name__ == "__main__":
    main()
