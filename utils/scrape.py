import requests
from constants.constants import DATA_URL
from utils.exception import format_exception

import logging
logging.basicConfig(filename='pandemic-watch.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG
                   )

logger=logging.getLogger(__name__)


def get_news():
    '''

    :return:
    '''
    try:
        r = requests.get(DATA_URL)
        response = r.json()
        logging.info(response)
        previous_recoveries = response['cases_time_series'][-1]['dailyrecovered']
        previous_date = response['cases_time_series'][-1]['date']
        return previous_recoveries, previous_date
    except Exception as e:
        return format_exception(e)
