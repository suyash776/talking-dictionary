# main.py
import speech_recognition as rec
from PyDictionary import PyDictionary
import helper
import warnings

def warn(*args, **kwargs):
    pass

warnings.warn = warn

################  Opening Greetings###############
helper.announce('Hello this is a python verbal dictionary')

##################################################

####Initilize Variables
dictionary=PyDictionary()
run=True

while (run):
    helper.announce('Please say the word you want the meaning of')
    audio=helper.listen()

    try:
        heard_word=helper.recognize(audio)
        meaning=dictionary.meaning(heard_word)
        helper.announce('The word I heard was '+ heard_word)

        if meaning is None:
            helper.announce('Sorry I could not find the meaning of ' + heard_word)
            helper.announce('Lets try again.')
            continue

        for speech in meaning:
            if(len(meaning[speech])==1):
                helper.announce('I found '+ str(len(meaning[speech]))+ ' meaning that is '+speech)
                helper.announce('The top meaning I found is ')
                helper.announce (str(meaning[speech]))
            else:
                helper.announce('I found '+ str(len(meaning[speech]))+ ' meanings that are '+speech+'s')
                num=2
                helper.announce('Here are the top '+str(num)+' meanings that are '+speech+'s for '+heard_word)
                for index in range(num):
                    helper.announce('Meaning number '+str(index+1)+' is ')
                    helper.announce (str(meaning[speech][index]))


    except rec.UnknownValueError:
        helper.announce('Sorry, I could not understand the audio.')

    except rec.RequestError as e:
        helper.announce('Sorry, I could not understand the audio.')

    helper.announce('Do you want to try another word?')
    try:
        audio=helper.listen()
        answer=helper.recognize(audio)

        if(answer=='no'):
            run=False
    except rec.UnknownValueError:
        helper.announce('Sorry, I could not understand audio.')
helper.announce('Thank you for using the python verbal dictionary. ')
helper.announce('Have a good day ')
