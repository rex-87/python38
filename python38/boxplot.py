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

	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt
	import plotly.express as px	

	# ---- Fixing random state for reproducibility
	np.random.seed(19680801)

	# ---- fake up some data
	N = 30
	mu = 4.5
	# uut_std, meas_std = .010, .0025
	uut_std, meas_std = .010, .0025
	uut_count = 10
	data = []
	for i in range(uut_count):
		data.append(np.random.normal(mu+np.random.normal(0, uut_std, 1), meas_std, N))

	df = pd.DataFrame(data).transpose()
	# import IPython; IPython.embed(colors='Neutral')
	fig = px.box(df, points = False) # points: 'all' displays all points; False displays no points and whiskers extend to min/max
	fig.update_layout(
		title= 'Example of box plot: N = {}, mu = {}, uut_std = {}, meas_std = {}'.format(
			N,
			mu,
			uut_std,
			meas_std,
		),
		xaxis_title = "Serial Number",
		yaxis_title = "Value",
	)
	fig.update_yaxes(range=[4.35, 4.6])
	fig.show()

	# ---- matplotlib
	# fig1, ax1 = plt.subplots()
	# ax1.set_title(
		# 'Example of box plot: N = {}, mu = {}, uut_std = {}, meas_std = {}'.format(
			# N,
			# mu,
			# uut_std,
			# meas_std,
		# ),
	# )
	# ax1.boxplot(data, showfliers=False)
	
	# plt.grid(which = 'major', linestyle='--', linewidth=0.5)
	# plt.grid(which = 'minor', linestyle='--', linewidth=0.2)
	# plt.minorticks_on()
	# plt.show()

## -------- SOMETHING WENT WRONG -----------------------------	
except:

	import traceback
	LOG.error("Something went wrong! Exception details:\n{}".format(traceback.format_exc()))

## -------- GIVE THE USER A CHANCE TO READ MESSAGES-----------
finally:
	
	# input("Press any key to exit ...")
	pass
