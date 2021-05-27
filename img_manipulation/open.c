#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "read.c"
#include "data.c"

int main(int argc, char ** argv) {
  if (argc < 2) {
    fprintf(stderr, "Provide a file\n");
    return EXIT_FAILURE;
  }
  
  FILE * file = fopen(argv[1], "rb");
  if (file == NULL) {
    fprintf(stderr, "Could not open the file\n");
    return EXIT_FAILURE;
  }

  fseek(file, 0, SEEK_END); // reposition stream position indicator
  // get current position in stream and size of the file
  size_t sz = ftell(file); 
  rewind(file); //set position of stream to the beginning

  //memory allocation to contain the file
  char * buffer = NULL;
  buffer = malloc(sz * sizeof(*buffer));
  if (buffer == NULL) {
    fprintf(stderr, "Memory error\n");
    return EXIT_FAILURE;
  }

  // copy the file into the buffer
  size_t result = fread(buffer, sizeof(char), sz, file);
  if (result != sz) {
   fprintf(stderr, "Read error\n");
   return EXIT_FAILURE;
  } 

  long * dimensions = readBuffer(buffer, sz);
  //displayBuffer(dimensions); not yet implemented
  free(dimensions);

  //display the contents of the buffer
  /* const size_t csz = sz; */
  /* for (size_t i = 0; i < csz; i++) { */
  /*   printf("%d ", buffer[i]); */
  /* } */
  /* printf("\n"); */
  
  size_t * pc = &sz;
  char * data = getData(buffer, pc);

  // display the IDAT chunk
  int cnt = 1;
  for (size_t i = 0; i < sz; i++) {
    cnt++;
    printf("%d ", data[i]);
  }
  printf("cnt = %d", cnt);
  
  free(data);
  
  fclose(file);
  free(buffer);
  return EXIT_SUCCESS;
}
     
  
