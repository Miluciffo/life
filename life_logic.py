life=[]
next_life=[]

for y in range(80):
    for x in range(120):
        life.append(0)#y*120+x
        next_life.append(0)

def getLife(x,y):
    return life[y*120+x]


def setLife(x,y,s):
    life[y*120+x]=s

