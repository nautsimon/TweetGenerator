from rest_framework import viewsets
from generates.models import Generate
from .serializers import GenerateSerializer
from collections import defaultdict, Counter
import tweepy as tweepy
import re
import random
import sys



consumer_key = 'ZVf8uKCcoFzcsTzN6sVXyTnbN'
consumer_secret = 'duWsSe95grFNt9gDA0mO9rtU6i6ds7Levk5OxNlXnWSN9lGLDd'
access_token = '3849389602-cAcwvTcPyDrTec1nMfYZDkDrqGPxRCgX6reSDpH'
access_token_secret = 'GFwja2G0fm0BLRDq5EP8Lpl2IOLT5AkRTrndYTa7PYPfz'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)


def genTensor(data):
    # text = data
    # # length of text is the number of characters in it
    # print('Length of text: {} characters'.format(len(text)))
    # # Take a look at the first 250 characters in text
    # print(text[:250])
    # # The unique characters in the file
    # vocab = sorted(set(text))
    # print('{} unique characters'.format(len(vocab)))
    # # Creating a mapping from unique characters to indices
    # char2idx = {u: i for i, u in enumerate(vocab)}
    # idx2char = np.array(vocab)

    # text_as_int = np.array([char2idx[c] for c in text])
    # print('{')
    # for char, _ in zip(char2idx, range(20)):
    #     print('  {:4s}: {:3d},'.format(repr(char), char2idx[char]))
    # print('  ...\n}')
    # # Show how the first 13 characters from the text are mapped to integers
    # print(
    #     '{} ---- characters mapped to int ---- > {}'.format(repr(text[:13]), text_as_int[:13]))
    # # The maximum length sentence we want for a single input in characters
    # seq_length = 100
    # examples_per_epoch = len(text)//seq_length

    # # Create training examples / targets
    # char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

    # for i in char_dataset.take(5):
    #     print(idx2char[i.numpy()])
    # sequences = char_dataset.batch(seq_length+1, drop_remainder=True)

    # for item in sequences.take(5):
    #     print(repr(''.join(idx2char[item.numpy()])))

    # def split_input_target(chunk):
    #     input_text = chunk[:-1]
    #     target_text = chunk[1:]
    #     return input_text, target_text

    # dataset = sequences.map(split_input_target)
    # for input_example, target_example in dataset.take(1):
    #     print('Input data: ', repr(''.join(idx2char[input_example.numpy()])))
    #     print('Target data:', repr(''.join(idx2char[target_example.numpy()])))
    # for i, (input_idx, target_idx) in enumerate(zip(input_example[:5], target_example[:5])):
    #     print("Step {:4d}".format(i))
    #     print("  input: {} ({:s})".format(
    #         input_idx, repr(idx2char[input_idx])))
    #     print("  expected output: {} ({:s})".format(
    #         target_idx, repr(idx2char[target_idx])))

    # # Batch size
    # BATCH_SIZE = 64

    # # Buffer size to shuffle the dataset
    # # (TF data is designed to work with possibly infinite sequences,
    # # so it doesn't attempt to shuffle the entire sequence in memory. Instead,
    # # it maintains a buffer in which it shuffles elements).
    # BUFFER_SIZE = 10000

    # dataset = dataset.shuffle(BUFFER_SIZE).batch(
    #     BATCH_SIZE, drop_remainder=True)

    # dataset
    # # Length of the vocabulary in chars
    # vocab_size = len(vocab)

    # # The embedding dimension
    # embedding_dim = 256

    # # Number of RNN units
    # rnn_units = 1024

    # def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    #     model = tf.keras.Sequential([
    #         tf.keras.layers.Embedding(vocab_size, embedding_dim,
    #                                   batch_input_shape=[batch_size, None]),
    #         tf.keras.layers.LSTM(rnn_units,
    #                              return_sequences=True,
    #                              stateful=True,
    #                              recurrent_initializer='glorot_uniform'),
    #         tf.keras.layers.Dense(vocab_size)
    #     ])
    #     return model

    # model = build_model(vocab_size = len(vocab),embedding_dim=embedding_dim,rnn_units=rnn_units,batch_size=BATCH_SIZE)

    # for input_example_batch, target_example_batch in dataset.take(1):
    #     example_batch_predictions = model(input_example_batch)
    #     print(example_batch_predictions.shape, "# (batch_size, sequence_length, vocab_size)")
    # model.summary()

    # sampled_indices = tf.random.categorical(example_batch_predictions[0], num_samples=1)
    # sampled_indices = tf.squeeze(sampled_indices,axis=-1).numpy()
    # sampled_indices
    # print("Input: \n", repr("".join(idx2char[input_example_batch[0]])))
    # print()
    # print("Next Char Predictions: \n", repr("".join(idx2char[sampled_indices ])))

    # def loss(labels, logits):
    #     return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

    # example_batch_loss  = loss(target_example_batch, example_batch_predictions)
    # print("Prediction shape: ", example_batch_predictions.shape, " # (batch_size, sequence_length, vocab_size)")
    # print("scalar_loss:      ", example_batch_loss.numpy().mean())
    # model.compile(optimizer='adam', loss=loss)
    # # Directory where the checkpoints will be saved
    # checkpoint_dir = './training_checkpoints'
    # # Name of the checkpoint files
    # checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

    # checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    #     filepath=checkpoint_prefix,
    #     save_weights_only=True)

    # EPOCHS=10
    # history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])
    # tf.train.latest_checkpoint(checkpoint_dir)
    # model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)

    # model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

    # model.build(tf.TensorShape([1, None]))
    # model.summary()
