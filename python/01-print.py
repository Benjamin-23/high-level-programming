# intro to python 
# print("Hello word");
print(199);
print(5+5)
# adding variable
age = '25' 
print(len(age))
names ="benjamin kitonga"
splitName = names.split(' ')
print(splitName[0][0].capitalize())

# function 
def  sum(a,b):
    return a + b

def sub( a,b):
    return a - b 

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
option = input("operation (sum/sub): ")

if option == "sum":
    print(f'a + b = {sum(a,b)}')

elif option == "sub":
    print(f'a - b = {sub(a,b)}')

else:
    print("invalid response")


# loops

sentence = "and bring back the screenshot"
letters = {}
for l in sentence:
    if l in letters:
        letters[l] +=1
    else:
        letters[l] = 1
print(letters)

number = 0
if number > 0:
    print(f'{number} is positive number')
elif number < 0 :
    print(f'{number} is negative number')
else:
    print(f'{number} number is zero')