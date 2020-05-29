from bs4 import BeautifulSoup
import requests
import csv
from os import path

source_code = requests.get("https://www.latestly.com/coronavirus-live-map-india-news-updates/").text
soup = BeautifulSoup(source_code,"lxml")

numbersinfo = []
textforit = []

article = soup.find("ul", class_="covid-list")

for subarticle in article.find_all("li"):
    data = subarticle.find("p").text
    numbersinfo.append(data)

    text = subarticle.find("span").text
    textforit.append(text)

print("ALL OVER INDIA")

for i in range(len(textforit)):
    print(f"{numbersinfo[i]:15} --> {textforit[i]:6}")

#The class was created to sort the state names
class store_data:

    def __init__(self, sName, sActive, sDeaths, sRecovered):
        self.sName = sName
        self.sActive = sActive
        self.sDeaths = sDeaths
        self.sRecovered = sRecovered

arrObj = []

article = soup.find("table", class_="table-fixed covid-table")

flag = 0
for subtable in article.find_all("tr"):
    if flag == 0:
        flag = 1
        continue
    name = subtable.find("div", class_="col1").text
    active = subtable.find("div", class_="col2").text
    deaths = subtable.find("div", class_="col3").text
    recovered = subtable.find("div", class_="col4").text
    if name == "Total":
        continue
    arrObj.append(store_data(name, active, deaths, recovered))

#Sorting the names of the state as they are not in proper order
for i in range(len(arrObj)):
    for j in range(i, len(arrObj)):

        if arrObj[i].sName > arrObj[j].sName:
            temp = arrObj[i]
            arrObj[i] = arrObj[j]
            arrObj[j] = temp


a = "STATE / UNIONTERRITORY"
b = "ACTIVE"
c = "DEATHS"
d = "RECOVERED"

print(f"\n\n| {a:27} | {b:8} | {c:7} | {d:9} |\n")

arrObj.remove(arrObj[30])

for i in range(len(arrObj)):

    print(f"| {arrObj[i].sName:27} | {arrObj[i].sActive:8} | {arrObj[i].sDeaths:9} | {arrObj[i].sRecovered:7} |")


if path.isfile("CORONA.csv") == True:
    flag1 = 0
    flag2 = 0
    i = 0
    print("\n\nSince last time you checked the status what has changed...")
    with open("CORONA.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if flag1 == 0:
                flag1 = 1
                continue

            tempName = line[0]
            tempActive = int(line[1])
            tempDeaths = int(line[2])
            tempRecovered = int(line[3])

            diff = int(arrObj[i].sActive) - tempActive
            if diff != 0:
                if flag2 == 0:
                    print(f"In {tempName}")
                    flag2 = 1

                if diff > 0:
                    print(f"\t Active = +{diff}")
                else:
                    print(f"\t Active = {diff}")
            
            diff = int(arrObj[i].sDeaths) - tempDeaths
            if diff != 0:
                if flag2 == 0:
                    print(f"In {tempName}")
                    flag2 = 1
                
                if diff > 0:
                    print(f"\t Deaths = +{diff}")
                else:
                    print(f"\t Deaths = {diff}")
            
            diff = int(arrObj[i].sRecovered) - tempRecovered
            if diff != 0:
                if flag2 == 0:
                    print(f"In {tempName}")
                    flag2 = 1
                
                if diff > 0:
                    print(f"\t Recovered = +{diff}")
                else:
                    print(f"\t Recovered = {diff}")
            i += 1
            if flag2 == 1:
                print()
            flag2 = 0
            

    with open("CORONA.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow([a,b,c,d])

        for i in range(len(arrObj)):
            csv_writer.writerow([arrObj[i].sName, arrObj[i].sActive, arrObj[i].sDeaths, arrObj[i].sRecovered])

else:

    with open("CORONA.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow([a,b,c,d])

        for i in range(len(arrObj)):
            csv_writer.writerow([arrObj[i].sName, arrObj[i].sActive, arrObj[i].sDeaths, arrObj[i].sRecovered])
