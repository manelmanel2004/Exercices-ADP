
user_string = input("Please type  string: ").lower()
vowels = ['a', 'e', 'o']

for vowel in vowels:
    if vowel in user_string:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
