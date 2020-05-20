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

print("ALL OVER INDIA\n")
for i in range(len(textforit)):
    print(f"{textforit[i].upper():20} -->  {numbersInfo[i]:6}")


sName = []
sConfirm = []
sActive = []
sRecovered = []
sRIP = []

for article in soup.find_all("div", class_="views-row"):
    
    sName.append(article.find("span", class_="st_name").text)
    sConfirm.append(article.find("div", class_="tick-confirmed").small.text)
    sActive.append(article.find("div", class_="tick-active").small.text)
    sRecovered.append(article.find("div", class_="tick-discharged").small.text)
    sRIP.append(article.find("div", class_="tick-death").small.text)

a = "STATE / UNION TERRITORY"
b = "CONFIRM"
c = "ACTIVE"
d = "RECOVERED"
e = "DEATHS"
print(f"\n\n| {a:22} | {b:8} | {c:7} | {d:10} | {e:7} |\n")
for i in range(len(sName)):
    
    print(f"| {(sName[i]):22} | {(sConfirm[i]):8} | {(sActive[i]):7} | {(sRecovered[i]):10} | {(sRIP[i]):7} |")