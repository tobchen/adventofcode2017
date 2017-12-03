#include <stdio.h>
#include <stdlib.h>

long int* puzzle;
long int puzzle_half_size = 500;

long int set_puzzle(long int pos_x, long int pos_y) {
	long int sum = 0;
	for (long int x = -1; x <= 1; ++x) {
		for (long int y = -1; y <= 1; ++y) {
			if (!(x == 0 && y == 0)) {
				sum += puzzle[(puzzle_half_size + pos_y + y) * (puzzle_half_size * 2) + (puzzle_half_size + pos_x + x)];
			}
		}
	}
	puzzle[(puzzle_half_size + pos_y) * (puzzle_half_size * 2) + (puzzle_half_size + pos_x)] = sum;
	return sum;
}

void simple_set(long int x, long int y, long int value) {
	puzzle[(puzzle_half_size + y) * (puzzle_half_size * 2) + (puzzle_half_size + x)] = value;
}

int main(void) {
	long int size = 2;
	long int x = 2, y = 1;
	long int current;
	
	long int look_for = 277678; // 277678

	puzzle = calloc((puzzle_half_size * 2) * (puzzle_half_size * 2), sizeof(long int));
	// TODO Fill puzzle
	simple_set(-1, -1, 5);
	simple_set(0, -1, 4);
	simple_set(+1, -1, 2);

	simple_set(-1, 0, 10);
	simple_set(0, 0, 1);
	simple_set(+1, 0, 1);

	simple_set(-1, 1, 11);
	simple_set(0, 1, 23);
	simple_set(+1, 1, 25);
	simple_set(+2, 1, 26);

	while (1) {
		while (y > -size) {
			--y;
			current = set_puzzle(x, y);
			if (current > look_for) goto done;
		}
		while (x > -size) {
			--x;
			current = set_puzzle(x, y);
			if (current > look_for) goto done;
		}
		while (y < size) {
			++y;
			current = set_puzzle(x, y);
			if (current > look_for) goto done;
		}
		++size;
		while (x < size) {
			++x;
			current = set_puzzle(x, y);
			if (current > look_for) goto done;
		}
	}

	done:
	printf("%ld, %ld: %ld\n", x, y, current);

	return 0;
}