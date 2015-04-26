import re



if __name__ == "__main__":

    document = "ajTrain.train"

    fileOpen = open(document,"r")

    # Initialize an empty list of words. We will add words as we parse the file
    wordsList = []

    currWordNow = ""
    wordData = ""

    # Loop through the file and gather the data for different words
    for line in fileOpen.readlines():
        #print line
        currWord = ""

        # append the data for a word in the same file and process it and save it as word.train & word.test
        

        currWordList = re.findall("<instance id=\"[\w]+.[a-z].[\w]+.[\d]+\"",line)
        if len(currWordList) != 0:
            #print currWordList[0].split('"')[1].split(".") 
            currWord = currWordList[0].split('"')[1].split(".")
            currWord = currWord[0] + "." + currWord[1]
            print currWord
    
        
        if currWord != currWordNow and currWord != "":
            print wordData
            wordData = ""
            currWordNow = currWord
            print "changed the global comparator to ",currWord
            # create a new file for the currWord.train
            fileWrite = open(currWord+".train","w")
            
        else:
            if "lexelt" not in line:
                wordData += line

    print wordData
            
