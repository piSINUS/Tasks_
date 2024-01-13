
def chempPlace():
    count = int(input(" Ведите кол-во запросов "))
    
    for i in range(count):
        countPl =  int(input("Количество участников ")) 
        time = [int(a) for a in input("Ведите набор чисел ").split()]
        time.append(0)
        voidlist = []
        schet = 1
        maxt = max(time)
        for j in range(countPl+1):
            voidlist.append(0)        
        if len(time) == countPl+1:
            for t in range(countPl+1):
                print(f"t = {t}")               
                e = maxt-1
                if time[t] == maxt or  time[t] == (e) or ((e in time) and time[t]==e-1):
                    voidlist[time.index(maxt)] = schet
                    time[time.index(maxt)] = 0
                    maxt = max(time) 
                    print(voidlist)
                else:
                    schet+=(len(set(time)))
        else:
            print("не правильное количкство участников и времени")
        voidlist.remove(0)
        print(voidlist)

chempPlace() 
# time = [int(a) for a in input("Ведите набор чисел ").split()]
# timeStruckt =[{'salary':x,'id':i} for i,x in enumerate(time)]
# timeStruckt.sort(key=lambda x:x['salary'])
# print(next((x['id']  for x in timeStruckt),None))