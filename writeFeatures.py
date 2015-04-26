import os

##===============================================
# Function to write feature set for TIMBL classifier for each word in a different .train and .test file
def writeTimblFeatures(path, slicedData, currWord):

    #print currWord

    outputFile = open(path+"/"+currWord+".train","w")

    for element in slicedData:
        length = len(element)
        #print element
        line = ""
        for item in element[len(element)-1]:
            line += str(item)+" "
        line += str(element[1])
        #print line
        outputFile.write(line)
        outputFile.write("\n")

    outputFile.close()

##===============================================


# Function to write feature set for SVM classifier for each word in a different .train and .test file
def writeSVMFeatures(slicedData, currWord):

    print currWord
        
    outputFile = open(currWord+".train","w")

    for element in slicedData:
        length = len(element)
        print element
        line = str(element[1])
        for item in element[len(element)-1]:
            line += " "+str(item)+":1"
        
        print line
        outputFile.write(line)
        outputFile.write("\n")

    outputFile.close()

##===============================================
