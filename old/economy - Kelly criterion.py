import random
kiekis = 1000000
posibilities = 2

minbet = 50
player = 5000
house = 1000000
houseadvinproc = 0

extrisk = 1.1
bet = 0
pmax = player
#ats = [0] * posibilities
for i in range(kiekis):
    bet = player*0.04
    if player < bet:
        print("gameover", i)
        break
    elif house < bet:
        print("victory", i)
        break
    sk = random.random()
    #print(sk, bet, player)
    if sk > 0.5+(houseadvinproc*0.01):
        player += bet
        house -= bet
    else:
        player -= bet
        house += bet
    if player > pmax:
        pmax = player
print('\n')
print('player has',player,'most won',pmax)
print('house has',house)
