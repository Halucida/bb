from tensorflow.keras.utils import pad_sequences

from stop_words import get_stop_words

def Helist(sentence):
    untest = sentence.lower().split()
    united = [i for i in untest if i not in unlist]
    result = " ".join(united)
    return result

def Helpad(token, sentence, **helargs):
    temp = token.texts_to_sequences(sentence)
    result = pad_sequences(temp, **helargs)
    return result