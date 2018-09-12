#!/usr/bin/env python

#-----------------------------------------------------------------------------------------------------------------------------
#
# THE MAIN INTENTION OF THIS PROGRAM IS TO HELP UNDERSTAND THE USAGE OF BLOCKCHAIN AND MORE SPECIFICALLY MULTICHAIN.
#
# PURPOSE::
# THIS PYTHON SCRIPT WILL POLL A MULTICHAIN BLOCKCHAIN AFTER THE SPECIFIED DELAY.
# IT STARTS POLLING FROM THE SPECIFIED BLOCK AND CHECKS FOR ANY TRANSACTION HAVING MESSAGE DATA. IT EXTRACTS THE MESSAGE DATA
# IN A SEPARATE OUTPUT FILE  
# IT KEEPS POLLING FOR ANY NEW BLOCKS GETTING ADDED IN THE CHAIN AND FOR TRANSACTIONS THEREIN
# Date# 9-Sep-2018
#
#----------------------------------------------------------------------------------------------------------------------------


import os
import sys
import time
import poller_poll_chain
from datetime import datetime
import ConfigParser

config = ConfigParser.ConfigParser()
#Check If Configuration File Exists Else An Exception
try:
	cfile_path = sys.argv[1]
	with open(cfile_path) as cfile:
		config.readfp(cfile)
		delay=config.getfloat('setval','delay') 
		url=config.get('setval','url')
		uid=config.get('setval','uid')
		pwd=config.get('setval','pwd')
		start_block_no=config.getint('setval','start_block_no')
		trx_file_path=config.get('setval','trx_file_path')
		cntrl_file_path=config.get('setval','cntrl_file_path')
		asset_name=config.get('setval','asset_classifier')

		#The Output File For Transaction & Message Details
		trx_file_name = trx_file_path
		#Opening The Transaction File
		target1 = open(trx_file_name, 'w')

		#The Control File For Reference Details
		cntrl_file_name = cntrl_file_path
		#Opening The Control File
		target2 = open(cntrl_file_name, 'w')

		start = time.time()
		block_no = 0			#Initialized To Zeros

		loop_cnt = 1
		while loop_cnt < 2:
			time.sleep(delay)
			##Get The Next Block No.
			if block_no == 0:
				block_no = start_block_no
			else:
				block_no = block_no + 1
			
			##Call The Chain To Identify Block Hash Of The Block Height
			block_hash = poller_poll_chain.mchain_getblockhash(url, uid, pwd, block_no)
			if str(block_hash) == '--NoBlock--':
				print 'Polling for Block No.: ' + str(block_no)
				block_no = block_no - 1
			else:	
				if block_hash != 'E0101':
					##Get All Latest Transaction In The Block.
					latest_block_trx = poller_poll_chain.mchain_getblock(url, uid, pwd, block_hash)
					tx_cnt = len(latest_block_trx)
					if tx_cnt > 0:
						for cnt in range(tx_cnt):
							
							#Extract The Transaction Detail
							tid = latest_block_trx[cnt]
							t_asset_name, t_asset_data, t_asset_time = poller_poll_chain.mchain_getrawtransaction(url, uid, pwd, tid)
							
							print '++[Block No. - ' + str(block_no) + '] [Block Hash - ' + str(block_hash) + '] [Trx Cnt - ' + str(tx_cnt) + '] [Trx Id] - ' + str(tid) +']'
							
							#Write The Trx/Mssg Detail To Transaction File
							if t_asset_data == '':
								r=0 #Do Nothing
							else:
								if t_asset_name == asset_name:
									data = t_asset_data
									if len(data) != 0:
										ascii_data = data[0].decode("hex")	
									else:
										ascii_data = ''
																		
									line1 = 'Hex Data       : ' + str(t_asset_data)
									target1.write(line1)
									target1.write("\n")
									
									line1 = 'Ascii Data     : ' + str(ascii_data)
									target1.write(line1)
									target1.write("\n")

									line1 = 'Asset Name     : ' + str(t_asset_name) 
									target1.write(line1)
									target1.write("\n")
									
									line1 = 'Data Trx. Time : ' + str(datetime.utcfromtimestamp(t_asset_time).strftime('%Y-%m-%d %H:%M:%S'))
									target1.write(line1)
									target1.write("\n")
								
									line1 = '==================='
									target1.write(line1)
									target1.write("\n")
								
									line2 = 'Block No. : ' + str(block_no) 
									target2.write(line2)
									target2.write("\n")
									
									line2 = 'Block Hash: ' + str(block_hash) 
									target2.write(line2)
									target2.write("\n")
									
									line2 = 'Trx. Id   : ' + str(tid)
									target2.write(line2)
									target2.write("\n")

									line2 = '==================='
									target2.write(line2)
									target2.write("\n")

									
							cnt = cnt + 1
				else:
					break
				
		#Close The Transaction File	
		target1.close()

		#Close The Control File	
		target2.close()

except Exception as e:
	print ('File Not Found/Specify Correct Path for Configuration File (INI) file/Configuration File Content Incorrect')
	print (str(e))