import time
running = True
while running is True:
    def uiFunction():
        open("quoteService.txt" ,"w").close()
        quoteService = open("quoteService.txt", "r+")
        quoteService.write("run")
        quoteService.close()
        time.sleep(5)
        run = "run"
        quoteService = open("quoteService.txt", 'r+')
        quote = quoteService.readline()
        if quote != run:
            time.sleep(3)
            print(quote)
            quoteService.close()

    status = uiFunction()
    if status is False:
        running = False
