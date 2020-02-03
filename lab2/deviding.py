from time import sleep

def main():
	# A / B
	sleep(1)
	A, B, sign = ten_2_two(int(input("Введите делимое:\n")), int(input("Введите делитель:\n")))
	sleep(1)
	origB = B
	B, k = predvaritelnij_sdvig_delitelya(A, B)
	sleep(1)
	print(f"Значение регистра  B = {B}"), sleep(1)
	minusB = dop_kod_minus(B)
	sleep(1)
	RQ = devision(A, B, minusB, origB, k)
	sleep(1)
	print(f"*********\n* ОТВЕТ *\n*********\nЧастное = {'-' if sign == 1 else ''}{two_2_ten(RQ[int(len(RQ)/2):])}"
		  f"\nОстаток = {two_2_ten(RQ[:int(len(RQ) / 2)])}")

def devision(A: str, B: str, minusB: str, origB: str, k: int):
	print("Переход к основному циклу операции деления!"), sleep(1)
	RQ = ['0' for i in range(len(A) * 2)]
	print(f"Значение регистра RQ = {''.join(RQ)}"),  sleep(1)
	Q = list()
	print("SUM. Операция NC = А + (-B)"), sleep(1)
	print(f"{' ' * 23 + A}\n{' ' * 21}+\n{' ' * 23 + minusB}\n{' ' * 23 + '-' * len(minusB)}"), sleep(1)
	ch_ost = plus_binary(A, minusB)
	print(f"Значение регистра NC = {ch_ost}"), sleep(1)
	RQ = RQ[:int(len(RQ) / 2)] + [el for el in shift_left(''.join(RQ[int(len(RQ) / 2):]))[:-1]]
	if ch_ost[0] == '1': RQ += ['0']
	else: RQ += ['1']
	print(f"Бит {int(len(RQ)/2-1)} регистра NC равен {ch_ost[0]},\nпоэтому {int(len(RQ)/2)} бита регистра RQ смещены влево на 1 бит "
		  f"с потерей 31-го, а бит 0 установлен в {RQ[-1]}"), sleep(1)
	print(f"Значение регистра RQ = {''.join(RQ)}"), sleep(1)
	for i in range(k): # 5.6
		ch_ost = ch_ost[0] + shift_left(ch_ost[1:]) # 5.3
		print(f"SHIFT. {int(len(RQ)/2)} бита регистра RQ смещены влево на 1 бит.\n"
			  f"Младший (0-ой) бит установлен в 0"), sleep(1)
		if ch_ost[0] == '1': # 5.4
			print("SUM. Операция NC = NC + B"), sleep(1)
			print(f"{' ' * 23 + ch_ost}\n{' ' * 21}+\n{' ' * 23 + B}\n{' ' * 23 + '-' * len(B)}"), sleep(1)
			ch_ost = plus_binary(ch_ost, B)
			print(f"Значение регистра NC = {ch_ost}"), sleep(1)
		else:
			print("SUM. Операция NC = NC + (-B)"), sleep(1)
			print(f"{' ' * 23 + ch_ost}\n{' ' * 21}+\n{' ' * 23 + minusB}\n{' ' * 23 + '-' * len(minusB)}"), sleep(1)
			ch_ost = plus_binary(ch_ost, minusB)
			print(f"Значение регистра NC = {ch_ost}"), sleep(1)

		RQ = RQ[:int(len(RQ) / 2)] + [el for el in shift_left(''.join(RQ[int(len(RQ) / 2):]))[:-1]]
		if ch_ost[0] == '1': RQ += ['0']
		else: RQ += ['1']
		print(f"Бит {int(len(RQ) / 2 - 1)} регистра NC равен {ch_ost[0]}, "
			  f"поэтому 32 бита регистра RQ смещены влево на 1 бит "
			  f"с потерей 31-го, а бит 0 установлен в {RQ[-1]}"), sleep(1)
		print(f"Значение регистра RQ = {''.join(RQ)}"), sleep(1)
		if abs(int(two_2_ten(ch_ost))) < abs(int(two_2_ten(origB))):
		# а частное дополняется нулями так, чтобы число разрядов частного равнялось k+1.
			break
	print(f"Значение {len(ch_ost)-1} разряда NC = {ch_ost[0]}"), sleep(1)
	if ch_ost[0] == '1':
		print("В знаковом разряде содержится единица, значит требуется коррекция остатка."), sleep(1)
		print("SUM. Операция NC = NC + B"), sleep(1)
		print(f"{' ' * 23 + ch_ost}\n{' ' * 21}+\n{' ' * 23 + B}\n{' ' * 23 + '-' * len(B)}"), sleep(1)
		ch_ost = plus_binary(ch_ost, B)
		print(f"Значение регистра NC = {ch_ost}"), sleep(1)
	print(f"SHIFT. {int(len(ch_ost))} бита регистра NC смещены вправо на {abs(k)} бит.\n"), sleep(1)
	for i in range(abs(k)):
		ch_ost = shift_right_logic(ch_ost)
	print(f"Значение регистра NC = {ch_ost}"), sleep(1)
	for i in range(int(len(RQ) / 2)):
		RQ[int(len(RQ) / 2) - 1 - i] = ch_ost[len(ch_ost) - 1 - i]
	print(f"Значение регистра RQ = {''.join(RQ)}"), sleep(1)
	return ''.join(RQ)

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

