#Harry Dreesen-Higginbotham
def myFunc(word): # sets up the function
    a = word.split() # initially splits up the sentence into words.
    for a in word: # if there are the words in the sentence 
        b = a.split() # splits the words into letters
        for b in a: 
            print(b) #prints the letters
c = input(print("Enter a short sentence: ")) #input your phrase
c = c.replace(" ", "-") #inspo from graham :)
(myFunc(c)) #does the function
