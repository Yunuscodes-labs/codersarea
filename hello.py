# # # # wap to print which number is repeated how many times in a list
 

# # # numbers = [1, 2, 3, 2, 4, 1, 5, 2, 3, 1]

# # # count_dict = {}   

# # # for num in numbers:
# # #     if num in count_dict:
# # #         count_dict[num] += 1   
# # #     else:
# # #         count_dict[num] = 1    


# # # for num, count in count_dict.items():
# # #     print(f"{num} is repeated {count} times")

# # #WAP that takes a list and a elements as arguments and returns the index of the element from the list and if the element is not found in the list it should return element due 

# def function(l,a):
#     for i in range (len(l)):
#         if l[i]==a:
#             return(i)
#             break
# list=[9,8,78,98]
# a=int(input("enter the number"))
# c=function(list,a)
# if c=None:
#     print('member due')
#     else:
#         print(c)''            


# #exception handeling,file handeling,functions
        

#WAP to sort a list in ascending order without sort function
list=[88,56,44,65]
def sort(a):
    for i in range(len(a)):
        if a[i]>a[i+1]:
            a[i]=a[i+1]

            else:
                continue
function(list)                
print(list)