# -------------------------------------------
    text = data
    print('Length of text: {} characters'.format(len(text)))
    # Take a look at the first 250 characters in text
    print(text[:250])
    # The unique characters in the file
    vocab = sorted(set(text))
    print ('{} unique characters'.format(len(vocab)))
    # Creating a mapping from unique characters to indices
    char2idx = {u:i for i, u in enumerate(vocab)}
    idx2char = np.array(vocab)

    text_as_int = np.array([char2idx[c] for c in text])
    print('{')
    for char,_ in zip(char2idx, range(20)):
        print('  {:4s}: {:3d},'.format(repr(char), char2idx[char]))
    print('  ...\n}')
    # Show how the first 13 characters from the text are mapped to integers
    print ('{} ---- characters mapped to int ---- > {}'.format(repr(text[:13]), text_as_int[:13]))
    # The maximum length sentence we want for a single input in characters
    seq_length = 100
    examples_per_epoch = len(text)//seq_length

    # Create training examples / targets
    char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

    for i in char_dataset.take(5):
        print(idx2char[i.numpy()])
    
    sequences = char_dataset.batch(seq_length+1, drop_remainder=True)

    for item in sequences.take(5):
        print(repr(''.join(idx2char[item.numpy()])))


    def split_input_target(chunk):
        input_text = chunk[:-1]
        target_text = chunk[1:]
        return input_text, target_text

    dataset = sequences.map(split_input_target)

    for input_example, target_example in  dataset.take(1):
        print ('Input data: ', repr(''.join(idx2char[input_example.numpy()])))
        print ('Target data:', repr(''.join(idx2char[target_example.numpy()])))

    for i, (input_idx, target_idx) in enumerate(zip(input_example[:5], target_example[:5])):
        print("Step {:4d}".format(i))
        print("  input: {} ({:s})".format(input_idx, repr(idx2char[input_idx])))
        print("  expected output: {} ({:s})".format(target_idx, repr(idx2char[target_idx])))
    # Batch size
    BATCH_SIZE = 64
    steps_per_epoch = examples_per_epoch//BATCH_SIZE

    # Buffer size to shuffle the dataset
    # (TF data is designed to work with possibly infinite sequences,
    # so it doesn't attempt to shuffle the entire sequence in memory. Instead,
    # it maintains a buffer in which it shuffles elements).
    BUFFER_SIZE = 10000

    dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

    dataset
    # Length of the vocabulary in chars
    vocab_size = len(vocab)

    # The embedding dimension
    embedding_dim = 256

    # Number of RNN units
    rnn_units = 1024
    if tf.test.is_gpu_available():
        rnn = tf.keras.layers.CuDNNGRU
    else:
        import functools
        rnn = functools.partial(
            tf.keras.layers.GRU, recurrent_activation='sigmoid')
    def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
        model = tf.keras.Sequential([tf.keras.layers.Embedding(vocab_size, embedding_dim,
                                batch_input_shape=[batch_size, None]),rnn(rnn_units,return_sequences=True,recurrent_initializer='glorot_uniform',stateful=True),tf.keras.layers.Dense(vocab_size)
        ])
        return model
    model = build_model(vocab_size = len(vocab),embedding_dim=embedding_dim, rnn_units=rnn_units,batch_size=BATCH_SIZE)
    for input_example_batch, target_example_batch in dataset.take(1):
        example_batch_predictions = model(input_example_batch)
        print(example_batch_predictions.shape, "# (batch_size, sequence_length, vocab_size)")
    model.summary()
    sampled_indices = tf.random.categorical(example_batch_predictions[0], num_samples=1)
    sampled_indices = tf.squeeze(sampled_indices,axis=-1).numpy()
    sampled_indices
    print("Input: \n", repr("".join(idx2char[input_example_batch[0]])))
    print()
    print("Next Char Predictions: \n", repr("".join(idx2char[sampled_indices ])))
    
    
    def loss(labels, logits):
        return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

    example_batch_loss  = loss(target_example_batch, example_batch_predictions)
    print("Prediction shape: ", example_batch_predictions.shape, " # (batch_size, sequence_length, vocab_size)")
    print("scalar_loss:      ", example_batch_loss.numpy().mean())
    model.compile(optimizer = tf.train.AdamOptimizer(),loss = loss)
    # Directory where the checkpoints will be saved
    checkpoint_dir = './training_checkpoints'
    # Name of the checkpoint files
    checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

    checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_prefix,save_weights_only=True)
    
    
    EPOCHS=100


    # train
    history = model.fit(dataset.repeat(), epochs=EPOCHS, steps_per_epoch=steps_per_epoch,callbacks=[checkpoint_callback])
    tf.train.latest_checkpoint(checkpoint_dir)
    model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)

    model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

    model.build(tf.TensorShape([1, None]))
    model.summary()

