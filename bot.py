import tweepy
import time

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)


#user = api.get_user("MikePawlica29")
#print(user.screen_name)
#print(user.followers_count)




def attention(tweet):
    alert = " DAWG ALERT!!! : "
    ann = []
    
    for i in  tweet:
        ann.append(i.lower())

    return ''.join([alert] + ann)

def smallboy(twittname):
    user = api.get_user(twittname)
    tweets = api.user_timeline(screen_name=user.screen_name)

    if tweets[0].text[0:2] != "RT":
        api.update_with_media("{}.jpg".format(twittname),"@"+twittname+attention(tweets[0].text),tweets[0].id)



def bigboy(twittname):
    user = api.get_user(twittname)
    tweets = api.user_timeline(screen_name=user.screen_name)

    for tweet in tweets:
            if tweet.text[0:2] != "RT":
                api.update_with_media("{}.jpg".format(twittname),"@"+twittname+attention(tweet.text),tweet.id)
                time.sleep(5)


smallboy("bloopers217")
#bigboy("MikePawlica29")
#bigboy("RealDealCamill")
#bigboy("O_Jak_Tam")