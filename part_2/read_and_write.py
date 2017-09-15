with open('example.txt','r', encoding = 'utf-8') as myfile:
	text = ''
	count = 0
	for line in myfile:
		content = myfile.read()
		print (content)
		text = text + str (content)
		number_words = text.split(' ')	
		count = count + len (number_words) 
	print(text)
	print (count)
 #number_words = text.split(' ')
#print(number_words)
	words = myfile.read()
	print (words)