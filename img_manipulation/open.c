#include <stdlib.h>
#include <stdio.h>

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
  long sz = ftell(file); // get current position in stream
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

  // display the contents of the array
  for (int i = 0; i < sz; i++) {
    printf("%d ", buffer[i]);
  }

  fclose(file);
  free(buffer);
  return EXIT_SUCCESS;
}
     
  
