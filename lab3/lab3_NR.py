

import subprocess as s
from time import sleep


#s.call(['qsub', '-I -l nodes=1:ppn=1,walltime=00:30:00'])
s.call(['cd', 't4'])
s.call(['ml', 'icc'])

file = 'integral.cpp'
instructions = ['SSE2', 'SSE3', 'SSSE3', 'SSE3_ATOM', 'SSSE3_ATOM',
				'ATOM_SSSE3', 'ATOM_SSE4.2', 'SSE4.1', 'SSE4.2', 'AVX',
				'CORE-AVX-I', 'CORE-AVX2', 'CORE-AVX512', 'MIC-AVX512', 'COMMON-AVX512']

def compile():
	for optim in range(4):
		for instr in instructions:
			time = ''
			pwd = s.check_output(['pwd'])[0:-1]
			res = s.check_output(['icc', '-O{optim} -x{instr} {pwd}/{file} -o integral'.
								 format(optim=optim, instr=instr, file=file, pwd=pwd)])
			if "Unrecognized keyword" not in res:
				with open('log.txt', 'a') as f:
					with open('tmp', 'r') as tmp:
						time = [line for line in tmp.readlines()]
						time = time[1]
					f.write('{optim} :: {instr} :: time')
					# /usr/bin/time -p ./inte 2>tmp && cat tmp




