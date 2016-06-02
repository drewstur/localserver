import urllib

def read_text():
    quotes = open("C:\Users\DrewDesktop\Documents\GitHub\localserver\python\lesson - use classes\profanity.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

    #if "true" in output:
        #print("Profanity detected!!")
    #elif "false" in output:
        #print("No profanity detected!!")
    #else:
        #print("Couldn't scan document")
        
read_text()

