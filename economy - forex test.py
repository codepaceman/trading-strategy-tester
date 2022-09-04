import statistics as stat
import random
f = open("DAT_ASCII_EURUSD_M1_202203.csv", "r")
bank = f.read().split(';')[1::5]
bank = [float(i) for i in bank]
lev = 500
ats = 0
li = 0
bear = 1
trades = 0
win = 1.005
for i in range(100,len(bank)):
    if stat.fmean(bank[i-10:i:])*bear>stat.fmean(bank[i-100:i:])*bear:
        bear *= -1
        ats += (bank[i]-bank[li])*lev*bear
        li = i
        trades += 1
print(ats,trades,li+1)
