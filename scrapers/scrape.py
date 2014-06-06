#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import csv

def getMNames(trs, year, w):
	for tr in trs:
		td = tr.findAll("td")
		w.writerow([year, td[0].text, td[1].text, "m", td[2].text, ""])

def getFNames(trs, year, w):
	for tr in trs:
		td = tr.findAll("td")
		w.writerow([year, td[0].text, td[3].text, "f", "", td[4].text])

def request(w, year):
	URL = "http://www.ssa.gov/cgi-bin/popularnames.cgi"
	payload = { "year": year, "top": 1000, "number": "n" }
	r = requests.post(URL, data=payload)
	soup = BeautifulSoup(r.text)
	table = soup.find("table", {"width":"$tablewidth"})
	trs = table.findAll("tr", {"align":"right"})
	getMNames(trs, year, w)
	getFNames(trs, year, w)

def init(startYear, endYear):
	header = ["year","rank","name","gender","numM","numF"]
	outfile = open("babynames.csv", "wb")
	writer = csv.writer(outfile)
	writer.writerow(header)
	endYear += 1
	for year in range(startYear, endYear):
		request(writer, year)
	outfile.close()

if __name__ == "__main__":
	init(1880, 2013)