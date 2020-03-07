import base64
import math

base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def main():
	with open(input("text file?\n"), "r") as f:
		content = f.read()
	print (content)

	asciibinary = ''.join(['0' * (8 - len(str(bin(ord(c)))[2:])) + str(bin(ord(c)))[2:] for c in content])

	if (len(asciibinary) % 6 != 0):
		asciibinary += '0' * (6 - (len(asciibinary) % 6))
	base64string = ""
	base64string = base64enc(asciibinary)
	if len(content) % 3 != 0:
		base64string += '=' * (3 - len(content) % 3)
	print (base64.b64encode(content.encode()).decode())
	print (base64string)
	if base64string == base64.b64encode(content.encode()).decode():
		print ("True")
	else:
		print ("False")
	print("Base64 ", Quantity(base64string), "Byte")
	print("ASCII ", Quantity(content), "Byte")

	with open("archive file?\n", "rb") as archive:
		archivecontent = archive.read()
	print("Archive Base64 ", Quantity(archivecontent), "Byte")
	print(archivecontent)

def base64enc(inp: str):
	base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	return "".join([base[int(c)] for c in inp])

def Quantity(base64string):
	symbols = list(set(base64string))
	pairs = {}
	Entropy = 0
	OverallLength = len(base64string)
	for i in symbols:
		pairs[i] = base64string.count(i)
	for r in pairs:
		Entropy -= (pairs[r] / OverallLength) * math.log2(pairs[r] / OverallLength)
	return Entropy * OverallLength / 8

if __name__ == '__main__':
	main()
