import json
import re
import random as r
import commands
import os
from gtts import gTTS

with open("chat.json") as file:
    data = json.load(file)
    
def inp():
    return str(input("> "))

intents = len(data["intents"])

resp = ""
command = ""
globalx = 0

def check(inpt: list):
     for x in range(0, len(inpt)):
        for i in range(0, intents):
            if inpt[x] in data["intents"][i]["patterns"]:
                return data["intents"][i]["response"] + [x]
            else:
                pass
            
        
        
        
def execute(cn, inp, ctxnum):
    return {
        'GOOGLE':commands.google(inp, ctxnum),
        'YOUTUBE':commands.youtube(inp),
        }.get(cn)

while 1:
    inpt = re.sub("[^\w]", " ",  inp().lower()).split()
    #print(inpt)
    c = check(inpt)
    print(c[1])
    #print("kys fattie")
    
    #try:
    if c[0][0] == "COMMAND":
            #print(c[0][1])
            execute(str(c[0][1]), inpt, c[1])
    elif c[0][0] == "OUTPUT":
            #print(gX)
            choice = r.choice(c[0][1])
            commands.speak(choice)
            print(choice)
           
            #print(r.choice(c[0][1]))
            #print(r.choice[1])
    elif c[0][0] == "ERR":
            print(r.choice(c[0][1]))
    #except Exception as e:
     #   print(e)
    
    
   