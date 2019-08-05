#To search for data in messages.json
import json
with open('qyTJBtF1bJgx_message') as data:
	data = data.read()
	s = json.loads(data)
	partic = s[0]['participants']
	print(partic)
	for i in range(0,len(s)):
		n = s[i]['participants']
		print(n)
print(len(s))
