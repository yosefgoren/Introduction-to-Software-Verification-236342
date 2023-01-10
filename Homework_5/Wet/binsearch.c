#define SIZE (127)
int binsearch(char x) {
	char a[SIZE];
	char low=0, high=SIZE;
	
	while(low < high) {
		char middle = low+high;
		middle /= 2;

		if (a[middle]<x)
			high = middle;
		else if (a[middle]>x)
			low = middle + 1;
		else // a[middle]==x
			return middle;
	}
	return -1;
}