def predvaritelnij_sdvig_delitelya(A: str, B: str):
	A, B = [el for el in A], [bel for bel in B]
	A_k, B_k = 0, 0
	for i in range(len(A)):
		if A[i] == '1':
			A_k = i
			break
	for k in range(len(B)):
		if B[k] == '1':
			B_k = k
			break
	B = ''.join(B)
	for i in range(abs(B_k - A_k)):
		if B_k > A_k:
			B = shift_left(B)
		else:
			B = shift_right_logic(B)
	print(f"Сдвиг регистра B {'влево' if B_k - A_k else 'вправо'} на {abs(B_k - A_k)} бит")
	return B, B_k - A_k

def shift_left(a: str):
	return a[1:len(a)] + '0'

def shift_right_logic(a: str):
	return '0' + a[:len(a) - 1]

def two_2_ten(el: str):
	sign = ''
	if el[0] == '1':
		el = plus_binary(el[1:], dop_kod_minus('0' * (len(el) - 2) + '1'))
		# minus_1_binary(el[1:])
		sign = '-'
		el = ['1' if s == '0' else '0' for s in el]
	return sign + str(sum([int(el[i]) * 2 ** (len(el) - i - 1) for i in range(len(el))]))

def ten_2_two(m: int, r: int, bits=32):
	sign = 0
	if m == 0 or r == 0:
		print("Недопустимые числа!")
		exit(1)
	if m < 0 and r < 0:
		sign = 0
	if (m > 0 and r < 0) or (m < 0 and r > 0):
		sign = 1
	m, r = abs(m), abs(r)
	if abs(m) > 7 or abs(r) > 7:
		bits = 32
	if abs(m) > 2147483647 or abs(r) > 2147483647:
		bits = 64
	if abs(m) > 9223372036854775807 or abs(r) > 9223372036854775807:
		bits = 128
	print(f"Для представления чисел в двоичном формате будет использовано {bits} бит(а)"), sleep(1)
	print("Представления введённых чисел в двоичном формате:"), sleep(1)
	mask = (1 << bits) - 1
	if m < 0:
		res_m = (bin(((abs(m) ^ mask) + 1) & mask))[2:]
	else:
		res_m = bin(abs(m))[2:]
		res_m = ''.join("0" for i in range(bits - len(res_m))) + res_m
	print(f"Делимое: регистр   A = {res_m}"), sleep(1)
	if r < 0:
		res_r = (bin(((abs(r) ^ mask) + 1) & mask))[2:]
	else:
		res_r = bin(abs(r))[2:]
		res_r = ''.join("0" for i in range(bits - len(res_r))) + res_r
	print(f"Делитель: регистр  B = {res_r}"), sleep(1)
	return res_m, res_r, sign

def dop_kod_minus(a: str):
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

if __name__ == '__main__':
	main()