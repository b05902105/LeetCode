#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

int distributeCandies(int *arr, int size){
	int max = size / 2;
	int *map = (int *)malloc(sizeof(int)*(2*100000 + 1));
	memset(map, 0, sizeof(int)*(2*100000 + 1));
	int cnt = 0;

	for (int i = 0; i < size; i++)
		if (!map[arr[i] + 100000]){
			map[arr[i]+100000] = 1;
			cnt += 1;
		}

	return (cnt < max)? cnt : max;

}

int main(){
	int c[] = {6, 6, 6, 6};
	printf("%d\n", distributeCandies(c, 4));

	return 0;
}
