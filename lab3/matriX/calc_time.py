import os
import sys

path = os.path.abspath(os.path.dirname(sys.argv[0]))
lines = [2, 6, 10, 16, 20, 24, 28, 32, 37, 41, 45, 49,53,58,62,66,70,74]
times = []
res = [0]*len(lines)
for file in [ fil for fil in os.listdir(path) if "calc" not in fil]:
	i = 1
	temp = []
	with open(file, 'r') as f: # [5:]
		for line in f.readlines():
			if i in lines:
				temp.append(float(line[5:]))
			i+=1
	times.append(temp)

for i in range(len(times[0])):
	for j in range(len(times)):
		res[i] += times[j][i]
res = [ str(e/5)[:6] for e in res]
with open(os.path.join(path, 'result_calc'), 'w+') as r:
	r.write('\n'.join(res))
