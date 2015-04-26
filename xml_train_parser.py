import re, processor
import writeFeatures as WRITE




if __name__ == "__main__":

    # Check if the folder exists or not, if not then create it. Initializing it before running the program as it is necessary
    path = "trainingData"
    if not os.path.exists(path):
        os.makedirs(path)



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

            wordData = processor.processDataBlock(blockData)    

            # Create a new file based on each word and add the feature set to it along with the class id - FOR TIMBL classifier only
            # Method signature => (pathname, data to be stored, fileName/ wordName)
            WRITE.writeTimblFeatures(path, wordData, wordsList[-1])
            
            print "="*80
            #print blockData
            blockData = ""
        else:
            blockData += line
            
