def Fizzbuzz(list1,list2):
    if (len(list1)+ len(list2))%3 is 0 and (len(list1)+ len(list2))%5 is not 0:
        return "Fizz"
    elif (len(list1)+ len(list2))%5 is 0 and (len(list1)+ len(list2))%3 is not 0:
        return "Buzz" 
    while (len(list1)+ len(list2))%3 is 0 and (len(list1)+ len(list2))%5 is 0:
        return "Fizzbuzz"  

print (Fizzbuzz ("apples","banana"))
