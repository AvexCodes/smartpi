import webbrowser
import random as r
import os

from mpyg321.mpyg321 import MPyg321Player
player = MPyg321Player()

from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    #os.system('mpg321 voice.mp3 &')
    player.play_song("voice.mp3")

def cleanTerm(inp, x):
    """
        Remove unwanted text from list, to maintain 100% accuracry of what user invoked
    """
    print(x)
    inp.pop(0)
    for i in range(x):
        inp.pop(0)
    
    return inp

def google(inp, x):
    jj = ' '
    inp = cleanTerm(inp, x)
    resp = ["Condsider it done!", "Furfilling request now!", "On it!", f"Googling {jj.join(inp)}"]
    choice = r.choice(resp)
    speak(choice)
    print(choice)
    joiner = '+'
    url = "https://google.com/search?q=" + joiner.join(inp)
    webbrowser.open(url)
    
def youtube(inp):
    pass  