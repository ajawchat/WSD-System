# Program to extract and arrange the required data from the XML and arrange it into a space delimited format

import xml.etree.ElementTree as ET

#global hash tables to store the word counts and occurrences and the mapping of the ids to the numbers
bag_of_words = {}
cntr_words = 0
id_mapping = {}
cntr_id = 0


##===============================================

def removePunctuations(strList):
    # We keep the comma, as it provides pauses in the text
    punctuation = [".",")","(","","-","\n"]
    # convert each string to lowercase, for better matching
    newList = [item.lower().replace("\n","") for item in strList if item not in punctuation]
    return newList

##===============================================


def extractFeatures(context):
    global bag_of_words, cntr_words, id_mapping, cntr_id

    #--------------------------------------------------------------
    
    # Clean the context for getting the POS tags. It does not contain the $$head$$ string for processing
    posContext = context.replace("$$head$$","")
    
    #--------------------------------------------------------------
    

    # Split the string based $$head$$ as it differentiates the word we are looking for from the rest of the string
    context = context.split("$$head$$")

   
    ## We split the first and the last part to get the relevant features (words)
    part1 = context[0].split(" ")
    part2 = context[2].split(" ")

    #clean the lists to represent what we want. Removing empty strings, punctuations
    # We keep commas as suggested by Professor
    newpart1 = removePunctuations(part1)
    newpart2 = removePunctuations(part2)
    
    #print newpart1
    #print newpart2

    # Append the terms as the features

    result = []

    len1 = len(newpart1)
    len2 = len(newpart2)

    #This appends the 3rd word before the target word
    if len1 > 3:
        result.append(newpart1[-3])
    else:
        result.append("")

    #This appends the 2nd word before the target word
    if len1 > 2:
        result.append(newpart1[-2])
    else:
        result.append("")

    #This appends the 1st word before the target word
    if len1 > 1:
        result.append(newpart1[-1])
    else:
        result.append("")
    

    #This appends the 1st word after the target word
    if len2 > 1:
        result.append(newpart1[0])
    else:
        result.append("")
    
    #This appends the 1st word after the target word
    if len2 > 2:
        result.append(newpart1[1])
    else:
        result.append("")

    #This appends the 1st word after the target word
    if len2 > 3:
        result.append(newpart1[2])
    else:
        result.append("")

    #print result 

    return result
    
    

##===============================================


def processDataBlock(dataBlock):

    global bag_of_words, cntr_words, id_mapping, cntr_id
    
    print "Inside processDataBlock"
    

    fileData = dataBlock
    
    # replace all the <head> --> <<head>> and all the </head> tags to <<head>>
    fileData = fileData.replace("<head>","$$head$$").replace("</head>","$$head$$")
    
    #print fileData

    xmlSlicedData = []
    
    ## Start XML processing now
    root = ET.fromstring(fileData)
    element = root.getiterator()

    
    
    for item in element:
        if item.tag == "instance":
            #print item.find('context').text
            #print "\n\n"
            xmlElem = []
            subRoot = item.getiterator()
            for sub in subRoot:
                if sub.tag == "instance":
                    xmlElem.append(sub.attrib["id"])
                elif sub.tag == "answer":
                    '''
                    #mapping the ids to numbers, if required at all    
                    if id_mapping.get(sub.attrib["senseid"],"NA") == "NA":
                        id_mapping[sub.attrib["senseid"]] = cntr_id
                        cntr_id += 1
                    xmlElem.append(id_mapping[sub.attrib["senseid"]])
                    '''
                    xmlElem.append(sub.attrib["senseid"])
                
                elif sub.tag == "context":
                    if sub.text.count("$$head$$") > 2:
                        index1 = sub.text.index("$$head$$")
                        index2 = sub.text.replace('$$head$$', 'XXX', 1).find('$$head$$')
                        context = sub.text[0:index1-1] + sub.text[index1+8:index2] + sub.text[index2+8:]
                        print context
                        #xmlElem.append(extractFeatures(sub.text))
                    else:
                        print sub.text
                        xmlElem.append(extractFeatures(sub.text))
                
            xmlSlicedData.append(xmlElem)

    
    print xmlSlicedData,"\n\n\n"

    return xmlSlicedData
    
    # Extract the features
    #print id_mapping
    
    #writeToNewFile(xmlSlicedData)
    


    
    
    
