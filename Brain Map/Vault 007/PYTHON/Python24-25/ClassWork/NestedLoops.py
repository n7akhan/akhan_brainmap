aList = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
vowels = ["a","e","i","o","u"]

for days in aList:
    print(f'{days} length is {len(days)}')
    for vowel in vowels:
        print(f'{vowel} = {days.count(vowel)}')
