import requests
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
import re

# Site URL
url = "https://nec.gov.np/applicant/cat/26"
html_content = requests.get(url).text

# Parse HTML code for the entire site
soup = BeautifulSoup(html_content, "lxml")
table_initial = soup.find_all("table", attrs={"class": "table"})
table1 = table_initial[0]
# the head will form our column names
body = table1.find_all("tr")
head = body[0]  # 0th item is the header row
body_rows = body[1:]  # All other items becomes the rest of the rows
headings = []
sub_heading = []
all_rows1 = []
sub_headers = [
    "Full Name",
    "Permanent Address",
    "Gender",
    "Category",
    "Qualification",
    "University/Country",
    "Passout Year",
    "Reg. No",
]
for item in head.find_all("th"):  # loop through all th elements
    item = (item.text).rstrip("\n")
    headings.append(item)
    for link in soup.find_all("a"):
        if link.get("title") != None:
            url_view = link.get("href")
            try:
                view_content = requests.get(url_view).text
                soup_view = BeautifulSoup(view_content, "lxml")
                info_view = soup_view.find_all("table", attrs={"class": "table"})
                sub_table = info_view[0]
                sub_body = sub_table.find_all("tbody")
                # Head values (Column names) are the first items of the body list
                for sub_head in sub_body:
                    rows = []
                    for sub_item in sub_head.find_all("td"):
                        sub_item = (sub_item.text).rstrip("\n")
                        rows.append(sub_item)
                if rows not in all_rows1:
                    all_rows1.append(rows)

            except:
                continue

df1 = pd.DataFrame(data=all_rows1, columns=sub_headers)
df1.to_excel(r"output/details.xlsx", index=False, header=True)
all_rows = []  # will be a list for list for all rows
for row_num in range(len(body_rows)):  # A row at a time
    row = []
    for row_item in body_rows[row_num].find_all("td"):
        aa = re.sub("(\xa0)|(\n)|,", "", row_item.text)
        row.append(aa)
    all_rows.append(row)
df = pd.DataFrame(data=all_rows, columns=headings)
df.to_excel(r"output/general_info.xlsx", index=False, header=True)
