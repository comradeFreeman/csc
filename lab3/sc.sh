#!/bin/bash
ml icc
if [[ $(pwd) != "/home/grid/testbed/tb434/t4" ]]
then
	cd /home/grid/testbed/tb434/t4 
fi
for co in O{1,2,3}
do
	printf "\n**********  -"$co" NO X! **********"
        echo "***********  -"$co" NO X! **********" >> log
	icc -$co integral.cpp -o integral
	/usr/bin/time -p ./integral 2>>log
done

echo "" >> log

for c_o in O{1,2,3}
do
	printf "\n**********  -"$c_o"  **********"
        echo "***********  -"$c_o"  **********" >> log
	for x_opt in SSE2 SSSE3 SSE4.1 SSE4.2 AVX
	do
		icc -$c_o -x$x_opt integral.cpp -o integral
		printf "\n=========  -x"$x_opt"  =========="
		echo "=========  -x"$x_opt"  ==========" >> log
		/usr/bin/time -p ./integral 2>>log
	done
	printf "\n"
done
