from bs4 import BeautifulSoup
import time
import csv

start_url= "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser= webdriver.Chrome("/chromedriver_win32/chromedriver.exe")
browser.get(start_url)


def scrap():
    headers=["Proper name","Distance","Mass","Radius"]
    planet_data=[]
    

    for i in range(0,503):
        soup=BeautifulSoup(browser.page_source,"html.parser")

        for th_tag in soup.find_all("th",attrs={"class","brightest_stars"}):
            tr_tags= th_tag.find_all("tr")
            temp_list= []

            for index, tr_tag in enumerate(tr_tags):
                if index == 0:
                    temp_list.append(tr_tag.find_all("a") [0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")

            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a')
    
    with open("scraper.csv", "w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrap()