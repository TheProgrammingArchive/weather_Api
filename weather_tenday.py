from bs4 import BeautifulSoup
import requests

global site_source
global soup

#temporary source
site_source = requests.get('https://weather.com/en-IN/weather/tenday/l/bf01d09009561812f3f95abece23d16e123d8c08fd0b8ec7ffc9215c0154913c').text
soup = BeautifulSoup(site_source, features='lxml')

class weatherTenDay:
    def timeof_report(self):
        time = soup.find('div', class_='DailyForecast--timestamp--iI022').text
        return time

    def weather_Details(self):
        for weather_Report in soup.find_all('summary', class_='Disclosure--Summary--AvowU DaypartDetails--Summary--2nJx1 Disclosure--hideBorderOnSummaryOpen--LEvZQ'):

            dateof_Report = weather_Report.find('h2', class_='DetailsSummary--daypartName--1Mebr').text

            temperature_day = weather_Report.find('div', class_='DetailsSummary--temperature--3FMlw').text

            weather_Description = weather_Report.find('div', class_='DetailsSummary--condition--mqdxh').text

            avg_precipindex = weather_Report.find('div', class_='DetailsSummary--precip--2ARnx').text

            wind_Details = weather_Report.find('div', class_='DetailsSummary--wind--Cv4BH DetailsSummary--extendedData--aaFeV').text

            lists = [dateof_Report, temperature_day, weather_Description, avg_precipindex, wind_Details]
            print(lists)

tcal = weatherTenDay()
print(tcal.timeof_report())
tcal.weather_Details()

