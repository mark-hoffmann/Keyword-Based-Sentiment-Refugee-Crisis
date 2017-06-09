import requests
from BeautifulSoup import BeautifulSoup
'''
import MySQLdb

db = MySQLdb.connect("localhost","root","password","Syria" )
cursor = db.cursor()
'''
f = open('Independence.txt', 'w')



monthDict = {'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07', 'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December':'12'}
n = 0
ave= 0
sum = 0

#max stories per page
url2 = "http://www.independent.co.uk/search/simple.do?articleTypes=news&useHideArticle=true&sectionId=506&startYear=2010&searchString=Syria+refugee&startDay=1&useSectionFilter=true&sortOrder=desc&sortString=publishdate&startMonth=1&destinationSectionUniqueName=search&pageLength=500&publicationName=ind&pageNumber="

for i in range(1,5):
	r = requests.get(url2+str(i))
	bs = BeautifulSoup(r.text)
	
	divs = bs.findAll( 'div', { 'class': 'summary' } )
	print url2+str(i)
	for one in divs:
		
		try:
			date = one.find('span', {'class':'resultDateInfo'})
			link = one.find( 'a',href=True)
			#print "NEW ONE"
			#print date.text
			dateList = date.text.split(" ")
			parsedDate = monthDict[dateList[2]] + '/' + dateList[1] + '/' + dateList[3]
			#print parsedDate
			#print link['href']
			s = requests.get(link['href'])
			bss = BeautifulSoup(s.text)
			div = bss.find( 'div', {'class': 'body '})
			#print div.text
			charNum = len(div.text)
			
			n += 1
			
			print str(n) + " out of 1597"
			#sum += float(charNum)
			#ave = sum / n
			#print "UPDATED AVERAGE: " + str(ave)  #after running all articles, average = 4697 characters
			f.write('Independent: ' + parsedDate)
			f.write(div.text)
			'''
			try:
				cursor.execute("""INSERT INTO Syria (Source, Date, Text) VALUES('Independent',%s,%s) """,(parsedDate,div.text))
				db.commit()
			except:
				db.rollback()

			'''
		except Exception, e:
			print "Couldn't do it: %s" % e
	

f.close()
