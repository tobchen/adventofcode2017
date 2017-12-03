#include <stdio.h>
#include <stdlib.h>

int main(void) {
	long int size = 2;
	long int x = 2, y = 1;
	long int current = 10;

	long int look_for = 277678; // 277678

	while (1) {
		while (y > -size) {
			++current;
			--y;
			if (current == look_for) goto done;
		}
		while (x > -size) {
			++current;
			--x;
			if (current == look_for) goto done;
		}
		while (y < size) {
			++current;
			++y;
			if (current == look_for) goto done;
		}
		++size;
		while (x < size) {
			++current;
			++x;
			if (current == look_for) goto done;
		}
	}

	done:
	printf("%ld, %ld: %ld\n", x, y, labs(x)+labs(y));

	return 0;
}