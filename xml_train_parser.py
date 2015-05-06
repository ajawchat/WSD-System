import re, processor, os
import writeFeatures as WRITE
import processorTest


if __name__ == "__main__":

    # Check if the folder exists or not, if not then create it. Initializing it before running the program as it is necessary
    path = "testData"
    if not os.path.exists(path):
        os.makedirs(path)

    document = ""	

    if path == "trainingData":
	document = "./DATA/EnglishLS.train"
    else:
	document = "./DATA/EnglishLS.test"


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
            
	    if path == "trainingData":
            	wordData = processor.processDataBlock(blockData, wordsList[-1])
            else:
		wordData = processorTest.processDataBlock(blockData, wordsList[-1])    
             
            # Create a new file based on each word and add the feature set to it along with the class id - FOR TIMBL classifier only
            # Method signature => (pathname, data to be stored, fileName/ wordName)

            if path == "trainingData":
		WRITE.writeTimblFeatures(path, wordData, wordsList[-1])
	    else:
		WRITE.writeTimblFeaturesTest(path, wordData, wordsList[-1])
            
            print wordsList
               
            print "="*80
            #print blockData
            blockData = ""
        else:
            blockData += line
            
