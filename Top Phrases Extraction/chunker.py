import nltk
nltk.download('stopwords')
from tkinter import *
import time
from nltk.corpus import stopwords
import re

def transform(sentence):
    sentence = sentence.split()
    for i in range(len(sentence)):
        sentence[i] = sentence[i].replace(',', '')
        sentence[i] = sentence[i].replace('.', '')
        sentence[i] = sentence[i].replace(']', '')
        sentence[i] = sentence[i].replace('[', '')
        sentence[i] = sentence[i].replace(')', '')
        sentence[i] = sentence[i].replace('(', '')
        sentence[i] = sentence[i].replace('|', '')
        sentence[i] = sentence[i].replace('#', '')
        sentence[i] = sentence[i].replace(':', '')
        sentence[i] = sentence[i].replace(';', '')
    return ' '.join(sentence)


def extractPhrase(corpus):
    
    stop_words = stopwords.words("english")
    '''
    austen_emma = gutenberg.sents('austen-emma.txt')

    # Fixing the corpus
    corpus = [' '.join(sent) for sent in austen_emma]


    regex = re.compile('[a-zA-Z]+')

    # Removing the noise

    corpus =[' '.join([word for word in sent.split() if regex.search(word)]) for sent in corpus]
    '''

    #corpus = input('Please Enter the text: ')
    corpus = corpus.split('.')

    regex = re.compile('[a-zA-Z]+')

    # Removing the noise
    corpus =[' '.join([word for word in sent.split() if regex.search(word)]) for sent in corpus]

    #N-gram
    #Calculating no. of bigrams and trigrams

    frequency_count = {}
    for sent in corpus:
        sent = sent.split()
        #print(sent)
        N = 2
        bigrams = [' '.join(sent[i: i + N]) for i in range(len(sent) - N + 1)]
        for bigram in bigrams:
            bigram = transform(bigram)
            s = bigram.split()
            if s[len(s) - 1] not in stop_words:
                if bigram in frequency_count:
                    frequency_count[bigram] += 1
                else:
                    frequency_count[bigram] = 1
        
        N = 3
        trigrams = [' '.join(sent[i: i + N]) for i in range(len(sent) - N + 1)]
        for trigram in trigrams:
            trigram = transform(trigram)
            s = trigram.split()
            if s[len(s) - 1] not in stop_words:
                if trigram in frequency_count:
                    frequency_count[trigram] += 1
                else:
                    frequency_count[trigram] = 1

        N = 4
        fourgrams = [' '.join(sent[i: i + N]) for i in range(len(sent) - N + 1)]
        for fourgram in fourgrams:
            fourgram = transform(fourgram)
            s = fourgram.split()
            if s[len(s) - 1] not in stop_words:
                if fourgram in frequency_count:
                    frequency_count[fourgram] += 1
                else:
                    frequency_count[fourgram] = 1

    frequency_count = sorted(frequency_count.items(), key = lambda x: x[1], reverse = True)

    '''
    c = 100
    for phrase in frequency_count:
        c -= 1
        if c == 0:
            break
        print(phrase[0], phrase[1])
    '''
    res = []
    cnt = 0
    for phrase in frequency_count:
        if cnt == 100:
            break
        res.append(str(cnt + 1) + '. ' + phrase[0])
        cnt += 1
    return res



def showPhrase(wall):
    corpus = textField.get()

    phrases = extractPhrase(corpus)
    
    for phrase in phrases:
        mylist.insert(END, phrase)

    mylist.pack(side = TOP, fill = BOTH)
    #side = TOP,

    scroll_bar.config( command = mylist.yview )

if __name__ == '__main__':

    wall = Tk()
    wall.geometry("1000x1000")
    wall.title('Assignment 1(NLP)')

    font = ('poppins',10,'italic')
    text = ("poppins", 35, "bold")

    text1 = Label(wall,text="Natural Language Processing",font=('Helvetica',30,'bold'))
    text1.pack()
    text2 = Label(wall,text="Debojyoti Biswas(CS2104)",font=('Helvetica',25,'bold'))
    text2.pack()
    text3 = Label(wall,text="Write any text to get top 100 phrases",font=('Helvetica',20,'italic'))
    text3.pack()


    #frame = Frame( wall, width=400, height=400)
    #frame.pack(expand=True, fill='both')
    #frame.pack_propagate(0)
    scroll_bar = Scrollbar(wall)
    
    scroll_bar.pack( side = RIGHT,
                    fill = Y )
    
    mylist = Listbox(wall, 
                    yscrollcommand = scroll_bar.set )

                    
    textField = Entry(wall, justify='center', width = 20, font = text)
    textField.pack(pady = 20)
    textField.focus()
    textField.bind('<Return>', showPhrase)




    #label1 = Label(wall, font=font)
    #label1.pack()
    #label2 = Label(wall, font=font)
    #label2.pack()
    wall.configure(bg='#856ff8')
    wall.mainloop()


