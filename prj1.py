# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt

def signal_expansion(signal_input, lengthPerBit):
    
    signalExp = []
    
    for i in range(len(signal_input)):
        
        if(signal_input[i]==1):
            for i in range(lengthPerBit):
                signalExp.append(1)
                pass
        
        elif(signal_input[i]==0):
            for i in range(lengthPerBit):
                signalExp.append(0)
                pass
            pass
    
    return signalExp

def add_gaussian_noise(signal, mean, std_dev):
    
    noise = np.random.normal(mean, std_dev, len(signal))
    noisy_signal = signal + noise
    
    return noisy_signal

def transform_to_voltage(signal_input,zeroVoltage,oneVoltage):
    
    signal = []
    
    for i in range(len(signal_input)):
        
        if(signal_input[i]==1):
            signal.append(oneVoltage)
            
        elif(signal_input[i]==0):
            signal.append(zeroVoltage)    
            
        pass
    
    return signal

def bit_string_maker(length):
    
    signal = []
    
    for i in range(0, int(length/2)):
        signal.append(1)
        signal.append(0)
        pass
    
    return signal

def communication_channel(signal):
    
    mean = 0
    std_dev = 1
    
    noisy_signal = add_gaussian_noise(signal, mean, std_dev)
    
    return noisy_signal

# MAIN!
bitRate = 10**6
zeroVoltage = int(input("enter zeroVoltage: "))
oneVoltage = zeroVoltage * -1

signal = bit_string_maker(int(input("Enter signal length: ")))
print("signal: " +signal)

signalExp = signal_expansion(signal, 30)
signalExp = transform_to_voltage(signalExp,zeroVoltage,oneVoltage)
print("signalExp: " + signalExp)

time = np.arange(len(signalExp))

plt.step(time,signalExp)

noisy_signal = communication_channel(signalExp)

print("noisy signal: " + noisy_signal)

time = np.arange(len(noisy_signal))

plt.plot(time,noisy_signal)