import os
import decimal
import math

def main():
	file = input("Enter name of file:\n")
	totalSYM = countSymbols(file)
	SYMdict = SymbolsDict(file)
	freq = SYMdict.copy()
	for key in freq:
		freq[key] = decimal.Decimal(freq[key]) / decimal.Decimal(totalSYM)
	entropy = Entropy(freq)
	### out
	print("Частоты:\n")
	for key, value in freq.items():
		print(f"{key}: %.10f" % value)
		#print("{0}: {1}".format(key, value))
	print("\nСредняя энтропия:\n\t %.2f" % entropy)
	print(f"\nКоличество информации\n \tvs\t \nРазмер файла\t\n\n %.2f" % (entropy * totalSYM / 8) +  f" ### %.2f" % os.path.getsize(file))

def Entropy(freq: dict):
	entropy = 0
	for key in freq.keys():
		entropy += freq[key] * decimal.Decimal(math.log2(decimal.Decimal(1) / freq[key]))
	return entropy

def countSymbols(file: str):
	f = open(file, 'r')
	return sum([sum(1 for s in line) for line in f.readlines()])

def SymbolsDict(file: str):
	f = open(file, 'r')
	sd = {}
	for line in f.readlines():
		for sym in line:
			if sym not in sd.keys():
				sd[sym] = 1
			else:
				sd[sym] += 1
	return sd

if __name__ == "__main__":
	main()