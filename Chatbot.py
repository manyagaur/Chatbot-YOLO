import nltk
from nltk.chat.util import Chat, reflections
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?",
        ["I am a bot created by Manya. you can call me YOLO!",]
    ],
    [
        r"how are you ?|sup|wassup|kkrh",
        ["I'm doing goodnHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","It's OK, never mind",]
    ],
    [
        r"I am fine|I am good",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"I'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["Age is just a number?",]
    ],
    [
        r"What (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Manya created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Hogwarts, London',]
    ],
    [
        r"How is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"I work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy(but you should definitely eat an apple to keep the doctor away haha) ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["Not much into sports",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Dhoni","Sania Mirza"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Christian Bale and SRK"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Sorry,can't help you there"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]
def chat():
    print("Hi! I am a chatbot created by Manya for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()
