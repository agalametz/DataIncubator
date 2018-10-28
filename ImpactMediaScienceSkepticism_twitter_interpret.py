import numpy as np
import pandas as pd
import re
import operator
import matplotlib.pyplot as plt

def cleanfile(filename):
    f = open(filename+'.json','r')
    line = np.array(f.readlines())
    f.close
    f = open(filename+'_clean.json','w')
    f.write('id,,created_at,,text\n')
    for val in line:
        if val[0:3] == '105': 
            val = val[0:20]+','+val[20:]
            val = val[0:40]+','+val[40:]
            f.write(val)
    f.close

list = ['CNN_climatechange','BBC_climatechange','FoxNews_climatechange','LastWeekTonight_climatechange','CNBC_climatechange','MSNBC_climatechange','CNN_vaccines','BBC_vaccines','FoxNews_vaccines','LastWeekTonight_vaccines','CNBC_climatechange','MSNBC_climatechange','CNN_science','BBC_science','FoxNews_science','LastWeekTonight_science','CNBC_science','MSNBC_science']
for filename in list:
    cleanfile(filename)

list = ['CNN_science','BBC_science','FoxNews_science','LastWeekTonight_science','CNBC_science','MSNBC_science']
countsRT = np.zeros(6)
countstweets = np.zeros(6)
for index,filename in enumerate(list):
    tweet = pd.read_csv(filename+'_clean.json',engine='python',delimiter=',,')
    text = tweet["text"]
    countstweets[index%6] = len(np.array(text))
    for val in text:
        if val[0:3] == 'RT ' or val[0:3] == '"RT': countsRT[index%6] += 1

print(countsRT*100/countstweets)
rate = countsRT*100./countstweets
rate[0]=0
rate[1]=0
bin = np.array(range(7))
x = [0,0,0,0,0,0,0,rate[2],0,0,rate[3],0,0,0,0,0,rate[5]] 
y = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6]
plt.plot(x,y,c='r')
plt.plot([0,0],[6,6],c='w')
plt.scatter([0,0,rate[2],rate[3],0,rate[5]],[1,2,3,4,5,6],c='r')
plt.yticks(range(7),[' ','CNN','BBC','Fox','LWT','CNBC','MSNBC'])
plt.xticks([0,20,40,60,80,100])
#plt.ylabel([1,2,3,4,5,6],[' ',' ',' ',' ',' ',' '])
plt.xlabel('% RT')
#plt.text(10,150,'query = FoxNews/Science')
plt.show()

list = ['FoxNews_science']
keyword = []
for index,filename in enumerate(list):
    tweet = pd.read_csv(filename+'_clean.json',engine='python',delimiter=',,')
    text = tweet["text"]
    for val in text:
#        val.split(" ")
        keyword.append(val)
#keyword = np.array(np.unique(keyword[0:20]))
s=['a','about','above','after','again','against','all','am','an','and','any','are','as','at','be','because','been','before','being','below','between','both','but','by','can','cannot','could','did','do','does','doing','down','during','each','few','for','from','further','had','has','have','having','he','her','here','hers','herself','him','himself','his','how','i','if','in','into','is','it','its','itself','me','more','most','my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours', 'ourselves','out','over','own','same','says','she','should','so','some','such','than','that','the','their','theirs','them','themselves','then','there','these','they','this','those','through','to','too','under','until','up','very','was','we','were','what','when','where','which','while','who','whom','why','with','would','you','your','yours','yourself','yourselves','#FoxNews','RT']

word = {}
for val in keyword:    
    val = str(val)
    val = re.findall(r'\S+',val)
    for val2 in val:
        val2 = val2.replace('"','')
        val2 = val2.replace(',','')
        val2 = val2.replace(':','')
        if not val2 in s and '\xe2' not in val2 and 'https' not in val2 and '@' not in val2:
            if val2 in word:
                word[val2] += 1
            else:
                word[val2] = 1
#print(sorted(word.iteritems(), key=operator.itemgetter(1)))

wordTop20 = []
for val in range(0,21):
    wordTop20.append(sorted(word.iteritems(), key=operator.itemgetter(1))[-val-1])
ind,countsTop20 = zip(*wordTop20)

plt.scatter(range(21),countsTop20)
plt.yticks([0,50,100,150])
plt.xticks(np.array(range(0,21)))#,['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
for val in range(0,21):
    plt.text(val-0.3,countsTop20[val]-10,str(ind[val]),rotation=90)
plt.ylabel('Counts')
plt.xlabel('Rank')
plt.text(10,150,'query = FoxNews/Science')

plt.show()

