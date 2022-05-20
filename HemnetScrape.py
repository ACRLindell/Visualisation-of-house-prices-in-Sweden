import requests
import csv
import numpy as np
from bs4 import BeautifulSoup

page = requests.get("https://www.hemnet.se/salda/bostader?housing_form_groups%5B%5D=apartments")

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())