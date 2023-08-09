import random

def get_word(guessword):
    f=open('word.txt')
    read=[]
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            read.append(line)
    randomword=random.choice(read)
    if(randomword  == guessword):
        print('Yess you guessed it right!!')
        return 1
    else:
        print('Bad luck the right word was: ',randomword)
        return 1
    

        

def main():
    print("Let's play a game")
    b='y'
    print('You have to guess a word from below and write it when asked if your guessed word is same as the word drawed from the list then you won or else you lose')
    print('The words are:')
    while(b=='y'):
        print('karel \nconsole \nguess\nword\ngame')
        print('Enter your guessed word:',end='')
        guessedword=input()
        words=get_word(guessedword)
        if words==1 :
            print('Wanna try again then press y or else n')
            b=input()

    
    
    
    
if __name__ == "__main__":
    main()
