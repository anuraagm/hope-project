import os
import sys
import traceback
import json

import logging
logging.basicConfig(filename='pandemic-watch.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG
                   )

logger=logging.getLogger(__name__)


def format_exception(e):
    '''

    :param e:
    :return:
    '''
    try:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        line = exc_tb.tb_lineno
        tb = sys.exc_info()[-1]
        stk = traceback.extract_tb(tb, 1)
        func_name = stk[0][2]
        message = "Error : "+ str(e) + "\n\t\t\t Filename: "+str(file)+"\n\t\t\t Line Number: "+str(line)\
                  +"\n\t\t\t In function: "+str(func_name)
        logging.error(message)
        json.dumps({"message":message+". Check the logs for more information.", "status":False})
    except Exception as e:
        logging.error(e)
