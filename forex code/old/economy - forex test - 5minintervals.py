f = open("DAT_ASCII_EURUSD_T_202203.csv", "r")
bank = f.read().split(',')
timeint = 500 #in sec
last = 1
lasti = 0
leverage = 500 # to 1
ats = ""
cash = 500
for i in range(3,len(bank)-1,3):
    num = int(bank[i][-7:][:-3])
    if last+timeint < num or num < last:
        if float(bank[i+1]) > float(bank[lasti+1]):
            ats += str((float(bank[i+1])-float(bank[lasti+1]))*100*leverage)+" "+bank[i]+"\n"
            last = num
            lasti = i
print(ats)
