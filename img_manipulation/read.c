#include "read.h"
// define a struct that holds information about a certain image
// e.g. format, size, color etc.x
// use a header file for that

size_t traverseData(unsigned char * arr, size_t arr_size) {
  // store temporary string in temp and the final string in str
  // using malloc so that we can free the memory later
  // and adjust array size accordingly
  char * temp = NULL;
  size_t l = 0;
  char * str = NULL;
  size_t sz = 0;
  int t = 0;
  // determine how many digits the number has
  // from 0 to 255
    for (int i = 0; i < arr_size; i++) { 
      unsigned char num = arr[i];
      if (num < 100 && num > 9) 
	l = 2;
      else if (num < 10)
	l = 1;
      else
	l = 3;
      
      // malloc for temp and str
      temp = realloc(temp, l * sizeof(*temp));
      sz+=l; // adjust size for str
      str = realloc(str, sz * sizeof(*str));
      sprintf(temp, "%x", arr[i]);

      // copy to the malloc'ed str buffer
      char * pc = NULL;
      if (t == 0) { // only first occurrence
	strcpy(str, "0x");
	strcat(str, temp);
	t++;
      }
      else { // for every consecutive value from temp
	pc = &str[strlen(str)];
	strcpy(pc, temp);
      }
    }
        
    long int size = strtol(str, NULL, 0);
    free(arr);
    free(temp);
    free(str);
    return size;
  }

void readFormat(char * buffer) {
  // need only read from 1 to 3 inclusive
  // check the first 8 bytes if they are correct
  // chekc the length of the first IDAT chunk
  char c = buffer[1];
  if (isupper(c))
    c = tolower(c);
  switch (c)
    {
    case 'p':
      printf("<PNG>"); break;
    case 'j':
      printf("<JPG>"); break;
    }
  printf("\n");
}

long int readDimensions(char * buffer, unsigned beg, unsigned end) {
  unsigned char * dimension = NULL;
  size_t l = 0;
  unsigned ind = 0;
  for (; beg < end; beg++) {
    if (buffer[beg] == 0) {
      continue;
    }
    else {
      l++; 
      dimension = realloc(dimension, l * sizeof(*dimension));
      dimension[ind] = buffer[beg];
      ind++;
    }
  }
  long int dim = traverseData(dimension, l);
  return dim;
}

long * readBuffer(char * buffer, size_t sz) {
  readFormat(buffer); // use enum for formats? PNG 0 JPEG 1 etc.
  long * dimensions = malloc(2 * sizeof(*dimensions));
  long int width = readDimensions(buffer, WMIN, WMAX);
  long int height = readDimensions(buffer, HMIN, HMAX);
  dimensions[0] = width;
  dimensions[1] = height;

  printf("Width: %ld; Height: %ld", width, height);
  printf("\n");
  return dimensions;
}
