
def main():
	file = input("file:\n")
	bits = text_to_bits(file)
	len_t = int(len(bits) / 8)
	while(len(bits) % 6 != 0):
		bits += '0'
	sharp = 0
	n = 6
	bits6 = [bits[i:i + n] for i in range(0, len(bits), n)]
	while ((len_t + sharp) % 3 != 0):
		sharp+=1
	bits6 = [two_to_ten(elem) for elem in bits6]
	name = f'base64_{"_".join(file.split("."))}.txt'
	with open(name, 'w') as fin:
		fin.write(base64enc(bits6) + "".join(['=' for e in range(sharp)]))
	print(f"Saved as {name}")

def text_to_bits(file, encoding='utf-8', errors='surrogatepass'):
	f = open(file, 'r')
	text = "".join([line for line in f.readlines()])
	bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
	return bits.zfill(8 * ((len(bits) + 7) // 8))

def two_to_ten(el: str):
	return sum([int(el[i])*2**(len(el)-i-1) for i in range(len(el))])

def base64enc(inp: list):
	base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	return "".join([base[c] for c in inp])

if __name__ =="__main__":
	main()