import urllib2
from BeautifulSoup import BeautifulSoup
import urlContentParser

# 2016-17
# 1. October - 1475272800
# 2. November - 1477954800
# 3. December - 1480546800
# 4. January - 1483225200
# 5. February - 1485903600
# 6. March - 1488322800
# 7. April - 1490997600
# 8. May - 1493589600
# 9. June - 1496268000
# 10. July - 1498860000
# 11. August - 1501538400
# 12. September - 1504216800

baseUrl = 'https://echelog.com/logs/browse/angularjs/'
initialUrl = ['1475272800','1477954800','1480546800','1483225200','1485903600','1488322800','1490997600','1493589600','1496268000','1498860000','1501538400','1504216800']
extraUrl = []
url = []

for eachMonth in range(0,11):
    #Putting the extraUrls into the extraUrl list.
    opener = urllib2.build_opener()
    ourUrl = opener.open(baseUrl+initialUrl[eachMonth]).read()
    soup = BeautifulSoup(ourUrl)
    numberList = ['0', '1', '2', '3', '4', '5', '7', '7', '8', '9']
    for eachA in soup.findAll('a'):
        firstChar = (str(eachA.get('href')))[0]
        if(firstChar in numberList):
            extraUrl.append(eachA.get('href'))

    #Editing the extraUrl list.
    #Months with 31 days
    if eachMonth==0 or eachMonth==2 or eachMonth==3 or eachMonth==5 or eachMonth==7 or eachMonth==9 or eachMonth==10:
        for i in range(0,3):
            extraUrl.pop(0)
        extraUrl.pop()
        del extraUrl[32:]
        extraUrl.pop()

    #Months with 30 days
    if eachMonth==1 or eachMonth==6 or eachMonth==8 or eachMonth==11:
        for i in range(0,3):
            extraUrl.pop(0)
        extraUrl.pop()
        del extraUrl[1:] #BUG!!!
        extraUrl.pop()

    #Month with 28 days
    if eachMonth==4:
        for i in range(0,3):
            extraUrl.pop(0)
        extraUrl.pop()
        del extraUrl[29:]
        extraUrl.pop()

    #Populating url list.
    for i in range(0,len(extraUrl)):
        url.append(baseUrl + extraUrl[i])

    #Calling urlContentParser
    urlContentParser.urlContentParser(url, eachMonth)

    #Resetting extraUrl to empty
    extraUrl = []