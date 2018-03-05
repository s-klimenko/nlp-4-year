from nltk.corpus import wordnet

tea = wordnet.synsets('tea') #1
coffee = wordnet.synsets('coffee') #1
container = wordnet.synsets("container") #1
artifact = wordnet.synsets("artifact") #1

for ss in tea:
    print(ss, ss.definition())

for ss in coffee:
    print(ss, ss.definition())

for ss in container:
    print(ss, ss.definition())

for ss in artifact:
    print(ss, ss.definition())
        

tc = tea[0].lch_similarity(coffee[0])
ca = container[0].lch_similarity(artifact[0])
print('---')
print('tea-coffee: ', tc)
print('container-artifact', ca)
print('разница: ', tc-ca)
