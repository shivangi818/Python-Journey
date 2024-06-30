def palindrome(text):
    if len(text)<=1:
        print("Palindrome")
    else:
        if text[0]==text[-1]:
            palindrome(text[1:-1])
            pass
        else:
            print("not a palindrome")
palindrome("malayalam")
palindrome("abba")
palindrome("python")

