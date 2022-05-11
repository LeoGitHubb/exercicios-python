def palindromo():

    print("Digite uma palavra:")
    word = input()

    if str(word) == str(word)[::-1] :
        print("Palindrome")
    else:
        print("Not Palindrome")
    
print(palindromo())