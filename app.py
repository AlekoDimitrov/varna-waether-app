from bs4 import BeautifulSoup
import requests


def extract():
    url = 'https://www.sinoptik.bg/varna-bulgaria-100726050?search'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup


def transform(soup):
    currentTemp = soup.find('span', class_='wfCurrentTemp').text
    # print(currentTemp)
    a = soup.findAll('a', class_='wfNonCurrentContent')
    for item in a:
        days = item.find('span', class_='wfNonCurrentDay').text
        # print(days)
        
        dates = item.find('span', class_='wfNonCurrentDate').text
        # print(dates)
        
        temperatures = item.find('span', class_='wfNonCurrentTemp').text.split()
        temperatures.remove('|')
        # print(temperatures)
        
        conditions = item.find('strong', class_='wfNonCurrentCond').text
        # print(conditions)
        
        weather = {
            'currentTemp': currentTemp,
            'days': days,
            'dates': dates,
            'temperatures': temperatures,
            'conditions': conditions
        }
        weatherList.append(weather)
    return


weatherList = []
c = extract()
transform(c)
print(weatherList)