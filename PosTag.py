import nltk

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
    #print "String entered: ", var;
    if(var != ""):  
        token = nltk.word_tokenize(var)
    else:
        print "Empty string entered. "
        return;

    #print "Tokenized data: ", token

    tagged = nltk.pos_tag(token)
    #print "POS tagged: ", tagged

if __name__ == "__main__":
    pos_tag("THIS IS A TEST STRING");
