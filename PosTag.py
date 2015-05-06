import nltk,re

# WSD Project ML_IN_CL

# This module accepts a input string from command line.
# Tokenizes input and does part of speech(POS) tagging using NLTK library.

''' List of POS Tags
POS Tag     Description 
CC      coordinating conjunction 
CD      cardinal number 
DT      determiner 
EX      existential
FW      foreign word 
IN      preposition/subordinating conjunction
JJ      adjective 
JJR         adjective, comparative 
JJS         adjective, superlative 
LS      list marker 
MD      modal 
NN      noun, singular
NNS         noun plural
NNP         proper noun
NNPS        proper noun
PDT         predeterminer
POS         possessive ending 
PRP         personal pronoun
PRP$        possessive pronoun 
RB      adverb
RBR         adverb, comparative 
RBS         adverb, superlative 
RP      particle 
TO      to 
UH      interjection 
VB      verb, base form 
VBD         verb, past tense 
VBG         verb, gerund/present participle
VBN         verb, past participle 
VBP         verb, sing. present, non-3d 
VBZ         verb, 3rd person
WDT         wh-determiner 
WP      wh-pronoun
WP$         possessive
WRB         wh-abverb '''

# Given Input >> "I am a boy"
# Expected Output >>  [('I', 'PRP'), ('am', 'VBP'), ('a', 'DT'), ('boy', 'NN')]

def pos_tag(var):
    #var = raw_input("Please enter input string ");
    
    if(var != ""):  
        token = nltk.word_tokenize(var)
    else:
        print "Empty string entered. "
        return;

    
    tagged = nltk.pos_tag(token)
    
    #print "POS tagged: ", tagged
    return tagged


#================================================

def getPOS(preList, postList, currWord):
    newList = preList + [currWord] + postList
    totalLen = len(newList)
    str = " ".join(newList)
    tagged = pos_tag(str)
    
    featureSet = []
    if len(preList) > 3:
    	featureSet.append(tagged[len(preList)-3][1])
    else:
        featureSet.append("*")

    if len(preList) > 2:
	featureSet.append(tagged[len(preList)-2][1])
    else:
        featureSet.append("*")

    if len(preList) > 1:
	featureSet.append(tagged[len(preList)-1][1])
    else:
        featureSet.append("*")

    
    if len(postList) > 0:
	featureSet.append(tagged[len(preList)+1][1])
    else:
        featureSet.append("*")

    if len(postList) > 1:
	featureSet.append(tagged[len(preList)+2][1])
    else:
        featureSet.append("*")

    if len(postList) > 2:
	featureSet.append(tagged[len(preList)+3][1])
    else:
        featureSet.append("*")

    
    return featureSet
    

    
#================================================


if __name__ == "__main__":
    pos_tag("Extensity  ( for example the size of a patch of light )  usually correlates with the number and spatial distribution of receptors activated .  Finally ,  duration is correlated with the period of time for which the relevant neurones are active .  ( I am leaving aside phenomena such as accommodation , whereby a constant stimulus when sustained may <head>activate</head> the nervous system progressively less intensively , with a corresponding reduction in the perceived intensity of the stimulus . These ,  and other features of adaptation ,  do not invalidate the underlying conceptual framework .  )  The earliest psychophysical observations demonstrated a correlation between the intensity of the physical stimulus and  subjective reports of the intensity of the resultant experience .");
    
