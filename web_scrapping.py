import requests
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
import re
# Site URL
url="https://nec.gov.np/applicant/cat/1?fbclid=IwAR3j_qNtnjJ31L12_SauLNjgz4FJjjZILCnvXkNaVxiPSv3YYnsU8na6ddE"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse HTML code for the entire site
soup = BeautifulSoup(html_content, "lxml")
gdp = soup.find_all("table", attrs={"class": "table"})
table1 = gdp[0]
# the head will form our column names
body = table1.find_all("tr")
# Head values (Column names) are the first items of the body list
head = body[0] # 0th item is the header row
body_rows = body[1:] # All other items becomes the rest of the rows

# Lets now iterate through the head HTML code and make list of clean headings

# Declare empty list to keep Columns names
headings = []
sub_heading=[]
all_rows1=[]
sub_headers=['Full Name', 'Permanent Address', 'Gender', 'Category', 'Qualification', 'University/Country', 'Passout Year', 'Reg. No']
for item in head.find_all("th"): # loop through all th elements
    # convert the th elements to text and strip "\n"
    item = (item.text).rstrip("\n")
    headings.append(item)
    for link in soup.find_all("a"):
        if link.get("title")!=None:
            url_view=link.get("href")
            try:
                view_content = requests.get(url_view).text
                soup_view = BeautifulSoup(view_content, "lxml")
                info_view = soup_view.find_all("table", attrs={"class": "table"})
                sub_table=info_view[0]
                sub_body = sub_table.find_all("tbody")
                # Head values (Column names) are the first items of the body list
                for sub_head in sub_body:
                    rows=[]
                    for sub_item in sub_head.find_all("td"):
                        sub_item = (sub_item.text).rstrip("\n")
                        rows.append(sub_item)
                if rows not in all_rows1:
                    all_rows1.append(rows)

            except:
                continue

print(all_rows1)
print(len(all_rows1))
print("ok")

df1 = pd.DataFrame(data=all_rows1,columns=sub_headers)
df1.to_excel (r'details.xlsx', index = False, header=True)


    # append the clean column name to headings

# print(df1)


all_rows = [] # will be a list for list for all rows
for row_num in range(len(body_rows)): # A row at a time
    row = [] # this will old entries for one row
    for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
        # row_item.text removes the tags from the entries
        # the following regex is to remove \xa0 and \n and comma from row_item.text
        # xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
        aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
        #append aa to row - note one row entry is being appended
        row.append(aa)
    # append one row to all_rows
    all_rows.append(row)
print(all_rows)
df = pd.DataFrame(data=all_rows,columns=headings)
df.to_excel (r'general_info.xlsx', index = False, header=True)
