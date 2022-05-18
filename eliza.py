# -*- coding: utf-8 -*-
#Eliza Assignment
__author__ = "Zamar Iqbal"

import re, random

questions = ["How are you doing?", "How's your day?", "How are you feeling?", 
             "How's your day going?"]
askMore = ["Tell me more.", "Please share more.", "I'm here to listen.", 
           "Go on.", "Explain?", "How does that make you feel?"]
notSure = ["Hmm, that's quite interesting.", "Quite a conundrum.", 
           "I'd like to think I'm catching your drift.", "Huh."]

fineResponse = ["That's good to hear.", "Good, good.", "Great."]
happyResponse = ["Amazing!", "Wow!", "Awesome!", "Incredible!", 
                 "I'm so happy for you!"]
sadResponse = ["Oh no..", "Ahh..", "It's okay.", "I'm here to listen."]
madResponse = ["Center yourself.", "Take a deep breath.", "Relax.", "Calm down"]

greeting = "Hi, I'm Eliza. Tell me how you're feeling!\nIf you want to stop talking, say bye.\nWhat's your name?\n"
name = input(greeting)
print("Hello " + name + "!")

random.shuffle(questions)
print("\nEliza: " + questions[0] + "\n")

while(True):
        resp = input("")

        #User is feeling OK
        if re.search(r'okay|ok|fine|alright|decent|i.*m.*well', resp, flags=re.IGNORECASE):
            random.shuffle(askMore)
            random.shuffle(fineResponse)
            print("Eliza: " + fineResponse[0] + " I'm glad you're feeling OK, " + name + ". " + askMore[0])

        #User is feeling happy
        elif re.search(r'happy|good|amazing|swell|ecstatic|great|fantastic|i.*m.*super', resp, flags=re.IGNORECASE):
            random.shuffle(askMore)
            random.shuffle(happyResponse)
            print("Eliza: " + happyResponse[0] + " I'm glad you're feeling happy, " + name + "! " + askMore[0])

        #User is feeling sad
        elif re.search(r'sad|depressed|i.*m.*down|unhappy|not.*good|not.*great|i.*bad|melancholy', resp, flags=re.IGNORECASE):
            random.shuffle(askMore)
            random.shuffle(sadResponse)
            print("Eliza: " + sadResponse[0] + " I'm sorry you're feeling sad, " + name + "... " + askMore[0])
            
        #User is feeling mad
        elif re.search(r'mad|angry|i.*m.*upset|pissed.*off|enraged', resp, flags=re.IGNORECASE):
            random.shuffle(askMore)
            random.shuffle(madResponse)
            print("Eliza: " + madResponse[0] + " It's okay to feel angry, you need to let it out in a healthy way " + name + ". " + askMore[0])

        #User mentions family/friend
        elif re.search(r'mom|mother|dad|father|brother|bro|sister|sis|son|daughter|uncle|aunt|wife|husband|partner|cousin|friend', resp, flags=re.IGNORECASE):
            fam = re.search(r'mom|mother|dad|father|brother|bro|sister|sis|son|daughter|uncle|aunt|wife|husband|partner|cousin|friend', resp, flags=re.IGNORECASE).group()
            random.shuffle(askMore)
            print("Eliza: I understand that your " + fam + " makes you feel a certain way.\n" + askMore[0])

        #User uses past tense verb
        elif re.search(r'(\w+)ed\b',resp, flags = re.IGNORECASE):
            verb = re.search(r'(\w+)ed\b',resp, flags = re.IGNORECASE).group()
            random.shuffle(askMore)
            print("Why did you " + verb + "? " + askMore[0])
            
        #Exit chat
        elif re.search(r'bye', resp, flags=re.IGNORECASE):
            print("Eliza: " + "bye!")
            break;

        #All other cases
        else:
            random.shuffle(notSure)
            random.shuffle(askMore)
            print("Eliza: " + notSure[0] + " " + askMore[0])
