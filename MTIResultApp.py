import requests
import schedule
import time
import datetime
import sys
from bs4 import BeautifulSoup


session = requests.Session()

def killApp():
	if datetime.datetime.now().date() >= datetime.date(2021, 4, 2):
		  sys.exit('Date is overdue exiting app ...')
	
def functionalAlert():
	discParams = {
	"username": "MTI Final",
	"content": f"Still Working \n {datetime.datetime.now().strftime('%c')}",
	"avatar_url": "https://i.ibb.co/Xjq0PRf/cringe-Face.png"
	}
	session.post('https://discord.com/api/webhooks/825352589692239883/dloTkdl2W3g_EbBPLbvSWVInZjacT0-JhL0wzuu6mjmGPg1HxiIBw8g2f0i2OTMuHDp6', data=discParams)

def resultAlert():
	discParams = {
	"username": "MTI Final",
	"content": "@everyone \n **El Natega Zhrt** \n http://www.mti.edu.eg/university/student/",
	"avatar_url": "https://i.ibb.co/Xjq0PRf/cringe-Face.png"
	}
	session.post('https://discord.com/api/webhooks/825349277865345065/RIy6kKMVnTC6OdKURYo1ovfZSGOvQdO6yBgKw03IeoNurFPC4QD75znqLLFqFV89m7hW', data=discParams)


def getResult():
	postParams = {
		"__EVENTTARGET": "ctl00$Main$btnLoginEmail",
		"__EVENTARGUMENT": "",
		"__VIEWSTATE": "/wEPDwULLTEyODYwMjA1NzVkZKWggHAMzZrhX7ltibP8805z/TK7/ixIarKr9oTqBQBb",
		"__VIEWSTATEGENERATOR": "B71B77C3",
		"ctl00$Main$txtID": "",
		"ctl00$Main$txtPassword": "",
		"ctl00$Main$txtEmail": "Mohamed.81717@cs.mti.edu.eg"
	}
	response = session.post('http://www.mti.edu.eg/university/student/login.aspx', data=postParams)
	soup = BeautifulSoup(response.text, 'html.parser')
	if (len(soup.findAll(class_='list-group-item')) != 13):
		for i in range(5):
			resultAlert()
			time.sleep(5)

schedule.every(2).minutes.do(getResult)
schedule.every(30).minutes.do(killApp)
schedule.every(30).minutes.do(functionalAlert)

while 1:
	schedule.run_pending()
	time.sleep(1)