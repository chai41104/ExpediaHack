import nltk
import numpy as np
from nltk.tag import StanfordNERTagger
import re
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
ex = 'I want to biook a hotel Saurav Zangeneh in London on the 28th of February, to 17th of August'
st = StanfordNERTagger('/Users/sauravzangeneh/Downloads/stanford-ner-2018-10-16/classifiers/english.muc.7class.distsim.crf.ser.gz',
					   '/Users/sauravzangeneh/Downloads/stanford-ner-2018-10-16/stanford-ner.jar',
					   encoding='utf-8')

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = st.tag(sent)
    return sent

processed_location=preprocess(ex)
print(processed_location)
start_date=0
for items in processed_location:
	if items[1]=='LOCATION':
		print items[0]

chec=np.array([int(items[1]=='DATE') for items in processed_location])
selection_number=sum(chec)/2
searchval=True
ii = np.where(chec == searchval)[0]
start_date=np.array(processed_location)[ii[0:sum(chec)/2+1]]
end_date=np.array(processed_location)[ii[sum(chec)/2+1:]]

start_date_day=0
start_date_month=0
for element in start_date:
	t=''.join(re.findall(r'\d+',element[0].tostring()))
	if len(t)==0:
		temp=''.join(re.findall(r'[a-zA-Z]+',element[0].tostring()))
		if len(temp)>=3:
			start_date_month=temp
	else:
		start_date_day=t
print(start_date_day)
print(start_date_month)
# print(end_date)
# print(start_date)

