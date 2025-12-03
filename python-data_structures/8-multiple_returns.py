#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = None if sentence == '' else sentence[0]
    print("Length: {:d} - First character: {}".format(length, first))
