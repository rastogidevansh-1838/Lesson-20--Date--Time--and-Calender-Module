import random
import time
def getRandomDate(startDate, endDate):
    print("Printing Random date between", startDate, "and", endDate)
    randomGenerator = random.random()
    date_format = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(startDate, date_format))
    endTime = time.mktime(time.strptime(endDate, date_format))
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(date_format, time.localtime(randomTime))
    return randomDate
print("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))