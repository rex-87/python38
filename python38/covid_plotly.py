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

	import plotly.express as px
	import pandas as pd
	import os
	
	this_file_path = os.path.abspath(__file__)
	this_file_folder = os.path.dirname(this_file_path)
	
	confirmed_file_path = os.path.abspath(os.path.join(this_file_folder, r'..\data\time_series_covid19_confirmed_global.csv'))

	# df = px.data.iris()
	df = pd.read_csv(confirmed_file_path).transpose().reset_index()
	
	tdf = df.loc[4:,:].rename(columns={'index':'date'})
	for c in range(266):
		tdf = tdf.rename(columns={c:"{}; {}".format(df.loc[1, c], df.loc[0, c]).replace('; nan', '')})
	fig = px.scatter(tdf, x = 'date', y = 'France', title="A Plotly Express Figure")

	fig.show()
	
	foo = tdf.loc[:,['date', 'Afghanistan']]
	foo['country'] = 'Afghanistan'
	foo = foo.rename(columns={'Afghanistan':'confirmed'})
	
	import IPython; IPython.embed(colors='Neutral')

## -------- SOMETHING WENT WRONG -----------------------------	
except:

	import traceback
	LOG.error("Something went wrong! Exception details:\n{}".format(traceback.format_exc()))

## -------- GIVE THE USER A CHANCE TO READ MESSAGES-----------
finally:
	
	input("Press any key to exit ...")
