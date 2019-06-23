import random, string

def randomIDFA(n):
   randlst = [random.choice(string.ascii_letters.lower() + 2 * string.digits) for i in range(n)]
   return ''.join(randlst)

def randomADID(n):
   randlst = [random.choice(string.ascii_letters.upper() + 2 *  string.digits) for i in range(n)]
   return ''.join(randlst)


if __name__ == "__main__":
    print("件数: ")
    N = int(input())
    print("要素数: ")
    ele_num = int(input())
    print("スペース区切りで各要素の上限の値を入力: ")
    elements=[]
    for i in range(ele_num):
        elements.append(int(input()))
    
    print("作成するtableの幅: ")
    width = int(input())
    # IDFA
    tableIDFA = [[] for i in range(width)]
    for i in range(width):
        for j in range(width):
            tableIDFA[i].append(randomIDFA(4))
           
    # ADID
    tableADID = [[] for i in range(width)]
    for i in range(width):
        for j in range(width):
            tableADID[i].append(randomADID(4))

    num = range(N)
    for i in num:
        r = random.randrange(2)
        if r == 0:
            IDFA = tableIDFA[random.randrange(width)][random.randrange(width)] + '-' + tableIDFA[random.randrange(width)][random.randrange(width)] + '-' + tableIDFA[random.randrange(width)][random.randrange(width)]
            # add attributes
            row = IDFA + ',' + 'ios' 
            for i in range(ele_num):
                row = row + ',' + str(random.randrange(1, elements[i]+1))
            # print
            print(row)

        else:
            ADID = tableADID[random.randrange(width)][random.randrange(width)] + '-' + tableADID[random.randrange(width)][random.randrange(width)] + '-' + tableADID[random.randrange(width)][random.randrange(width)]
            # add attributes
            row = ADID + ',' + 'android' 
            for i in range(ele_num):
                row = row + ',' + str(random.randrange(1, elements[i]+1))
            # print
            print(row)
        
