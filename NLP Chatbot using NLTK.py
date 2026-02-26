import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello",
     ["Hello!", "Hi there!"]],
    [r"my name is (.*)",
     ["Hello %1, nice to meet you!"]],
    [r"bye",
     ["Goodbye!"]]
]

chat = Chat(pairs, reflections)
chat.converse()