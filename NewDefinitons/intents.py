import pandas as pd

ques_formats_pre = [
	'what is ',
	'summary of ',
	'i want summary of ',
	'brief explanation about ',
	'i want to know more about ',
	'summary for the current topic ',
	'more information about ',
	'summary for ',
	'give me summary for ',
	'i want summary for ',
	'what does ',
	'tell me something about ',
	'explain ',
	'elaborate ',
	'can you tell me about ',
	'what do you know about ',
	'what can you tell me about ',
	'do you have information about ',
	'define ',
	'can you define ',
	'give me definition of ',
]

new_ques_formats_pre = [
	'may i please have a definition for ',
	'what is the meaning of ',
	'please define ',
	'tell me the meaning of ',
	'define ',
	'i need to know what ',
	'tell me please what ',
	'what is the definition of ',
	'exactly what does ',
	'tell me what the word ',
	'tell me the definition of ',
	'can you give the definition of ',
	'please share the definition of ',
	'',
	'find what the word ',
	'do you know what ',
	'give me the meaning of ',
	'i would like to know what ',
	'can you tell me what ',
]

new_ques_formats_suff = [
	'',
	'',
	'',
	'',
	' for me please',
	' means',
	' means',
	'',
	' mean',
	' means',
	'',
	'',
	'',
	' means what',
	' mean please',
	' means',
	'',
	' means',
	' means',
]

ques_formats_suff = [
	'?',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	'',
	' mean?',
	'',
	'',
	'',
	'?',
	'?',
	'?',
	'?',
	'',
	'?',
	'',
]



keywords = [
]

non_ques_formats_pre = [
	'How is ',
	'Does ',
	'Why does ',
	'What are the properties of ',
	'What is another name for ',
	'How difficult it is to learn about ',
	'How many hours does it take to learn about ',
	'Are there any more resources for ',
	'What are the uses of ',
	'Can we perceive ',
	'Where can we find ',
	'Are there any applications for ',
	'Properties of ',
	'Uses of ',
	'Location of ',
	'Are there are any pre-requisites for '
]

non_ques_formats_suff = [
	'?',
	' exist in the real world?',
	' behave like that',
	'?',
	'?',
	'?',
	'?',
	'?',
	'?',
	'?',
	'?',
	'?',
	'',
	'',
	'',
	'?',
]

greetings = [
	"Hi",
	"Hi there",
	"Hola",
	"Hello",
	"Hello there",
	"Hya",
	"Hya there",
	"My user is Adam",
	"This is Adam",
	"I am Adam",
	"It is Adam",
	"My user is Bella",
	"This is Bella",
	"I am Bella",
	"It is Bella",
	"How are you?",
	"Hi how are you?",
	"Hello how are you?",
	"Hola how are you?",
	"How are you doing?",
	"Hope you are doing well?",
	"Hello hope you are doing well?",
]


# if(len(non_ques_formats_suff)==len(non_ques_formats_pre)):
# 	print(1)
# if(len(ques_formats_pre)==len(ques_formats_suff)):
# 	print(1)
if(len(new_ques_formats_suff)==len(new_ques_formats_pre)):
	print(1)
with open('./keywords.txt','r') as file1:
	currs = file1.readlines()
	for curr in currs:
		keywords.append(curr.strip())
print(len(keywords))

lst1 = []
lst2 = []

for keyword in keywords:
	# for i in range(len(ques_formats_pre)):
	# 	pre = ques_formats_pre[i]
	# 	suff = ques_formats_suff[i]
	# 	lst1.append(pre+keyword+suff)
	# 	lst2.append('Definition')
	# for i in range(len(non_ques_formats_suff)):
	# 	pre = non_ques_formats_pre[i]
	# 	suff = non_ques_formats_suff[i]
	# 	lst1.append(pre+keyword+suff)
	# 	lst2.append('OOS')
	for i in range(len(new_ques_formats_pre)):
		pre = new_ques_formats_pre[i]
		suff = new_ques_formats_suff[i]
		lst1.append(pre+keyword+suff)
		lst2.append('definition')
df = pd.DataFrame()
df['Text'] = lst1
df['Intent'] = lst2
print(len(lst1))
df.to_csv('./Definition_Intent.csv')
