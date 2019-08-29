from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gen.models import Gen
from gen.serializers import GenSerializer



# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
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
    for i in range(200):
        out.extend(random.choices(list(model[state]), model[state].values()))
        state = state[1:] + out[-1]
    markovOutput = ''.join(out)
    print(markovOutput[markovOutput.index(' ')+1:])


def getTweets(handle):
    # initialize a list to hold all the tweepy Tweets
    alltweets = []
    output = []
    outputList = ''
    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(
        screen_name=handle, count=200, tweet_mode="extended")
    # save most recent tweets
    alltweets.extend(new_tweets)
    # print(alltweets)
# ----------------------------------------------------
    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

   # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before" + str(oldest))

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(
            screen_name=handle, count=200, tweet_mode="extended",  max_id=oldest)

        # print(new_tweets)
        # if ('RT @' not in new_tweets.text):
        alltweets.extend(new_tweets)

        # save most recent tweet s

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print(len(alltweets))
# ----------------------------------------------------
    for tweet in alltweets:
        if (not tweet.full_text.startswith('RT')):
            # print(tweet.full_text.encode(
            #     "utf-8"))
            output.append(str(tweet.full_text))
            outputList = outputList + ' ' + (str(tweet.full_text))
            outputList = re.sub(
                r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', outputList)
    # for count, word in enumerate(outputList, 0):
    #     if ('https://t.co/' in word):
    #         outputList[count]

    print(output)
    print(outputList)
    genMarkov(outputList)
    # genTensor(outputList)


class GenerateViewSet(viewsets.ModelViewSet):
    serializer_class = GenerateSerializer
    queryset = Generate.objects.all()
    getTweets('@largeeggie')

@api_view(['GET', 'POST'])
def gen_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        gen = Gen.objects.all()
        serializer = GenSerializer(gen, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = GenSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            epic = str(request.data) + "fuck"

            return Response(epic, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def gen_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        gen = Gen.objects.get(pk=pk)
    except Gen.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GenSerializer(gen)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GenSerializer(gen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cry = "cry"
            return Response(cry)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        gen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from gen.models import Gen
# from gen.serializers import GenSerializer


# @csrf_exempt
# def gen_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         gen = Gen.objects.all()
#         serializer = GenSerializer(gen, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         gen = GenSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def gen_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         gen = Gen.objects.get(pk=pk)
#     except Gen.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = GenSerializer(gen)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = GenSerializer(gen, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         gen.delete()
#         return HttpResponse(status=204)
