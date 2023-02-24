import time
import random

while True:
    quoteServiceFile = open("quoteService.txt", "r+")
    contents = quoteServiceFile.readline()
    run = "run"
    quoteServiceFile.close()

    if contents == run:
        time.sleep(3)
        print(contents)
        ranNum = random.randrange(1, 100)
        modNumber = ranNum % 10  # 10 quotes available
        directory = open('quotes.txt', mode='r', encoding='utf-8-sig').readlines()
        quote = directory[modNumber-1]
        open('quoteService.txt', 'w').close()
        writeQuote = open('quoteService.txt', 'r+')
        writeQuote.write(quote)
        writeQuote.close()


