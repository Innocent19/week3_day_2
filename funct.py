def function_takes_string():
    vowels = "aeiou"
    new_string = str()
    input_string= input("Enter your string of choice:")
    no_duplications = set(input_string)
    duplicates_length = len(input_string) - len(no_duplications)
    for letter in input_string:
         if letter in vowels:
             new_string+=letter

    print((new_string, duplicates_length)) 
function_takes_string()    




