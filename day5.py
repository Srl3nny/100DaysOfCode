#project day 5 100 days of code
#password generator
import random

#create list of caracters
num = ['1','2','3','4','5','6','7','8','9','0']
letter = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','x','z','w','y','k']
symbols = ['#','%','*']


qt_num = int(input('How many numbers would you like in your password?\n'))
qt_letter = int(input('How many letters?\n'))
qt_symbols = int(input('How many symblos?\n'))


passwords = []

while qt_num > 0:
    #add (append) t list password
    passwords.append(random.choice(num))
    qt_num -= 1

while qt_letter > 0:
    passwords.append(random.choice(letter))
    qt_letter -= 1    

while qt_symbols > 0:
    passwords.append(random.choice(symbols))
    qt_symbols -= 1

#mess up the order of the itens
random.shuffle(passwords)

#convert list to string password
password=""
for i in passwords:
    password += i
print(password)
