import random
kiekis = 10000000
pmax = 0
combo = 0
for i in range(kiekis):
    sk = random.randint(0,1)
    if sk == 1:
        combo += 1
        if combo > pmax:
            pmax = combo
    else:
        combo = 0
print(pmax)
