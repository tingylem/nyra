import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


def belmont(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    sec = soup.find('table', class_='race-entry-table table-responsive')
    race=sec.find('caption', class_='hidden')
    print (race.text.strip())
    sect=sec.tbody
    for tr in sect.find_all('tr'):
        td = tr.find_all('td')
       # link=tr.find('a',class_='text-style-body-2')
        row = [elem.text.strip() for elem in td]
        ml=row[8]
        mlf, mlb=ml.split('-')
        ml=float(mlf) / float(mlb)
        if row[5]=='Dylan Davis' or row[5]=='Javier Castellano'or row[5]=='Irad Ortiz, Jr.'or row[5]=='John R. Velazquez': #Manuel Franco
            if ml<6:
                print(str(row[0]),str(row[2].partition('\n')[0]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),str(row[8]))

def main():
    #https://www.nyra.com//ajaxgetrace?tpl=FullEntryRaceTable&trackID=2&race="+raceInt+"&date=2020-06-04
    baseurl="https://www.nyra.com//ajaxgetrace?tpl=FullEntryRaceTable&trackID=2&race="
    year=datetime.now().strftime("%Y")
    month=datetime.now().strftime("%m")
    date=datetime.now().strftime("%d")
    an="&date="
    for x in range(1,14):
        url=baseurl+str(x)+an+year+"-"+month+"-"+date
        belmont(url)

if __name__ == "__main__":
    main()