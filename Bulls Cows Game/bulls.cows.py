import random
num=[]
a=0

def createnum():
    for i in range(4):
        x=random.randrange(0,9)
        num.append(x)
    if len(num)>len(set(num)):
        num.clear()
        createnum()
createnum()
print(num)

def game():
    global a
    j=[]
    n=input('Make a guess:(from 1000 up to 9999) ')
    a+=1
    for i in n:
        j.append(int(i))
    count1=0
    if num!=j:
        count = sum(num[i] == j[i] for i in range(len(num)))
        print(count,'cow')
        for i in num:
            for k in j:
                if i==k:
                    count1+=1
        print(count1-count,'bull')
        return game()
    print('Attempts:',a)
    return 'You win'
            
print(game())



            

