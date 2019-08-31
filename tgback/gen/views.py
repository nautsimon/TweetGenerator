from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings

import tweepy as tweepy
import re
import random
import sys
from collections import defaultdict, Counter

import os
import logging

# opsec on dum
consumer_key = 'ZVf8uKCcoFzcsTzN6sVXyTnbN'
consumer_secret = 'duWsSe95grFNt9gDA0mO9rtU6i6ds7Levk5OxNlXnWSN9lGLDd'
access_token = '3849389602-cAcwvTcPyDrTec1nMfYZDkDrqGPxRCgX6reSDpH'
access_token_secret = 'GFwja2G0fm0BLRDq5EP8Lpl2IOLT5AkRTrndYTa7PYPfz'

# tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
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
    print(markovOutput[markovOutput.index(' ')+1:markovOutput.rindex(' ')])
    return(markovOutput[markovOutput.index(' ')+1:markovOutput.rindex(' ')])


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


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def generate(request, format=None):
    if request.method == 'POST':
        print(request.data)
        handle = "@"+str(request.data)[11:-2]
        try:
            u = api.get_user(handle)
            print(u.id_str)
            print(u.screen_name)
            epic = getTweets(handle)
            return Response(epic, status=status.HTTP_201_CREATED)
        except:
            return Response("invalid username", status=status.HTTP_400_BAD_REQUEST)
