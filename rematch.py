import re

match = re.search(r'iii', 'piiig')
if match:
	print 'found', match.group()

match2 = re.search(r'..g','piiig')
if match2:
	print 'found', match2.group()

match3 = re.search(r'\d\d\d', 'p123g')
if match3: 
	print 'found', match3.group()

match4 = re.search(r'\w\w\w','@@abcd!!')
if match4:
	print 'found', match4.group()

match5 = re.search(r'pr+', 'piiig')
if match5:
	print 'found' match5.group()

match6 = re.search(r'i+', 'piigiiii')
if match6:
	print 'found' match6.group()


