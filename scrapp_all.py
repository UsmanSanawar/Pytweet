import twint
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime as dt
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime


now = datetime.datetime.now()
# usernames = open("user.txt", "r+")
# for user in usernames:
	# if user != "":
user= 'John__Tennant'
user = user.replace('\n','')
# userDetail = user.split(",")
# username = userDetail[0]
# since = userDetail[1]
# until =userDetail[2]
# screnshots = userDetail[3]
# csvname = username + "-" + now.strftime("%Y-%m-%d %H:%M:%S") + ".csv"
# csvname = csvname.replace(':','-').replace(' ','')
path= "/media/hamza/1EB6FA79B6FA50AF/TPI/twitter/finalwithgit/githubusmanbahi/Pytweet/CSV/"
csvname= path + user + '.csv'
c = twint.Config()
c.Profile_full = True
c.Retweets = True
c.Username = user
c.Store_csv = True
# c.Since=since
# c.Until=until
c.Output = csvname
twint.run.Search(c)
if os.path.isfile(csvname):
    data  = pd.read_csv(csvname)
    data  = data.drop(['conversation_id', 'created_at','username','name','place','replies_count','retweets_count','likes_count','video','near','geo','source','user_rt_id','user_rt','retweet_id','retweet_date','translate','trans_src','trans_dest','mentions','photos','cashtags','quote_url','reply_to','user_id','hashtags','urls','timezone'], axis=1)

    data['date'] = data['date'].apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d').date())
    data['Day'] = [d.day for d in data['date']]
    data['Month'] = [d.month for d in data['date']]
    data['Year'] = [d.year for d in data['date']]

    data.to_csv(csvname,sep=',')
