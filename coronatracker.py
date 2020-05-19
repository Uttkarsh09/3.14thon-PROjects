#if you think that this script is shit: 
#   bitch this is underconstruction

from bs4 import BeautifulSoup
import requests

source_code = requests.get("https://www.mygov.in/covid-19").text
soup = BeautifulSoup(source_code,"lxml")

numbersInfo = []
textforit = []

for article in soup.find_all("div", class_="iblock_text"):
    
    data = article.find("span", class_="icount").text
    numbersInfo.append(data)

    text = article.find("div", class_="info_label").text
    textforit.append(text)

print("""
    This s1mple script tells the current number of corona cases in India
    The numbers are provided by www.mygov.in
""")

arrow = "-->"

for i in range(len(textforit)):
    print(f"{textforit[i]:20} --> {numbersInfo[i]:6}")