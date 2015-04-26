import re, processor


if __name__ == "__main__":

    document = "ajTrain.train"

    fileOpen = open(document,"r")

    # Initialize an empty list of words. We will add words as we parse the file
    wordsList = []

    # Maintains the boundaries of a word
    flag = False

    blockData = ""
    
    for line in fileOpen.readlines():
        if "<lexelt item=" in line:
            blockData += line

            currWord = line.split('"')[1]
            wordsList.append(currWord)
            print wordsList

            
        elif "</lexelt>" in line:
            blockData += line
            # Do some processing

            processor.processDataBlock(blockData)    

            print "="*80
            #print blockData
            blockData = ""
        else:
            blockData += line
            
