res = {}
# (str(bin(int(a)))[-10:-7])
with open('codes.txt', 'r') as f:
	for line in f.readlines():
		res[line] = str(bin(int(line)))[-3:]
for key, val in res.items():
	if val == '000' or val == '001' or val == '101':
		print(key)
