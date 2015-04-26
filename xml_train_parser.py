import re



if __name__ == "__main__":

    document = "ajTrain.train"

    fileOpen = open(document,"r")

    # Initialize an empty list of words. We will add words as we parse the file
    wordsList = []

    currWordNow = ""

    for line in fileOpen.readlines():
        #print line
        currWord = ""
        currWordList = re.findall("<instance id=\"[\w]+.[a-z].[\w]+.[\d]+\"",line)
        if len(currWordList) != 0:
            #print currWordList[0].split('"')[1].split(".") 
            currWord = currWordList[0].split('"')[1].split(".")
            currWord = currWord[0] + "." + currWord[1]
            print currWord

        #check if the currWord == currWordNow
        if currWord == currWordNow:
            print "same"
        elif currWord != currWordNow and currWord != "":
            print "not same"
            currWordNow = currWord
            print "changed the global comparator to ",currWord
            # create a new file for the currWord.train
            fileWrite = open(currWord+".train","w")
            
            
