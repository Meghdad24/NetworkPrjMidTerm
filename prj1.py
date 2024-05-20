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

def sampling(noisy_signal, first_len, exp_len):
    samples = []
    
    for i in range(first_len):
        samples.append(noisy_signal[int(i*exp_len) + int(exp_len/2)])
        pass
    
    return samples

def Retrieving_bits_of_information(samples):
    Retrieved_bits = []
    
    for voltage in samples:
        if(voltage >= 0):
            Retrieved_bits.append(0)
            pass
        elif(voltage < 0):
            Retrieved_bits.append(1)
            pass
        pass
    
    
    return Retrieved_bits


# MAIN!
bitRate = 10**6
zeroVoltage = 5
 # int(input("enter zeroVoltage: "))
oneVoltage = zeroVoltage * -1

# signal = bit_string_maker(int(input("Enter signal length: ")))
signal = bit_string_maker(20)
# print(signal)

exp_len = 20
signalExp = signal_expansion(signal, exp_len)
signalExpV = transform_to_voltage(signalExp,zeroVoltage,oneVoltage)
# print(signalExp)

time = np.arange(len(signalExpV))

plt.step(time,signalExpV)

noisy_signal = communication_channel(signalExpV)

# print(noisy_signal)

time = np.arange(len(noisy_signal))

plt.plot(time,noisy_signal)

samples = sampling(noisy_signal, len(signal), exp_len)
# print(samples)

Retrieved_bits = Retrieving_bits_of_information(samples)
# print(Retrieved_bits)


voltageArray = np.arange(0.1, 2.1, 0.1)
percentage_of_error_bits = []

for FzeroVoltage in voltageArray:
    FsignalExp = signal_expansion(signal, exp_len)
    FsignalExpV = transform_to_voltage(FsignalExp,FzeroVoltage,FzeroVoltage * -1)
    Fnoisy_signal = communication_channel(FsignalExpV)
    
    
    # time = np.arange(len(Fnoisy_signal))
    # plt.figure()
    # plt.step(time,FsignalExpV)
    # plt.plot(time,Fnoisy_signal)
    
    Fsamples = sampling(Fnoisy_signal, len(signal), exp_len)
    # print(Fsamples)

    Retrieved_bits = Retrieving_bits_of_information(Fsamples)
    # print(Retrieved_bits)
    
    # plt.figure()
    # time = np.arange(len(Retrieved_bits))
    # plt.step(time,Retrieved_bits)
    
    number_of_error_bits = 0

    for i in range(len(signal)):
        if(Retrieved_bits[i] != signal[i]):
            number_of_error_bits += 1
            pass
        pass
    
    percentage_of_error_bits.append(number_of_error_bits / len(signal))
    
    pass

plt.figure()
time = np.arange(len(percentage_of_error_bits))
plt.plot(time,percentage_of_error_bits)
plt.title('The error value is proportional to the voltage value')

plt.ylabel('Voltage')

# افزودن شبکه (grid)
plt.grid(True)

# افزودن راهنما (legend)
plt.legend()
