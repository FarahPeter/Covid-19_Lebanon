from bs4 import BeautifulSoup
import requests
import re
import json

def find_between( s, first, last=None):
    try:
        if (last!=None):
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        else:
            start = s.index(first) + len(first)
            return s[start:]
    except ValueError:
        return ""


def GetCovid19DataLeb():
    def ExtractData(response):
        #total cases
        totalcasesFullData=find_between(response,"Total Cases","responsive")
        day=find_between(totalcasesFullData,"categories: ","        }")
        totalCasesData=find_between(totalcasesFullData,"data: ","        }],")
        print("Days: "+str(day))
        print("Total cases: "+str(totalCasesData))

        #daily cases
        dailyCasesFullData = find_between(response, "Daily New Cases", "responsive")
        dailyCasesData = find_between(dailyCasesFullData, "data: ", "            },")
        print("Daily cases: "+str(dailyCasesData))

        #Active cases
        activeCasesFullData = find_between(response, "Active Cases", "responsive")
        activeCasesData = find_between(activeCasesFullData, "data: ", "        }")
        print("Active cases: "+str(activeCasesData))

        # total death
        totalDeathFullData = find_between(response, "Total Deaths", "responsive")
        totalDeathData = find_between(totalDeathFullData, "data: ", "        }],")
        print("Total death: " + str(totalDeathData))

        # daily death
        dailyDeathFullData = find_between(response, "Daily Deaths", "responsive")
        dailyDeathData = find_between(totalDeathFullData, "data: ", "        }],")
        print("Daily death: " + str(totalDeathData))

        #converting all results into array
        day=json.loads(day)
        totalCasesData=json.loads(totalCasesData)
        dailyCasesData=json.loads(dailyCasesData)
        activeCasesData=json.loads(activeCasesData)
        totalDeathData=json.loads(totalDeathData)
        dailyDeathData=json.loads(dailyDeathData)
        #print(len(totalCasesData),len(dailyCasesData),len(activeCasesData),len(totalDeathData),len(dailyDeathData))
        return ({"total cases":totalCasesData,"total deaths":totalDeathData,"active cases":activeCasesData})


    def GetCovidData():
        cookies = {
        '_ga': 'GA1.2.563498610.1672792908',
        '_gid': 'GA1.2.1844988139.1672792908',
        '_gat': '1',
        'fs.bot.check': 'true',
        '__gads': 'ID=86f9c9045c33f903-22fef53606d8000d:T=1672792918:RT=1672792918:S=ALNI_MbnRCaQEjrGfY30rYMGsm2rmOV65A',
        '__gpi': 'UID=00000bba91ad4e11:T=1672792918:RT=1672792918:S=ALNI_Ma3YqD6eWQd_z90UJbb8aipLjhx3w',
    }
        headers = {
        'Host': 'www.worldometers.info',
        'Sec-Ch-Ua': '"Not;A=Brand";v="99", "Chromium";v="106"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        # 'Cookie': '_ga=GA1.2.563498610.1672792908; _gid=GA1.2.1844988139.1672792908; _gat=1; fs.bot.check=true; __gads=ID=86f9c9045c33f903-22fef53606d8000d:T=1672792918:RT=1672792918:S=ALNI_MbnRCaQEjrGfY30rYMGsm2rmOV65A; __gpi=UID=00000bba91ad4e11:T=1672792918:RT=1672792918:S=ALNI_Ma3YqD6eWQd_z90UJbb8aipLjhx3w',
    }
        response = requests.get('https://www.worldometers.info/coronavirus/country/lebanon/',cookies=cookies,headers=headers)
        return response

    response=GetCovidData()
    data=ExtractData(response.text)
    return(data)


#GetCovid19DataLeb()