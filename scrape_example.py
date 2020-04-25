import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_indeed():
	url="https://www.indeed.com/jobs?q=software+engineer+python&l=Spring%2C+TX"
	response = requests.get(url)

	soup = BeautifulSoup(response.content, "html.parser")
	results = soup.find(id=ResultsContainer)
	print(results)
	return results

def scrape_eia():
	url="https://www.eia.gov/outlooks/aeo/data/browser/data/index.php?studyID=AEO2020&tableID=1-AEO2020&caseID=ref2020-d112119a&regionID=0-0&freq=A&sid=&type=data"

	try:
		response = requests.get(url)
		
		if response.getcode() == 200:
			r = json.loads(response)
			# generate dataframe
			df = pd.read_json(r)
			df.to_csv(r'C:\Users\nfebres\Documents\GitHubProjects\web_scraping' + 'example.csv')
			print('the eia web data frame ' + df)
			return df
			
	except exception as e:
		print("error occured " + e)
		]
# numbers = [1, 2, 3]
# for i, v in enumerate(numbers):
	# print(v)
	
# list = [x*x for x in my_list if x is not None]
 # def fizz_buzz(list):
	# for i, v in enumerate(list):
		# if v % 3 == 0:
			# v = 'Fizz'
		# if v % 5 == 0:
			# v = 'buzz'
			
# def is_odd:
	# return v % 2 == 1
	

def main():
	scrape_eia()
	