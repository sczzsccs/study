import numpy as np

def setString(list:list) -> str:
    Str = "{"
    for Tuple in list:
        Str+="{"+str(Tuple[0])+", "+str(Tuple[1])+"}, "
    Str = Str[:-2]+"}"
    return Str

n = np.random.randint(1,25,(np.random.randint(3,35),2)).tolist()

i = 0
while (i < len(n)):
    print(f"{i} : {n[i]}")
    if(n[i][0] == n[i][1]): n.pop(i)
    n[i] = sorted(n[i])
    i+=1
print(n)

n= setString(n)
print(n)