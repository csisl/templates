#include <stdio.h>
#include <stdlib.h>

void readFile(char *fileName){
	FILE *fp;
	char buf[255];
	
	fp = fopen(fileName, "r");
	
	if(fp == NULL){
		fprintf(stderr, "Could not open file %s\n", fileName);
		exit(1);
	}
	
	while(fgets(buf, 255, fp) != NULL){
		printf("%s", buf);
	}
	
	fclose(fp);
}

int main(int argc, char *argv[]){

	if(argc < 2){
		printf("Invalid number of arguments\n");
		exit(1);
	}
	
	readFile(argv[1]);

	return 0;
}