#ggegennen----
    def generate_text(model, start_string):
        # Evaluation step (generating text using the learned model)

        # Number of characters to generate
        num_generate = 1000

        # Converting our start string to numbers (vectorizing)
        input_eval = [char2idx[s] for s in start_string]
        input_eval = tf.expand_dims(input_eval, 0)

        # Empty string to store our results
        text_generated = []

        # Low temperatures results in more predictable text.
        # Higher temperatures results in more surprising text.
        # Experiment to find the best setting.
        temperature = 1.0

        # Here batch size == 1
        model.reset_states()
        for i in range(num_generate):
            predictions = model(input_eval)
            # remove the batch dimension
            predictions = tf.squeeze(predictions, 0)

            # using a multinomial distribution to predict the word returned by the model
            predictions = predictions / temperature
            predicted_id = tf.multinomial(predictions, num_samples=1)[-1,0].numpy()

            # We pass the predicted word as the next input to the model
            # along with the previous hidden state
            input_eval = tf.expand_dims([predicted_id], 0)

            text_generated.append(idx2char[predicted_id])

        return (start_string + ''.join(text_generated))
    print(generate_text(model, start_string=u"g"))
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
    genTensor(outputList)


class GenerateViewSet(viewsets.ModelViewSet):
    serializer_class = GenerateSerializer
    queryset = Generate.objects.all()
    getTweets('@largeeggie')


# from rest_framework.generics  i mp ort (
#     ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView)


# class GenerateListView(ListAPIView):
#     queryset = Generate.objects.all()
#     serializer_class = GenerateSerializer


# class GenerateDetailView(RetrieveAPIView):
#     queryset = Generate.objects.all()
#     serializer_class = GenerateSerializer


# class GenerateCreateView(CreateAPIView):
#     queryset = Generate.objects.all()
#     serializer_class = GenerateSerializer


# class GenerateUpdateView(UpdateAPIView):
#     queryset = Generate.objects.all()
#     serializer_class = GenerateSerializer


# class GenerateDeleteView(DestroyAPIView):
#     queryset = Generate.objects.all()
#     serializer_class = GenerateSerializer
