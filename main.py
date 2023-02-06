#Vowel counter
#by Chris Cote

#Write a function average_vowels that takes a list of strings as a parameter and returns the average number of vowels occurring in each string
# in the list, both upper- & lower-cased. No library functions aside from input/output.

user_inputs = []
vowels = ["a", "e", "i", "o", "u"]
vowel_count = []

def average_vowels(vowels, user_input, vowel_count):
    user_entries = eval(input("How many words to you want to check?  "))
    for i in range(user_entries):
        user_input = input(("Please enter a word to check your vowels:  ")).lower()
        user_inputs.append(user_input)
        temp_vowel_count = 0
        for x in range (len(user_input)):
            for y in range (len(vowels)):
                if user_input[x] == vowels[y]:
                    temp_vowel_count += 1
                else:
                    temp_vowel_count += 0
        vowel_count.append(temp_vowel_count)
    print("The total number of words you checked was",len(user_inputs),"which contained",sum(vowel_count))
    print("vowels which is an average of",sum(vowel_count)/(len(user_inputs)),"vowels per word")


#average_vowels(vowels, user_inputs, vowel_count)

string = "hello"
string[2]="y"
print(string)
