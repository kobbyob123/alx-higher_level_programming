#!/usr/bin/python3

def multiple_returns(sentence):
    num = len(sentence)
    if sentence == '':
        return (num, None)
    
    first_char = sentence[0]
    return (num, first_char)
