f = open("DAT_ASCII_EURUSD_T_202203.csv", "r")
bank = f.read().split(',')
timeint = 500 #in sec
last = 1
lasti = 0
leverage = 500 # to 1
ats = 0
cash = 500
tip = 1
wins = 1.05
losss = 0.90
trades = 0
for i in range(3,len(bank)-1,3):
    num = int(bank[i][-7:][:-3])
    if last+timeint < num or num < last:
        if float(bank[i+1])*wins*tip > float(bank[lasti+1])*tip or float(bank[i+1])*losss*tip > float(bank[lasti+1])*tip :
            ats += (float(bank[i+1])-float(bank[lasti+1]))*100*leverage*tip
            last = num
            lasti = i
            tip *= -1
            trades += 1
print(ats,trades)
