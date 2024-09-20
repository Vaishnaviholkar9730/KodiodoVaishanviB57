#Q2. Write a program to input a string and print the count of vowels and consonants in the string
vowel="AEIOUaeiou"
vowel_count=0
consonant_count=0
string=input("Enter the string:")

for char in string:
    if char in vowel:
        vowel_count+=1
    else:
        consonant_count+=1

print(" vowels is:",vowel_count)
print(" consonants is:",consonant_count)









































