import json
import tweepy as tweepy
import re
import random
import sys
from collections import defaultdict, Counter

import os
import logging

# tweepy

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)




def genMarkov(data):
    STATE_LEN = 4
    model = defaultdict(Counter)
    print('Learning model...')
    for i in range(len(data) - STATE_LEN):
        state = data[i:i + STATE_LEN]
        next = data[i + STATE_LEN]
        model[state][next] += 1
    print('Sampling...')
    state = random.choice(list(model))
    out = list(state)
    for i in range(120):
        out.extend(random.choices(list(model[state]), model[state].values()))
        state = state[1:] + out[-1]
    markovOutput = ''.join(out)
    finalOut = markovOutput[markovOutput.index(' ')+1:markovOutput.rindex(' ')]
    print("mark", finalOut)
    return(finalOut)
    
def getTweets(handle):
    alltweets = []
    output = []
    outputList = ''
    new_tweets = api.user_timeline(
        screen_name=handle, count=200, tweet_mode="extended")
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    count = 0
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(
            screen_name=handle, count=200, tweet_mode="extended",  max_id=oldest)
        alltweets.extend(new_tweets)
        count = count + 1
        oldest = alltweets[-1].id - 1
        if (count > 2):
            break

        print(len(alltweets))
# ----------------------------------------------------
    for tweet in alltweets:
        if (not tweet.full_text.startswith('RT')):
            output.append(str(tweet.full_text))
            outputList = outputList + ' ' + (str(tweet.full_text))
            outputList = re.sub(
                r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', outputList)
    print(output)
    print(outputList)
    return genMarkov(outputList)



def lambda_handler(event, context):
    print(event['queryStringParameters']['user'])
    
    handle = "@"+str(event['queryStringParameters']['user'])
    print(handle)
    try:
        u = api.get_user(handle)
        print(u)
        print(u.id_str)
        print(u.screen_name)
        epic = getTweets(handle)
        return {
            'statusCode': 200,
            'body': json.dumps(epic)
        }
        #return Response(epic, status=status.HTTP_201_CREATED)
    except:
        return {
            'statusCode': 200,
            'body': json.dumps('fail')
        }
            
            
#def lambda_handler(event, context):
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }
    
