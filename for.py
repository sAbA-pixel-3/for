# циклы, for, while 

# for переменная in обьект операции:
#     действие с обьектом

# fruits = ["apple", 'banana', 'orange', 'kiwi']

# for fruits in fruits:
#     print(fruits) 


# nums = [1, 2,3,4,5,6,7,8,9]
# for num in nums:
#     print(num+5) 


# nums = "hello" # цифры нельзя итеррировать, но int можно

# for n in nums:
#     print(n) 


# # генератор чисел "range"
# for i in range(1, 11): # (start,end,step) 
#     print(i) 


# оператор break,  continue

# for i in range(1, 11):
#     if i == 5:
#         break # оператор кот принудительно завершает операцию
#     print(i) 


# for i in range(1, 11):
#     if i == 5:
#         continue # пропускает текушую итерацию
#     print(i) # 1,2,3,4,5,6,7,8,9,10


# for i in range(1, 11):
#     if i == 5:
#         print("five")
# else:
#     print("hello") 


# num = [1,2,3,4,5,6,7,8,9]
# res = 0

# for n in num:
#     res += n # res = res + num
# print(res)  








# for i in range(10, 0, -1):
#     print(i)  
# print("Start!") 


# words = 'hello world,I LOVE METALLL EYAAAAAAAAA'
# vowels = 'aeiouyAEIOUY'
# count = 0  
# for q in words:
#     if q in vowels:
#         count += 1 
# print("The amount of vowels is: ", count) 


# q = int(input("Enter any number: "))
# if q < 0:
#     print("Impossible!")
# else:
#     f = 1
#     for i in range(1, q + 1):
#         f *= i
# print(f"Factorial for {q} is {f}.")


# for i in range(1, 10):
#     for q in range(1, 10):
#         print(f"{i} * {q} = {i * q}")
#     print() 


# res = 0
# for num in range (1, 100):
#     res += num
# print(res) 


# num = 12345
# q = sum(int(q) for q in str(num)) 
# print(q) 


# text = ["hello","how","are","u"]
# count = 0
# for t in text:
#     count += 1
# print(count) 


