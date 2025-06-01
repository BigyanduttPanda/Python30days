#- Write a function that computes the sum and average of a list of numbers

#Sum of list of Numbers
def sum_list(a):
    total = sum(a)
    return total
a= [10,20,30,40,50,60,70,80,90]
Result = sum_list(a)
print("Sum of the list of numbers is : ",Result)


#Average of the List of number

def avg_list(a):
    total= round(sum(a)/len(a))
    return total

a = [10,20,30,40,50,60,70,80,90]
Result = avg_list(a)
print("Average of the list of numbers is : ",Result)