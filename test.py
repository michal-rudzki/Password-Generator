from random import randrange, randint

length = 3
val = {
    'up':   True,
    'low':  False,
    'nu':   True,
    'spec': False
}

def genUP():
    if val.get('up') == True:
        return 'UP'

def genLOW():
    if val.get('low') == True:
        return 'low'

def genNU():
    if val.get('nu') == True:
        return '123'

def genSPEC():
    if val.get('spec') == True:
        return '!@#$%'

val_random = ('up','low','nu','spec')
val_temp = []
password = ''

for index, value in enumerate(val_random):
    #print(index, value)
    if val.get(value) == True:
        val_temp.append(val_random[randint(0,len(val_random)-1)])

tmp = []
for l in range(10):
    if genUP() != None:
        tmp.append(genUP())
    if genLOW() != None:
        tmp.append(genLOW())
    if genNU() != None:
        tmp.append(genNU())
    if genSPEC() != None:
        tmp.append(genSPEC())
        
print(tmp)    
for c in tmp:
    print(tmp[randint(0, len(tmp)-1)])
#for v in val.keys():
#    for l in range(length):
#        if val[v] == True and v == list(val.items())[0][0]:
#            print("Uppercase")
#            print(v, val[v])
#        elif val[v] == True and v == list(val.items())[1][0]:
#            print("Lowercase")
#            print(v, val[v])
#        elif val[v] == True and v == list(val.items())[2][0]:
#            print("Numbers")
#            print(v, val[v])
#        elif val[v] == True and v == list(val.items())[3][0]:
#            print("Special")
#            print(v, val[v])
#        else:
#            print("---")
        
# print(val.values())
# print(val.items())
# print(val.keys())