#Code đa phần được skid từ https://replit.com/@ThyNguyn20/FastRoyalblueProtools :P

import time

a = 1
b = 2
c = 10
d = ("1 cốc")

beef = 25    #Burger bò
chicken = 25 #Burger gà
wings = 30  #Đùi gà
tenders = 30  #Gà ko xương
fries = 20  #Khoai
soft = 25   #Nước có ga
tea = 15    #Trà chanh
ic = 10     #Kem
brw = 12    #Brownies
cake = 12   #Bánh kem

print("*"*30)
print("Phần mềm order đồ ăn quán :3 ")
print("*"*30)

print("Menu của Quán: ")
print("_________________________________________")
print("|                                       |")
print("|  1 - Burger thịt bò phô mai 25k       |")
print("|  2 - Burger thịt gà 25k               |")
print("|  3 - Đùi gà rán (2 cái) - 30k         |")
print("|  4 - Gà không xương (10 miếng) - 30k  |")
print("|  5 - Khoai tây chiên - 20k            |")
print("|  =================================    |")
print("|  6 - Coke/Fanta/Sprite (450ml) - 25k  |")
print("|  7 - Trà chanh (250ml) - 15k          |")
print("|  8 - Kem Vanilla/Chocolate - 10k      |")
print("|  9 - Bánh Brownies - 12k              |")
print("|  10 - Bánh Kem - 12k                  |")
print("|_______________________________________|")
print(" ")
choice = input('Hãy nhập số của món bạn muốn ăn: ')
print("     ")

if choice == '1':
  print("Bạn đã chọn",a,"Burger thịt bò phô mai.")
if choice == '2':
  print('Bạn đã chọn',a,'Burger thịt gà.')
if choice == '3':
  print('Bạn đã chọn',b,'hai miếng đùi gà rán.')
if choice == '4':
  print('Bạn đã chọn',c,'miếng gà không xương.')
if choice == '5':
  print('Bạn đã chọn',a,'suất khoai tây chiên.')
if choice == '6':
  print('Bạn đã chọn',d,'đồ uống.')
if choice == '7':
  print('Bạn đã chọn',d,'Trà chanh.')
if choice == '8':
  print('Bạn đã chọn',a,'cây kem.')
if choice == '9':
  print('Bạn đã chọn',a,'miếng bánh Brownies.')
if choice == '10':
  print('Bạn đã chọn',a,'miếng bánh kem.')

print(" ")

choice3 = input ("Bạn có muốn chọn tiếp không? Hãy nhấn 1 nếu có, 0 nếu không.")
print(" ")
if choice3 == "1":

    choice2 = input ("Hãy chọn đồ ăn mà bạn muốn tiếp:")
    if choice2 == '1':
        print("Bạn đã chọn",a,"Burger thịt bò phô mai.")
    if choice2 == '2':
        print('Bạn đã chọn',a,'Burger thịt gà.')
    if choice2 == '3':
        print('Bạn đã chọn',b,'hai miếng đùi gà rán.')
    if choice2 == '4':
        print('Bạn đã chọn',c,'miếng gà không xương.')
    if choice2 == '5':
        print('Bạn đã chọn',a,'suất khoai tây chiên.')
    if choice2 == '6':
        print('Bạn đã chọn',d,'đồ uống.')
    if choice2 == '7':
        print('Bạn đã chọn',d,'Trà chanh.')
    if choice2 == '8':
        print('Bạn đã chọn',a,'cây kem.')
    if choice2 == '9':
         print('Bạn đã chọn',a,'miếng bánh Brownies.')
    if choice2 == '10':
        print('Bạn đã chọn',a,'miếng bánh kem.')
  
if choice3 == "0":
    print("Cảm ơn bạn đã dùng dịch vụ của chúng tôi !")



print(" ")
print("Mã hoá đơn của bạn: ...")
print(" ")
print("Hãy đến quầy thanh toán để thanh toán")
