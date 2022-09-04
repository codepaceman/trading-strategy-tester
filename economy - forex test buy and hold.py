f = open("DAT_ASCII_EURUSD_M1_202203.csv", "r")
bank = f.read().split(';')
spct = 5
lasti = 0
leverage = 500 # to 1
ats = 0
cash = 500
tip = 1
wins = 1.005
trades = 0
for i in range(spct,len(bank)-1,spct):
    if float(bank[i+1])*wins*tip > float(bank[lasti+1])*tip:
        ats += (float(bank[i+1])-float(bank[lasti+1]))*leverage*tip
        lasti = i
        tip *= -1
        trades += 1
print(ats,trades,lasti/5/1000)
print((float(bank[0+1])-float(bank[len(bank)-1]))*leverage)
