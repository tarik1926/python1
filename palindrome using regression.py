n = [1,2,3]

def is_palindrome(n):
    if len(n) <= 1:
        return True
    else:
        if n[0] == n[-1]:
            return is_palindrome(n[1:-1])
        else:
            return False

print(is_palindrome(n))