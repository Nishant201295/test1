import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import time

def scrape_data():
    df = pd.DataFrame(columns=['SNO', 'call OI', 'call CHNG IN OI', 'call VOLUME', 'call IV', 'call LTP', 'call CHNG',
                               'call BID QTY', 'call BID PRICE', 'call ASK PRICE', 'call ASK QTY', 'STRIKE PRICE',
                               'put BID QTY', 'put BID PRICE', 'put ASK PRICE', 'put ASK QTY', 'put CHNG', 'put LTP',
                               'put IV', 'put VOLUME', 'put CHNG IN OI', 'put OI'])

    co = Options()
    co.add_argument("--log-level=3")
    chrome_options = Options()
    driver = Chrome(executable_path=r"C:\Users\deepa\Downloads\chromedriver_win32 (2)\chromedriver.exe",
                    options=chrome_options)

    driver.get('https://www.nseindia.com/get-quotes/derivatives?symbol=BANKNIFTY')

    driver.minimize_window()
    time.sleep(3)

    for j in range(50):
        driver.refresh()
        continue_link1 = driver.find_element_by_xpath('''//*[@id="subtab-derivatives"]/div[2]/nav/div/div/a[2]''')
        time.sleep(10)
        filter_tag = SoupStrainer("table")

        continue_link1.click()
        time.sleep(3)
        rtime = str(driver.find_element_by_xpath('''//*[@id="asondate"]''').text)
        if rtime == '':
            continue

        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser", parse_only=filter_tag)

        gdp_table = soup.find("table", attrs={"id": "optionChainTable-indices"})
        gdp_table_data = gdp_table.tbody.find_all("tr")

        if len(gdp_table_data) == 1:
            continue
        else:
            for i in range(len(gdp_table_data)):
                list1 = []
                for td in gdp_table_data[i].find_all("td"):
                    # remove any newlines and extra spaces from left and right
                    cell_text = td.text
                    if cell_text is None or cell_text == '':
                        cell_text = '0'
                    cell_text = cell_text.replace(',', '')
                    list1.append(cell_text)

                if len(list1) > 0:
                    list1 = ['0' if i == '-' else i for i in list1]
                else:
                    continue
                del list1[0]
                del list1[-1]

                list1 = list(map(float, list1))
                list1.insert(0, rtime)
                df.loc[len(df)] = list1

    df.to_excel('option-data.xlsx')


def main():
    st.title('NSE Option Data Scraper')
    st.write("This app scrapes option data from NSE website")

    if st.button("Scrape Data"):
        scrape_data()
        st.success("Data scraped successfully!")

if __name__ == "__main__":
    main()
