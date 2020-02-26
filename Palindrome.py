my_str = input("Enter the String: ")
rev_str = reversed(my_str)
my_str = my_str.casefold() # make all values in same case if the input is ALpa it makes either ALPA or alpa
if list(my_str) == list(rev_str) :
    print("The given string is Palindrome ")
else :
    print("The given string is not palindrome")