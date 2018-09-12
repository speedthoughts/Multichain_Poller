#!/usr/bin/env python

#-----------------------------------------------------------------------------------------------------------------------------
#
# API CALLS TO MULTICHAIN TO - GET BLOCK HASH, GET BLOCK DETAILS AND GET TRANSACTIONS FROM A BLOCK
# RETURNS APPROPRIATE VALUE TO MAIN poller.py	
# Date# 9-Sep-2018
#
#----------------------------------------------------------------------------------------------------------------------------

import requests
import json
from requests import Request, Session

def mchain_getblockhash(url, uid, pwd, bht):

	URL = url
	userid = uid
	password = pwd
	block_ht = str(bht)
	
	
	PARAMS = {
		"jsonrpc":"2.0",
		"id":0,
		"method":"getblock",
		"params":[block_ht]
	}

	data = json.dumps(PARAMS)
	try:
		response = requests.get(URL, auth=(userid, password), data = data)
		result = response.json()
		#print str(response.status_code)
		#print str(response.text)
		if response.status_code == 200:
			rslt = result['result']['hash']
		else:
			rslt = '--NoBlock--'
		
		return(rslt)
	except Exception as e:
		rslt = 'E0101'
		#print rslt + ' ' + str(e)
		return(rslt)

def mchain_getblock(url, uid, pwd, hid):

	URL = url
	userid = uid
	password = pwd
	hash = hid

	PARAMS = {"jsonrpc":"2.0","id":0,"method":"getblock","params":[hash]}
	#print PARAMS
	
	data = json.dumps(PARAMS)
	response = requests.get(URL, auth=(userid, password), data = data)
	result = response.json()
	#print str(response.status_code)
	#print str(response.text)
	
	rslt = result['result']['tx']
	#print rslt
	return(rslt)

def mchain_getrawtransaction(url, uid, pwd, tid):

	URL = url
	userid = uid
	password = pwd
	trx_id = tid
	verbose = 1
	a_name = ''
	a_data = ''
	a_time = 0.00
	
	PARAMS = {"jsonrpc":"2.0","id":0,"method":"getrawtransaction","params":[trx_id,verbose]}
	#print PARAMS
	
	data = json.dumps(PARAMS)
	response = requests.get(URL, auth=(userid, password), data = data)
	result = response.json()
	#print str(response.status_code)
	#print str(response.text)

	rslt = result['result']['vout'][0]['assets']
	if len(rslt) == 0:
		r=0 #Do Nothing. This Is Not A Asset Trx.
	else:
		#This Transaction Is An Asset Trx.
		a_name = result['result']['vout'][0]['assets'][0]['name'] #<-- Here You Capture The Transaction Asset Name
		a_data = result['result']['data'] #<-- Here You Capture The Transaction Message Data 
		a_time = result['result']['blocktime'] #<-- Here You Capture The Transaction Message Time. 
		##
		#The Transaction Has No Timestamp That Is Built Into It. Each Node Has Its Own Time When It First Saw The Transition (Timereceived) 
		#And First Added It To Its Local Wallet (Time). But All Nodes Should Agree On The Blocktime, Which Is The Timestamp Of The Block In 
		#Which The Transaction Was Confirmed (If It Has Already Been Confirmed, That Is).
		##
		
	return (a_name, a_data, a_time)	
