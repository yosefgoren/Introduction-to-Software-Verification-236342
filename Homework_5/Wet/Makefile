ID?=0

cur: part_5b

part_2:
	cbmc --trace hack_me_2.c | grep "password="

part_3a:
	cbmc --trace hack_me_3_a.c | grep "password="
part_3b:
	cbmc hack_me_3_b.c

part_5a:
	cbmc --bounds-check predictable.c
	timeout 2 cbmc --bounds-check --function binsearch binsearch.c
	
part_5b:
	cbmc --unwind 1 --no-unwinding-assertions --function binsearch --bounds-check binsearch.c

part_5c:
	cbmc --unwind 2 --trace --no-unwinding-assertions --function binsearch --bounds-check binsearch.c
