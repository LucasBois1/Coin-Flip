#!/usr/bin/env python
#Python 2.7

from Tkinter import *
import random

def coin_flip(coin):
    if coin == 1:
        return 'Tails'
    else:
        return 'Heads'

def main(flip_num):

    final_result = {}

    for number in range(1,flip_num + 1):
        coin = random.randrange(0,2,1)
        if coin_flip(coin) not in final_result:
            final_result[coin_flip(coin)] = 1
        else:
            final_result[coin_flip(coin)] = final_result[coin_flip(coin)] +1
    heads = final_result.get('Heads')
    tails = final_result.get('Tails')

    heads = int(heads)
    tails = int(tails)

    headsPercentage = heads * 100 // flip_num
    tailsPercentage = tails * 100 // flip_num
    
    return final_result,heads,tails,headsPercentage,tailsPercentage

    #print '\n    Results\n','-'*18,'\nHeads ==>', heads,'\nTails ==>', tails, '\n','-'*18
    #print 'Heads ==>', headsPercentage, '%\nTails ==>', tailsPercentage, '%', '\n','-'*18
