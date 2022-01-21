from random import randint

def initMassiv():
    massivA = [];
    N = 10;
    for i in range(N):
        massivA.append(randint(1, 99))
# print(massivA)
    return massivA;

def filtr(a=[]):
    print(a)
  #  b = a.count();
    i = 0
    while i != len(a):
        print(i)
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                print(a)

        i += 1
    else:
        print('Цикл окончен, i =', i)


    return a;



def method():
    #massivA.count();
    initMassivB = [1,2,3,4,5,6,7]
    j=3
    initMassivB[j], initMassivB[j+1] = initMassivB[j+1], initMassivB[j]
    print(initMassivB)
    print("It is works");

filtr(initMassiv());
method();

#massivA.sort()
#print(massivA)

#print(massivA.count)
#print(massivA[1])
