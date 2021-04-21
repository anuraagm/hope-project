from PIL import Image, ImageDraw, ImageFont
from utils.exception import format_exception
from constants.constants import IMAGE_PATH, FONT_PATH
import os
import logging
logging.basicConfig(filename='pandemic-watch.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG
                   )

logger=logging.getLogger(__name__)


def create_post(data, date):
    '''

    :param data:
    :param date:
    :return:
    '''
    try:
        img = Image.new('RGB', (1080,1080), 'white')
        fnt = ImageFont.truetype(os.path.abspath(os.path.join(FONT_PATH,"OpenSans-Bold.ttf")), 50)
        img_name = str(date+".png").replace(" ","_")
        im_path = os.path.abspath(IMAGE_PATH)
        if not os.path.exists(im_path):
            os.mkdir(os.path.abspath(os.path.join(".","data")))
            os.mkdir(os.path.abspath(os.path.join(".", "data","posts")))
        for f in os.listdir(os.path.abspath(IMAGE_PATH)):
            os.remove(os.path.abspath(os.path.join(IMAGE_PATH, f)))
        img_path = os.path.abspath(os.path.join(IMAGE_PATH,img_name))
        logging.info(img_path)
        d = ImageDraw.Draw(img)
        d.text((290, 370), "On the "+date+"\n", font=fnt, fill=(0, 0, 0))
        d.text((210, 460), "The Doctors of India saved\n", font=fnt, fill=(0, 0, 0))
        d.text((350, 540), data+" people\n", font=fnt, fill=(0, 225, 0))
        d.text((290, 620), "From the pandemic\n", font=fnt, fill=(0, 0, 0))
        img.save(img_path)
        return img_path
    except Exception as e:
        return format_exception(e)
