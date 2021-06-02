# # problem 1
# dict_1={"player1":"aswin","player2":"ashu","player3":"cs"}
# dict_2={"player1":"ashu","fruit1":"apple","fruit2":"mango"}
# dict_3={}
# for i,j in dict_2.items():
#     for x,y in dict_1.items():
#         if i==x:
#             dict_3[i]=y+j
# print(dict_3)
"""
in this question both the dict types should be of same data type
if they are different then we should use exception handling
"""

# problem 2
# n1=input("what is your input\n")
# d1={}
# d1["string1"]=n1
# # print(d1)
# y=[]
# x=[]
# for i in d1.values():
#     y.append(i)
# y=str(*y)
# # print(y)
# for char in y:
#     # print(char)
#     x.append(char)
#     # print(x)
#     v = 0
#     for j in x:
#         if j==char:
#             v=v+1
#     print(j,":",v)

# problem 2
# modified code
# n1=input("what is your input\n")
# d1={}
# d1["string1"]=n1
# # print(d1)
# y=[]
# x=[]
# for i in d1.values():
#     y.append(i)
# y=str(*y)
# x=set(y)
# for char in x:
#     v = 0
#     for j in y:
#         # print(j)
#         if j==char:
#             v=v+1
#     print(char,":",v)

# problem 3
# sting_1="AN APPLE A DAY KEEPS A DOCTOR AWAY"
# sting_2="WATER"
# a=sting_2[0]
# for i in sting_1:
#     if a==i:
#         x=sting_1.index(i)
#         print(x)
#         print(sting_1[0:x])

# problem 4
# x=input("what is you string\n")
# y=x.split()
# v=0
# for i in y:
#     if i=="are":
#         v=v+1
# print("the occurence of are in the given string is:",v)
