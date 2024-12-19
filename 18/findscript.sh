# well
#

i=1024
maxlines=$(wc -l < input.txt.large)
echo "I: $i, maxlines: $maxlines"

testfile="input.txt"
while (( i < maxlines )) 
do
	echo "At Line: $i"
	head -n $i input.txt.large > $testfile
	python3 ./18a.py 2>&1 >/dev/null
	res=$?	
	if (( res == 1 ))
	then
		echo "res: $res"
		echo "Line: $i"
		echo "Result is: $( tail -n 1 < $testfile )"
		break
	fi	
	i=$((i + 1))
done

