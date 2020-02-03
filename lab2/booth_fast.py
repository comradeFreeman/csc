def main():
	m, r = ten_2_two(int(input("Введите множимое:\n")), int(input("Введите множитель:\n")))
	A = m + ''.join(['0' for i in range(len(r) + 1)])
	print(f"Значение регистра A = {A}")
	S = dop_kod(m) + ''.join(['0' for i in range(len(r) + 1)])
	print(f"Значение регистра S = {S}")
	P = ''.join(['0' for i in range(len(m))]) + r + '0'
	print(f"Значение регистра P = {P}")
	res = cycle_Booth(A, S, P, len(r))
	print(f"Результат произведения {two_2_ten(m)} на {two_2_ten(r)} равен {two_2_ten(res)}")

def dop_kod(a: str):
	inv = ['1' if s == '0' else '0' for s in a]
	inv.reverse()
	for i in range(len(inv)):
		if inv[i] == '1':
			inv[i] = '0'
		else:
			inv[i] = '1'
			break
	inv.reverse()
	return ''.join(inv)

def cycle_Booth(A: str, S: str, P: str, iter: int):
	print(f"Вход в главный цикл вычислений алгоритма Бута\nКоличество итераций цикла = {iter}")
	while iter > 0:
		if P[::-1][:2][::-1] == '01':
			print("ADD. Операция Р = А + Р")
			print(f"{' ' * 22 + A}\n{' ' * 20}+\n{' ' * 22 + P}\n{' ' * 22 + '-' * len(S)}")
			P = plus_binary(A, P)
			print(f"Значение регистра Р = {P}")
		elif P[::-1][:2][::-1] == '10':
			print("SUB. Операция Р = S + Р")
			print(f"{' ' * 22 + S}\n{' ' * 20}+\n{' ' * 22 + P}\n{' ' * 22 + '-' * len(S)}")
			P = plus_binary(S, P)
			print(f"Значение регистра Р = {P}")
		else:
			print("NOP - действия над регистром Р не предпринимаются!")
		P = shift_right(P)
		print(f"Операция P >> 1")
		print(f"Значение регистра Р = {P}")
		iter -= 1
	print("Выход из главного цикла вычислений алгоритма Бута")
	print("Операция P >> 1")
	print(f"*********\n* ОТВЕТ *\n*********\nЗначение регистра Р = 0{P[:len(P) - 1]}")
	return shift_right(P) #P[:len(P) - 1]

def shift_right(a: str):
	return str('0' if a[0] == '0' else '1') + a[:len(a) - 1]

def plus_binary(a: str, b: str):
	res = list()
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
	res.reverse()
	return ''.join(map(str, res))

def minus_1_binary(a: str):
	res = list()
	a = [int(al) for al in a]
	a.reverse()
	dop = 0
	if a[0] == 1:
		a[0] = 0
		a.reverse()
		return ''.join(map(str, a))

	for i in range(len(a)):
		if a[i] == 1:
			if dop == 1:
				dop = 0
				a[i] = 0
			break
		else:
			dop = 1
			a[i] = 1
	a.reverse()
	return ''.join(map(str, a))

def two_2_ten(el: str):
	sign = ''
	if el[0] == '1':
		#el = minus_1_binary(el[1:])
		el = plus_binary(el[1:], dop_kod('0' * (len(el) - 2) + '1'))
		sign = '-'
		el = ['1' if s == '0' else '0' for s in el]
	return sign + str(sum([int(el[i])*2**(len(el)-i-1) for i in range(len(el))]))


def ten_2_two(m: int, r: int, bits=4):
	res_m, res_r = '', ''

	if abs(m) > 7 or abs(r) > 7:
		bits = 8
	if abs(m) > 127 or abs(r) > 127:
		bits = 16
	if abs(m) > 32767 or abs(r) > 32767:
		bits = 32
	if abs(m) > 2147483647 or abs(r) > 2147483647:
		bits = 64
	if abs(m) > 9223372036854775807 or abs(r) > 9223372036854775807:
		bits = 128
	print(f"Для представления чисел в двоичном формате будет использовано {bits} бит(а)")
	print("Представления введённых чисел в двоичном формате:")
	mask = (1 << bits) - 1
	if m < 0:
		res_m = (bin(((abs(m) ^ mask) + 1) & mask))[2:]
	else:
		res_m = bin(m)[2:]
		res_m = ''.join("0" for i in range(bits - len(res_m))) + res_m
	print(f"Множимое число m = {res_m}")
	if r < 0:
		res_r = (bin(((abs(r) ^ mask) + 1) & mask))[2:]
	else:
		res_r = bin(r)[2:]
		res_r = ''.join("0" for i in range(bits - len(res_r))) + res_r
	print(f"Число-множитель r = {res_r}")
	return res_m, res_r


if __name__ == '__main__':
	main()

# def minus_1_binary(a: str):
# 	res = list()
# 	a = [int(al) for al in a]
# 	a.reverse()
# 	dop = 0
# 	if a[0] == 1:
# 		a[0] = 0
# 		a.reverse()
# 		return ''.join(map(str, a))
#
# 	for i in range(len(a)):
# 		if a[i] == 1:
# 			if dop == 1:
# 				dop = 0
# 				a[i] = 0
# 			break
# 		else:
# 			dop = 1
# 			a[i] = 1
# 	a.reverse()
# 	return ''.join(map(str, a))