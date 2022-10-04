from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from helpers.colors import colors
import csv



# Create chrome driver
def createDriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    return driver


# return the html of the page
def getPage(URL):
    browser = createDriver()
    browser.set_page_load_timeout(30)
    browser.get(URL)
    # sleep 10 seconds to load the page completely
    sleep(10)
    page = browser.page_source
    browser.quit()
    return page
    

# get the table body
def getTableBody(contestID):
    URL = f'https://vjudge.net/contest/{contestID}#rank'
    page = getPage(URL)
    soup = BeautifulSoup(page, 'html.parser')
    RankTable = soup.find(id='contest-rank-table')
    if(RankTable == None):
        print(f'\n{colors.red}Invalid contest ID or something wrong happened! ❌\n{colors.reset}')
        exit()
    TableBody = RankTable.find('tbody')
    return TableBody


# parse Trainee
def parseTrainee(traineeRaw):
    Info = list(filter(lambda x: x != '', traineeRaw));
    Trainee = {
        'Rank': Info[0],
        'Name': Info[1],
        'Solved Problems': Info[2]
    }
    return Trainee


# to store the trainees
def getTrainees(TableBody):
    Trainess = []
    for row in TableBody.find_all('tr', class_='this'):
        traineeRaw = []
        for col in row.find_all('td', class_='meta'):
            traineeRaw.append(col.text)
        Trainess.append(parseTrainee(traineeRaw))
    return Trainess

    
# write the trainees to csv file
def saveToCsv(Trainees):
    TrineesInfo = ['Rank', 'Name', 'Solved Problems']
    with open('Trainees.csv', 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames = TrineesInfo)
        writer.writeheader()
        writer.writerows(Trainees)    

    
def main():
    contestID = input(f'{colors.gold}Enter the ID of the contest: {colors.reset}')
    RankTable = getTableBody(contestID)
    Trainees = getTrainees(RankTable)
    saveToCsv(Trainees)
    print(f'{colors.green}\nBoard is scrapped successfully! ✅\n{colors.reset}')
    
    
if __name__ == '__main__':
    main()