import tweepy
import time
import hn_n_lidovky
import irozhlas_seznam_ct24 

time_now = time.localtime()


#udaje
api_key = "Pdsf7rXNFc21I5goaSKoSk2LR"
api_secret = "cRiB0KTvsqeIgySpaEDVoPYUWDhgsLzQVgWYqlQbXfa6DkCUEj"

access_token = "1225452827662782464-gLkLSPlFPBdA4l3TzczDQh3ItnhDpH"
access_token_secret = "ahMq3oVlcPhLQZrqmtuQQ24yMUdKuK41c7abKLO4FiqyW"

#login
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)



def Tweet1():
	tweet1 = irozhlas_seznam_ct24.irozhlas() + "\n" + irozhlas_seznam_ct24.seznam() + "\n" + irozhlas_seznam_ct24.ct24()
	delka1 = len(tweet1)
	rozdil1 = 280 - delka1
	if rozdil1 < 0:
		novy_tweet1 = tweet1[:(rozdil1-3)] + "..." 
		api.update_status(novy_tweet1)
	else:	
		api.update_status(tweet1)
					

def Tweet2():
	tweet2 = hn_n_lidovky.HN() + "\n" + hn_n_lidovky.DenikN() + "\n" + hn_n_lidovky.Lidovky()
	delka2 = len(tweet2)
	rozdil2 = 280 - delka2
	if rozdil2 < 0:
		novy_tweet2 = tweet2[:(rozdil2-3)] + "..." 
		api.update_status(novy_tweet2)
	else:	
		api.update_status(tweet2)
						

if ((time.localtime()[3] >= 6) and (time.localtime()[3] <= 21)):
	try: 
		Tweet1()
	finally:
		Tweet2()
	time.sleep(10800)
else:
	time.sleep(1800)
	





"""
	(irozhlas_seznam_ct24.irozhlas())  
	(irozhlas_seznam_ct24.seznam())     
	(irozhlas_seznam_ct24.ct24())


	print (hn_n_lidovky.HN() + hn_n_lidovky.DenikN()  + hn_n_lidovky.Lidovky())
	time.sleep(10800)
"""

