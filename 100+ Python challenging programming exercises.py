# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt

# Question 1
# l = []
# for i in range(2000, 3200):
#     if(i%7==0 and i%5!=0): 
#         l.append(str(i))

# print('-'.join(l))

#Question 2

# x = int(input("Enter your input "))
# f = 1
# for i in range(1,x+1):
#     f *= i
# print(f)


#Question 3

# x = int(input())
# d = {}
# for i in range(1, x+1):
#     d[i] = i*i
# print(d)

#Question 4

# x = input()
# li = x.split(',')
# print(li)
# tp = tuple(li)
# print(tp)
# print(type(tp))

#Question 5

# class Person:
#     def __init__(self):
#         pass
#     def getString(self):
#         self.name = input()
#     def printString(self, name):
#         print(self.name.upper())
#         print(name)
# p = Person()
# p.getString()
# p.printString("tahmid")

#Question 6

# [[0, 0, 0, 0, 0], 
#  [0, 1, 2, 3, 4], 
#  [0, 2, 4, 6, 8]] 

# n = int(input())
# m = int(input())
# n, m = map(int, input().split() )
# # print(n)
# # print(m)
# lii = []
# for i in range(n):
#     li = []
#     for j in range(m):
#        #print(i*j, end=" ")
#        li.append(i*j)
#     #print()
#     lii.append(li)

# print(lii)



# Question 8

# x = input()
# li = x.split(',')
# st = []
# for i in li:
#     st.append(str(i))
# st.sort()
# print(st)
# print (','.join(st))



# Question 9

# while True:
#     s = input()
#     if(len(s)>0):
#         print(s.upper())
#     else:
#         break

# Question 10
# s = input()
# li = s.split(" ")
# st = set(li)
# li2 = list(st)
# li2.sort()
# print(li2)
# print(' '.join(li2))



#Question 23
# print( 2 ** 2 )

# Question 24

# def square(num):
#     '''Return the square value of the input number.
    
#     The input number must be integer.
#     '''
#     return num ** 2

# print( square(2))
# print( square.__doc__)


