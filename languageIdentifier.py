import sys
import math

# This function reads the probabilities from the given text files
def get_parameter_vectors():
    e=[0]*26
    s=[0]*26

    #reading english probabilities from file
    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    #reading spanish probabilities from file
    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def count_occurences(filename):
    X=dict({'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0})
    with open (filename,encoding='utf-8') as f:
        fileText = f.read().upper()
        for char in fileText:
            if char in X:
                X[char] += 1
    f.close()
    return X


# The below code uses the Bayes rule to determine the probability of a given text file being in English or Spanish.
X = count_occurences("englishLetter.txt")
Y = count_occurences("spanishLetter.txt")

english, spanish = get_parameter_vectors()

#compute F(y) (the likelihood that a given file is in language y)
fEnglish = math.log(.6) #prior probability that text file is in English, before reading
fSpanish = math.log(.4) #prior probability that text file is in Spanish, before reading

englishOccurrences = count_occurences("englishLetter.txt")

i = 0
#use log to avoid unnecessary computation and underflow
for letter in englishOccurrences:
    fEnglish += englishOccurrences[letter] * math.log(english[i])
    fSpanish += englishOccurrences[letter] * math.log(spanish[i])
    i += 1

#compute P(Y = y|x)
if(fSpanish - fEnglish >= 100): #account for overflow, assume that file is in Spanish
    pEnglish = 0
elif(fSpanish - fEnglish <= -100): #account for underflow, assume that file is in English
    pEnglish = 1
else:
    pEnglish = 1 / (1 + math.pow((math.e),(fSpanish - fEnglish)))

print("Output for englishLetter.txt:")
print("P(English): " '%.4f' % pEnglish)
print()

fEnglish = math.log(.6) #prior probability that text file is in English, before reading
fSpanish = math.log(.4) #prior probability that text file is in Spanish, before reading

spanishOccurrences = count_occurences("spanishLetter.txt")

i = 0
for letter in spanishOccurrences:
    fEnglish += spanishOccurrences[letter] * math.log(english[i])
    fSpanish += spanishOccurrences[letter] * math.log(spanish[i])
    i += 1

#compute P(Y = y|x)
if(fSpanish - fEnglish >= 100): #account for overflow, assume that file is in Spanish
    pEnglish = 0
elif(fSpanish - fEnglish <= -100): #account for underflow, assume that file is in English
    pEnglish = 1
else:
    pEnglish = 1 / (1 + math.pow((math.e),(fSpanish - fEnglish)))

print("Output for spanishLetter.txt:")
print("P(English): " '%.4f' % pEnglish)




