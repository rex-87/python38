# -*- coding: utf-8 -*-
"""
	python38
	
	This project is an example of a Python project generated from cookiecutter-python.
"""

## -------- COMMAND LINE ARGUMENTS ---------------------------
## https://docs.python.org/3.7/howto/argparse.html
import argparse
CmdLineArgParser = argparse.ArgumentParser()
CmdLineArgParser.add_argument(
	"-v",
	"--verbose",
	help = "display debug messages in console",
	action = "store_true",
)
CmdLineArgs = CmdLineArgParser.parse_args()

## -------- LOGGING INITIALISATION ---------------------------
import misc
misc.MyLoggersObj.SetConsoleVerbosity(ConsoleVerbosity = {True : "DEBUG", False : "INFO"}[CmdLineArgs.verbose])
LOG, handle_retval_and_log = misc.CreateLogger(__name__)

try:
	
	## -------------------------------------------------------
	## THE MAIN PROGRAM STARTS HERE
	## -------------------------------------------------------
    
	import requests

	import pdfkit
	path_wkthmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
	config = pdfkit.configuration(wkhtmltopdf = path_wkthmltopdf)
	pdfkit_options = {
		# 'minimum-font-size': 30,
		'zoom': 2,
		'disable-javascript': None,
	}

	from bs4 import BeautifulSoup
	
	weekly_url = 'https://www.economist.com/weeklyedition/'
	page = requests.get(weekly_url)
	soup = BeautifulSoup(page.text, 'html.parser')
	
	url_l = ['https://www.economist.com'+a.get('href') for a in soup.body.div.div.next_sibling.next_sibling.next_sibling.main.div.find_all('a', class_='headline-link')]	
	
	# for url in url_l:
		# LOG.info("HTML to PDF: "+url+" ...")
		# out_pdf_name = "_".join(url.split('/')[-4:])
		# pdfkit.from_url(
			# url,
			# out_pdf_name+".pdf",
			# configuration = config,
			# options = pdfkit_options,
		# )

	LOG.info("HTML to PDF: generate only one pdf ...")
	pdfkit.from_url(
		url_l,
		"out.pdf",
		configuration = config,
		options = pdfkit_options,
	)

## -------- SOMETHING WENT WRONG -----------------------------	
except:

	import traceback
	LOG.error("Something went wrong! Exception details:\n{}".format(traceback.format_exc()))

## -------- GIVE THE USER A CHANCE TO READ MESSAGES-----------
finally:
	
	# input("Press any key to exit ...")
	pass
