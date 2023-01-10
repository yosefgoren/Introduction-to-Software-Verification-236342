ID1=0

cur: part_5b

part_2:
	cbmc hack_me_2.c

part_5a:
	cbmc --bounds-check predictable.c
	
part_5b:
	cbmc --unwind 1 --no-unwinding-assertions --function binsearch --bounds-check binsearch.c