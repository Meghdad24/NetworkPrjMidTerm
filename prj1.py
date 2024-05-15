# -*- coding: utf-8 -*-
"""
Created on Sun May 12 19:19:24 2024

@author: Pouria
"""

import random

def bit_string_maker(length):
    data = ""
    
    for i in range(0, length):
        # data = data + random.choice(["0","1"])
        data += "1"
        data += "0"
        pass
    
    return data


print(bit_string_maker(20))

bitRate = 10**6
print(bitRate)