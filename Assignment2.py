import sys
import random

def word_game(x1,x2,x3):
    L= [x1,x2,x3]
    word= random.choice(L)
    L.remove(word)
    if  len(x1)== len(x2) or len(x1) == len(x2) or len(x2)== len(x3):

        sys.stderr.write("Arguments should be a diﬀerent length\n")
        sys.stderr.flush()


    else :

        if len(word)>len(L[0]) and  len(word)>len(L[1]) :

            print(" Guess a longest word: {}".format(word))
            print("You found the longest word.Congratulations you won 50 pts")

        elif len(L[0])>len(word) and len(word)>len(L[1]):

            print("Guess a longest word:{}".format(word))
            print("You found a word from list.")
            print("You won 30 pts")

        elif len(L[0])>len(word) and len(L[1])>len(word) :

            print("Guess a longest word:{}".format(word))
            print("You found a shortest word from list.")
            print("You won 10 pts")
    return word


if len(sys.argv)== 4:
    print(word_game(sys.argv[1],sys.argv[2],sys.argv[3]))

else :
    sys.stderr.write("Please enter 3 words.")
    sys.stderr.flush()











