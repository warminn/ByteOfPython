# -*-- coding: UTF-8 --*-
#!/usr/bin/python
# Filename: use_logging.py

import os, platform, logging

if platform.platform().startswith('Windows'):
	logging_file = os.path.join(os.getenv('HOMEDRIVE'),
							'test.log')
else:
	logging_file = os.path.join(os.getenv('HOME'),'test.log')

logging.basicConfig(
				level = logging.DEBUG,
				format = '%(asctime)s : %(levelname)s : %(message)s',
				filename = logging_file,
				filemode = 'w',
				)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")
