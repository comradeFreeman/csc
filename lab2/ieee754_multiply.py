import re


def main():
	a, sign_a, exp_a, m_a = convert_to_ieee754(float(input("Введите множимое:\n")))
	b, sign_b, exp_b, m_b = convert_to_ieee754(float(input("Введите множитель:\n")))
	exp_a += 127
	exp_b += 127
	print(f"Значение множимого в формате IEEE754:\n{' ' * 15}a = {a}")
	print(f"Значение множителя в формате IEEE754:\n{' ' * 15}b = {b}")
	x_new = multiply('1' + m_a, '1' + m_b)
	x_new_unc = x_new
	exp_new = 0
	if x_new[0] == '1':
		x_new = x_new[1:]
		exp_new = 1
	x_new = x_new[:23]
	exp_pr = ten_2_two(exp_a + exp_b, 8)
	exp_new = ten_2_two(exp_a + exp_b - 127 + exp_new, 8)
	print(f"Произведение мантисс (неурезанное):\n{(' ' * 36)}1(.){m_a}"
		  f"\n{' ' * 34}*\n{' ' * 36}1(.){m_b}\n{' ' * 16 + '-' * len(x_new_unc)}\n"
		  f"{' ' * 16 + ''.join(x_new_unc)}")
	print(f"Произведение мантисс (урезанное до 23-х бит) + нормализация:\n{' ' * 40}{x_new}")
	print(f"Сумма экспонент множимого и множителя:\n{(' ' * 36)}{ten_2_two(exp_a, 8)}"
		  f"\n{' ' * 34}+\n{' ' * 36}{ten_2_two(exp_b,8)}\n{' ' * 35 + '-' * len(exp_pr)}\n"
		  f"{' ' * 35 + ''.join(exp_pr)}")
	print(f"Значение экспоненты после коррекции и нормализации мантиссы:\n{' ' * 36}{exp_new}")
	print(f"Результат произведения в формате IEEE754:\n{' ' * 19}{sign_a ^ sign_b}{exp_new}{x_new}")

def multiply(a: str, b: str):
	res = list()
	a, b = [e for e in a], [k for k in b]
	ser = ''
	for i in range(len(b)):
		res.append([str(int(k) * int(b[len(b) - 1 - i])) for k in a])
	for q in range(len(res) - 1):
		ser = plus_binary(''.join(res[0]), ''.join(res[q + 1]), q)
		res[0] = [el for el in ser]
	return ser

def convert_to_ieee754(x: float):
	if x > 0: sign = 0
	else: sign = 1
	exp = 0
	while x > 2.0 or x < 1.0:
		if x > 2.0:
			x /= 2.0
			exp+=1
		if x < 1.0:
			x *= 2.0
			exp-=1
	i = 0
	a = x - 1.0
	x = ''
	while i < 24:
		a *= 2
		if i <= 22:
			if a >= 1.0:
				a -= 1
				x += '1'
			else:
				x += '0'
		else:
			if a > 0.5:
				x = x[:-1] + '1'
		i+=1
	return str(sign) + ten_2_two(int(exp) + 127, 8) + x, sign, exp, x

def ten_2_two(m: int, bits=32):
	mask = (1 << bits) - 1
	if m < 0:
		res_m = (bin(((abs(m) ^ mask) + 1) & mask))[2:]
	else:
		res_m = bin(abs(m))[2:]
	return ('0'*(bits-len(res_m)) if bits > len(res_m) else '') + res_m

def plus_binary(a: str, b: str, q: int): # with overflow
	res = list()
	###
	b += '0' * (q + 1)
	if len(a) != len(b):
		a = ('0' * (len(b) - len(a))) + a
	###
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


