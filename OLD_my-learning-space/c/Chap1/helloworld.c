#include <stdio.h>
#include <string.h>

void helloWorld(); // Print HelloWorld in console
void readInput(); // Read char input in console
void readInputs(); // Read string input in console
void readLine(); // Read string with space

int  main(){
	//helloWorld();
	//readInput();
	//readInputs();
	readLine();
	return 0;
}

void helloWorld(){
	printf("Hello World !\n");
}

void readInput(){
	int input;
	printf( "Enter a value :");
	input = getchar();
	printf( "\nYou entered: %c, decimale value is : %d \n",input,input);
}

void readInputs(){
	char str[100];
	printf( "Enter values :");
	scanf("%s",str);
	printf( "You entered: %s \n",str);
	
	// --- Use multi input with scanf ---
	int buf;
	printf( "Enter string and integer values :");
	scanf("%s %d", str, &buf);
	printf( "You entered:\n %s %d\n",str,buf);

	// --- Print integer value of string ---
	printf( "Enter values :");
	printf( "--- --- Integer Value  --- ---\n");
	scanf("%s",str);
	for (int i = 0; i < strlen(str); i++)
		printf( "%c : %d\n",str[i],str[i]);
	// other method
	printf( "--- --- Hexa Value --- ---\n");
	for (int i = 0; str[i] != 0; i++)
		printf( "%c : 0x%x\n",str[i],str[i]);
}

void readLine(){
	int length;
	printf("Enter length of string\n");
	scanf("%d", &length);

	printf("%d", length+1);

	char str[length];
	printf("Enter %d characters \n", length);
	scanf("%s", str);
	//scanf("%10[0-9a-zA-Z ]", str);
	//scanf("%[^\n]s",name);
	/*
	char *name;
	scanf ("%m[^\n]s",&name);
	printf ("%s\n",name);
	*/
	printf("%s\n", str);
}

/*
	%d - int (same as %i)
	%ld - long int (same as %li)
	%f - float
	%lf - double[1]
	%c - char
	%s - string
	%x - hexadecimal
*/
