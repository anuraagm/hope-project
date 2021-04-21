import os
import keyring
DATA_URL = 'https://api.covid19india.org/data.json'
IMAGE_PATH = os.path.join("data", "posts")
FONT_PATH = os.path.join("constants", "fonts")
with open('tfile.txt') as f:
    word = f.read()
    API_KEY = keyring.get_password('API_KEY',word)
    API_SECRET_KEY = keyring.get_password('API_SECRET_KEY',word)
    ACCESS_TOKEN = keyring.get_password('ACCESS_TOKEN',word)
    ACCESS_TOKEN_SECRET = keyring.get_password('ACCESS_TOKEN_SECRET',word)

FEED_LIST = [
                "https://news.google.com/rss?q=india+coronavirus&hl=en",
                "https://news.google.com/rss?q=india+covid&hl=en",
                "https://news.google.com/rss?q=covishield&hl=en",
                "https://news.google.com/rss?q=covaxin&hl=en"
            ]

NSW = ["rising", "cases", "deaths", "death", "dead", "died", "deadly", "infected", "shortage", "wave", "kill", "killed",
       "killer", "blood", "bloody", "rise", "surge", "lack", "suffer", "suffering", "spike", "worst", "worse", "sad",
       "slack", "slackened", "slackening", "useless", "absurd", "hopeless", "pointless", "shameless", "unfortunate",
       "misfortune", "terrible", "terrifying", "fear", "feared", "fearful","trigger","triggered","triggering", "fail",
       "failed", "failure", "poor", "poverty", "modi", "gandhi", "PM", "politics", "political", "opposition", "saddening",
       "worsening", "media", "party", "election", "bad", "crash", "shambles", "apocalypse", "minister", "doomsday", "doom",
       "negative", "worrying","war","strain","shortage","dries","short","strained","symptoms","symptomatic","asymptomatic",
       "fight","fighting","turmoil","conflict","issue","issues","crisis","worsen","army","Army", "cases", "Cases"]
