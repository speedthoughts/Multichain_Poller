MultiChain Poller keeps on polling MultiChain for blocks and any new block. Further, it identifies asset-based transactions in the blocks as per the asset name you have provided in the configuration file and extracts the data information (in Hex format and converts to ASCII) 
This software is written with an inquisitiveness to understand Multichain behavior and more specifically to make use of Blockchain as transaction backbone with data processing occurring out of Multichain. 
MultiChain Poller is still under development, so it may break!!!

System Requirements
-	Two windows machines which act as two Multichain nodes. Refer the Multichain installable available at - https://www.multichain.com/download-install/ and the documentation to create and connect to a chain available at - https://www.multichain.com/developers/creating-connecting/  
-	Each of the machine connected to internet.
-	Each windows machine needs to have:
o	Python 2.x (available at - https://www.python.org/downloads/)
o	Multichain version 1.0.5
-	Asset created on Multichain with some transactions done using those. Preferable to have message data while doing the asset transactions.

Installation, Configuration, Launch and Stop the Poller Program
Installation:
To install MultiChain Poller, download and copy the files to your respective folder structure. 
Configure: 
The bundled software provides two configuration files. One – ‘poller_config.ini’ file, which is an actual configuration file and other - ‘poller_config – sample.ini’ file which is a sample configuration file provided for reference. Refer the sample configuration file and make your own configuration file. Following changes are needed:
- ‘delay’ parameter	Modify the value to specify the delay for polling in seconds. The poller will poll the chain for blocks or new blocks after the specified delay.
- ‘url’ parameter	Modify the value to specify the IP and Port to access the Multichain. For example - http://localhost:7565 or http:// 102.158.10.102:7566
- ‘uid’ parameter	Modify the value to provide user-id of your Multichain. You can find the user-id in multichain.conf file located at %APPDATA%\MultiChain\[your-chain name] as against rpcuser
- ‘pwd’ parameter	Modify the value to provide password of your Multichain. You can find the password in multichain.conf file located at %APPDATA%\MultiChain\[your-chain name] as against rpcpassword
- ‘start_block_no’ parameter	Modify the value to specify the block number from where you intend to start polling your installed Multichain.
  -	Always provide a value either 1 or greater than 1 
- ‘trx_file_path’ parameter	Provide the file path for text file (.txt)
- ‘cntrl_file_path’ parameter	Provide the file path for text file (.txt)
- ‘asset_classifier’ parameter	Name of Asset issued on the Multichain, which you want to track using this poller.

You can store the config file anywhere you want and specify the path of this config file when you start the poller you can specify the location of this config file.

Launch: 
Use the following commands:
1.	Go to the directory, which contains the copied files. Let’s say this folder is ‘C:\multichain-poller’, then:
cd multichain-poller

2.	Launch multichain-poller.py program specifying the configuration file path as a parameter to multichain-poller.py. Let’s say configuration file path is C:\multichain-poller\poller_config.ini, then:
python multichain-poller C:\multichain-poller\poller_config.ini

The poller will connect to a local MultiChain node. Before configuring the poller, make sure you have a MultiChain blockchain up and running with asset-based transaction conducted on the Multichain.
Once the poller is started, look for output such as this on your windows command prompt:

- ++[Block No. - 1] [Block Hash - 005d134ad7547b4e0adcd9e615abecdbe085cb5341205668f4615265264177bc] [Trx Cnt - 1] [Trx Id] - 485ae3be1db4b9afb539dce7e2e004cf1c26c5898289661abfcaea6049f80c9a]
- ++[Block No. - 2] [Block Hash - 0059603bf64cecfe081529a25961d8dfe4ab5058fcb0a73056790f3780a4e508] [Trx Cnt - 1] [Trx Id] - 8b7767ba71a4d7eb3d0c1f1f8bebc048c4ee603edbdeeda3df5f3de989a01ec1]
- ...
- ...

You can check the transaction file and the control file for further details on the extracted asset based transactions by the poller. The transaction file will contain the output such as this: Hex Data, ASCII Data, Asset Name and Data Trx. Time for those transactions, which are asset based, and having message data. The control file contains the corresponding Block No, Block Hash, and Trx. Id for which asset-based message data has been identified. 

Stop the Poller
To stop the poller program, simply exit the command prompt window or use the cntrl-c command. 

Important Considerations
If there are too many blocks existing on your Multichain, then the poller program will take some time to read these blocks and write output to the transaction/control files. The time to read the blocks will increase with the number of blocks. 
The size of the transaction file/control file will tend to increase if there are too many blocks on the chain. This may affect the opening and/or other files I/O. 
The poller has been tested on - Windows 10 64-bit; Processor – Intel(R) Core(TM) i5 CPU @2.3GHz; RAM – 8GB AND on Multichain 1.0.5 AND on python 2.7.13. 

******
