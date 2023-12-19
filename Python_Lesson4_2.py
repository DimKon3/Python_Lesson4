#x = int(input("Введите 5-ое число:"))
#x4 = x%10
#x3 = x//10%10
#x2 = x//100%10
#x1 = x//1000%10
#x0 = x//10000
#print("Результат:",x3**x4*x2/(x0-x1))

giveNumber = input("Введите целое пятизначное число: ")
print("Result ",(int(giveNumber[3])**int(giveNumber[4]))*int(giveNumber[2])/(int(giveNumber[0])-int(giveNumber[1])))