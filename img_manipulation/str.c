#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

  char * buffer = malloc(3 * sizeof(*buffer));
  buffer[0] = 'x';
  buffer[1] = 'a';
  buffer[2] = 'd';

    for (int i = 0; i < 3; i++) {
    printf("%c ", buffer[i]);
  }

  printf("%s \n", buffer);

  for (int i = 0; i < 3; i++) {
    char * pc = &buffer[i];
    printf("value: %d \n", *pc);
    printf("%I64d \n", strlen(pc)); // pointer points to where the string begins!
  }
  
  printf("%I64d \n", strlen(buffer));

  // char -> int; int -> str; strlen(str); str->int

  //  if num < 100 -> len = 2; else -> 3; < 10 -> 1

  size_t sz = 1;
  char * str = NULL;
  str = realloc(str, sz * sizeof(*str));
  printf("str: %s\n", str);
  strcpy(str, buffer);
  printf("str: %s\n", str);

  for (int i = 0; i < 10; i++) {
    printf("%c ", str[i]);
  }

  char * str2 = "malloc";
  char * pc = &str[3];
  strcpy(pc, str2);
  printf("str: %s\n", str);

  char str3[]= "";
  strcpy(str3, str2);
  printf("str: %s\n", str3);
  printf("strlen: %I64d\n", strlen(str2));

  int a = -7;
  unsigned char b = -7;
  printf("%b = %u", b);
  
   return 0;
}

