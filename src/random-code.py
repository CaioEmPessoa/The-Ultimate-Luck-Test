import random

RNG = random.randint(1, 100)
print(RNG)

if 1 <= RNG <= 50:
    print("Common (1/2)")
elif 51 <= RNG <= 70:
    print("Uncommon 1/5")
elif 71 <= RNG <= 85:
    print("Ok (1/9)")
elif 86 <= RNG <= 94:
    print("Rare (1/13)")
elif 94 <= RNG <= 99:
    print("Epic (1/20)")
elif 99 <= RNG <= 100:
    print("Legendary (1/100)")