from run import app
from flask import request, redirect
from utils.exception import format_exception
from utils.scrape import get_news
from utils.tweetimage import create_post
from utils.upload import upload_img_post
import json
import logging

logging.basicConfig(filename='pandemic-watch.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG
                   )

logger=logging.getLogger(__name__)


@app.route("/pandemic-watch/test",methods=['GET'])
def check_endpoint():
    '''

    :return:
    '''
    try:
        return json.dumps({"message":"App running on port 5005", "status":True})
    except Exception as e:
        return format_exception(e)


@app.route("/pandemic-watch/new",methods=['POST'])
def new_post():
    '''

    :return:
    '''
    try:
        data, date = get_news()
        img_path = create_post(data, date)
        status = upload_img_post(img_path)
        return json.dumps({"message":"Today's statistics", "recoveries":str(data), "date":date, "tweet_status":status,"status":True})
    except Exception as e:
        return format_exception(e)
