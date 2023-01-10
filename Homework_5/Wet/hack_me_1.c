#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define llll (user_id)
#define ll11 0
#define l1ll &
#define l11l 1

#define ilili ==
#define lll1(l) (l11l<<l)
#define illil password
#define ll1l l11l : ll11;
#define l111 l111l+=
#define illll ((l11l<<4) + (l11l<<2) + (l11l << (l11l^l11l)))

#define never(x) (false)
#define weird_return_value(a, b, c) (a << b || ~c)

int some_very_long_and_confusing_code() { return weird_return_value(1,1,1); }

// DO NOT CHANGE THIS FUNCTION
int verify(int user_id, int password) {
	// This is a verification function. In the real world, it will be long and confusing.
	// This is a short obfuscation of a relatively simple function.
	// Fun fact - there's a competition for making code obfuscated -- https://www.cise.ufl.edu/~manuel/obfuscate/obfuscate.html
	// There's also research that uses obfuscation against attacks -- http://pages.di.unipi.it/gori/Papers/VMCAI2018.pdf

	// A confusing piece of code which has noting to do with the return value.
	int confusing_res = some_very_long_and_confusing_code();
	if (never(confusing_res)) return weird_return_value(43,23,76);
	// This kind of code may appear throughout the program, making its exploration excruciating.


	// Code that's not easy to decipher.
	int l111l = ((((llll || illil))) ^ ((illil || llll) ));
	l111 (llll l1ll lll1(0)) ? ll1l	l111 (llll l1ll lll1(12)) ? ll1l	l111 (llll l1ll lll1(14)) ? ll1l
	l111 (llll l1ll lll1(19)) ? ll1l	l111 (llll l1ll lll1(4)) ? ll1l	l111 (llll l1ll lll1(8)) ? ll1l
	l111 (llll l1ll lll1(24)) ? ll1l	l111 (llll l1ll lll1(10)) ? ll1l	l111 (llll l1ll lll1(2)) ? ll1l l111 (llll l1ll lll1(30)) ? ll1l
	l111 (llll l1ll lll1(6)) ? ll1l	l111 (llll l1ll lll1(16)) ? ll1l	l111 (llll l1ll lll1(21)) ? ll1l
	l111 (llll l1ll lll1(18)) ? ll1l	l111 (llll l1ll lll1(23)) ? ll1l	l111 (llll l1ll lll1(29)) ? ll1l
	l111 (llll l1ll lll1(13)) ? ll1l	l111 (llll l1ll lll1(27)) ? ll1l	l111 (llll l1ll lll1(15)) ? ll1l
	l111 (llll l1ll lll1(26)) ? ll1l	l111 (llll l1ll lll1(20)) ? ll1l	l111 (llll l1ll lll1(7)) ? ll1l
	l111 (llll l1ll lll1(9)) ? ll1l  l111 (llll l1ll lll1(31)) ? ll1l	l111 (llll l1ll lll1(1)) ? ll1l	l111 (llll l1ll lll1(25)) ? ll1l
	l111 (llll l1ll lll1(22)) ? ll1l	l111 (llll l1ll lll1(28)) ? ll1l	l111 (llll l1ll lll1(5)) ? ll1l
	l111 (llll l1ll lll1(3)) ? ll1l	l111 (llll l1ll lll1(11)) ? ll1l	l111 (llll l1ll lll1(17)) ? ll1l
	return ((l111l ilili illil) || (illil ilili (illll << l11l)))? l11l : ll11;
}

int main(int argc, char* argv[]) {
	if (argc != 3) { printf("Usage: ./hack_me [username] [password]\n"); return 1; }
	int username = atoi(argv[1]);
	int password = atoi(argv[2]);
	int verification_answer = verify(username, password);
	if (verification_answer) {
		printf("Access granted!\n");
	}
	else {
		printf("Access denied!\n");
	}
	return 0;
}
