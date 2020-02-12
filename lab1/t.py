res = {}
a = input('chislo?\n')
while (a != '#'):
	try:
		res[a] = (str(bin(int(a)))[-10:-7])
		a = input('chislo?\n')
	except: continue
for key, value in res.items():
	if value == '100':
		print(key)
