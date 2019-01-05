#include <stdio.h>

#define KRED  "\x1B[31m"
#define KGRN  "\x1B[32m"
#define KYEL  "\x1B[33m"
#define KBLU  "\x1B[34m"
#define KMAG  "\x1B[35m"
#define KCYN  "\x1B[36m"
#define KWHT  "\x1B[37m"

#define RESET "\x1B[0m"

int main() {
	printf(KRED "KRED  \"\\x1B[31m\"\n" RESET);
	printf(KGRN "KGRN  \"\\x1B[32m\"\n" RESET);
	printf(KYEL "KYEL  \"\\x1B[33m\"\n" RESET);
	printf(KBLU "KBLU  \"\\x1B[34m\"\n" RESET);
	printf(KMAG "KMAG  \"\\x1B[35m\"\n" RESET);
	printf(KCYN "KCYN  \"\\x1B[36m\"\n" RESET);
	printf(KWHT "KWHT  \"\\x1B[37m\"\n" RESET);
	
	return 0;
}
