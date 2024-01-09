#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    else:
        sen_len = len(sentence)
        first = sentence[0]
        return (sen_len, first)
