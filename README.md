
# Web Scraper for NEC Applicant Information

This Python script is designed to scrape applicant information from the Nepal Engineering Council(NEC) of Nepal's website. It retrieves data such as full name, permanent address, gender, category, qualification, university/country, passout year, and registration number.

## Requirements
- Python 3.x
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- Pandas library (`pip install pandas`)
- lxml library (`pip install lxml`)

## Usage
1. Ensure all dependencies are installed.
2. Run the script `web_scraper.py`.
3. The script will fetch the data from the [NEC Applicant Information](https://nec.gov.np/applicant/cat/26) page.
4. The extracted data will be stored in a Pandas DataFrame and printed to the console.
5. You can access the data for further processing or export it to CSV, Excel, or other formats as required.

## Methodology
- The script utilizes the Requests library to fetch the HTML content of the webpage.
- BeautifulSoup is used to parse the HTML content and extract relevant information.
- The script locates the table containing applicant information and iterates through each row to collect data.
- For each applicant, it extracts additional details by following links to individual applicant pages.
- Finally, the collected data is structured into a DataFrame for easy analysis and manipulation.

## License
This project is licensed under the [MIT License](LICENSE).

