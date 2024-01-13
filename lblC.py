# проверьте, что
# заданная строка может быть о,разована как последовательность
# корректных автомо,ильных номеров, которые записаны подряд без
# пробелов. В случае положительного ответа выведите любое такое
# разбиение
def carSign():
    count = int(input("Ведите count "))   
    countNum =""
    prostChisl = [4,5,9,13,14,17,18,19,21,26,27,31,41,44,49,48]

    for i in range(count):
        carNum = str(input("Ведите последовательность "))

        while len(carNum)!=0:
            if len(carNum) in prostChisl or len(carNum)%4==0 or len(carNum)%5 ==0 :
                if (ord(carNum[0]) in range(65,90) and ord(carNum[1]) in range(48,58) and ord(carNum[2]) in range(48,58) and ord(carNum[3]) in range(65,90) and ord(carNum[4]) in range(65,90)):
                    countNum+=carNum[0:5]+" "
                    carNum =carNum[5:]
           
                elif ord(carNum[0]) in range(65,90) and ord(carNum[1]) in range(48,58) and ord(carNum[2]) in range(65,90) and ord(carNum[3]) in range(65,90) :
                    
                    if len(carNum)==5:
                        countNum = "-"
                        break
                    countNum+=carNum[0:4]+" "
                    carNum = carNum[4:]
                
                else:
                    print("-")
                    break
            else:
                print("-")
                break
            
        print(countNum)
        countNum = ''

count = int(input("Ведите count "))   

carSign()

