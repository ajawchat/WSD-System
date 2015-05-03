import re

def getAccuracy(fileName):
	fileOpen = open(fileName, "r").read()
    
	accuracy = []

        words = re.findall("Examine datafile[\" \"]+'./trainingData/[\w]+.[\w].train'",fileOpen)
        accuracyVal = re.findall("overall accuracy:[" " ]+[\d]+.[\d]+",fileOpen)
        
        for i in range(len(words)):
		word = words[i].split("/")[-1].split(".train")[0]
		val = re.findall("[\d]+.[\d]+",accuracyVal[i])[0]
                accuracy.append([word,val])
		print word," "*(20-len(word)),val,"..........",i+1
	
	for i in range(len(accuracy)):
		print accuracy[i][1]
	

if __name__ == "__main__":
	getAccuracy("file")
	
