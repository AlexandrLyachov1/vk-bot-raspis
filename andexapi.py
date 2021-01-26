from urllib.request import urlopen
from bs4 import BeautifulSoup
# Пандемия_COVID-19
page = urllib.urlopen("https://www.gismeteo.ru/weather-moscow-4368/")
# 17
soup = BeautifulSoup(page)
wx-values = soup.findAll(attrs={"class":"tab-weather__value_l"})
print wx-values[1]