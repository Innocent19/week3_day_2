def fizzbuzz(list1,list2
):
    # try:
        if (len(list1)+ len(list2))%3 == 0 and (len(list1)+ len(list2))%5 != 0:
            return "Fizz"
        elif (len(list1)+ len(list2))%5 == 0 and (len(list1)+ len(list2))%3 != 0:
            return "Buzz" 
        while (len(list1)+ len(list2))%3 == 0 and (len(list1)+ len(list2))%5 == 0:
            return "Fizzbuzz" 
    # except TypeError:
x = input("Enter list1 : ")
y = input("Enter list2 : ")
print (fizzbuzz (x,y))
