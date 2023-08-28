#pragma warning(disable:4996)
#include <stdio.h>
int main() {

	int hour, min, sec, time;

	scanf("%d %d %d %d", &hour, &min, &sec, &time);

	sec = sec + time;

	min = min + sec / 60;
	sec %= 60;

	hour = hour + min / 60;
	min %= 60;

	hour %= 24;

	printf("%d %d %d", hour, min, sec);

	return 0;
}