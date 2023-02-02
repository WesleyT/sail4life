import requests

from bs4 import BeautifulSoup
	
def dollartopound(dollar):
	return float(dollar * .72)

	
def poundtodollar(pound):
	return float(pound * 1.4)

def savepound():
	file = open("totalpounds.txt", "w")
	a = int(gettotalpound())
	file.write(str(a))
	file.close()

def savedollar():
	file = open("totaldollars.txt", "w")
	a = int(gettotaldollar())
	file.write(str(a))
	file.close()

	
def getcharitywater():
	site = requests.get("https://my.charitywater.org/jack-duncton/sail-4-life-sea-of-thieves-livestream")
	soup = BeautifulSoup(site.text, "html.parser")
	a = soup.find('h3', {'class', 'h10'})
	b = float(a.contents[1])
	return b
	
	
def getwateraid():
	site = requests.get("https://www.justgiving.com/fundraising/sail-4life")
	soup = BeautifulSoup(site.text, "html.parser")
	a = soup.find('span', {'class', 'statistics-amount-raised'})
	b = float(a.contents[0][1:])

	return b
	
def gettotaldollar():
	site1 = poundtodollar(getwateraid())
	site2 = getcharitywater()
	return site1 + site2
	
def gettotalpound():
	site1 = dollartopound(getcharitywater())
	site2 = getwateraid()
	return site1 + site2

def savedata():
	savepound()
	savedollar()

	
savedata()
