import tweepy
from utils.exception import format_exception
from constants.constants import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import logging
logging.basicConfig(filename='pandemic-watch.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG
                   )

logger=logging.getLogger(__name__)


def upload_post():
    '''

    :return:
    '''
    return


def upload_img_post(img_path):
    '''

    :param img_path:
    :return:
    '''
    try:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        status = "Do not go gentle into that good night,\n " \
                 "Old age should burn and rave at close of day,\n" \
                 "Rage rage against the dying of the light."

        image = img_path
        logging.info(image)
        logging.info(status)
        api.update_with_media(image, status)

        return True
    except Exception as e:
        return format_exception(e)