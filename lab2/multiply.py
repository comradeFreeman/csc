

def main():
	a = '11001011'
	b = '111000'
	res = list()
	a, b = [e for e in a], [k for k in b]
	#res = [ str(int(el) * int(b[len(b) - 1])) for el in a]
	#for i in range(len(b) - 1):
	#	res = [ el for el in plus_binary('0' + ''.join(res), ''.join([ str(int(k) * int(b[len(b) - 2 - i ])) for k in a]) + '0' * (i + 1))]
	#print(res)
	ser = ''
	for i in range(len(b)):
		res.append([str(int(k) * int(b[len(b) - 1 - i ])) for k in a])
	for q in range(len(res) - 1):
		ser = plus_binary(''.join(res[0]), ''.join(res[q + 1]), q)
		res[0] = [el for el in ser]
	print(ser)

def shift_left(a: str, n: int):
	return a[n:len(a)] + '0'*n

def plus_binary(a: str, b: str, q: int):
	res = list()
	b += '0'*(q+1)
	if len(a) != len(b):
		a = ( '0' * (len(b) - len(a))) + a
	a, b = [int(al) for al in a], [int(bl) for bl in b]
	a.reverse()
	b.reverse()
	dop = 0
	for i in range(len(a)):
		if a[i] + b[i] + dop == 3:
			res.append(1)
			dop = 1
		elif a[i] + b[i] + dop == 2:
			res.append(0)
			dop = 1
		elif a[i] + b[i] + dop == 1:
			res.append(1)
			dop = 0
		else:
			res.append(0)
	if dop == 1:
		res.append(1)
	res.reverse()
	return ''.join(map(str, res))

if __name__ == '__main__':
	main()