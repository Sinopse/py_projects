#include <stdlib.h>
#include <stdio.h>

void fillRow(unsigned ** arr, size_t row, size_t pxl) {
 
  unsigned * pxlarr = NULL;
  for (int i = 0; i < row; i++) {
    pxlarr = realloc(pxlarr, pxl * sizeof(*pxlarr));
    // pass in 0 values to pxlarr
    for (int j = 0; j < pxl; j++) {
      pxlarr[j] = 0;
    }
    arr[i] = pxlarr;
    pxlarr = NULL;
  }
}  

void fillCol(unsigned *** arr, size_t col, size_t row) {
  unsigned ** rowarr = NULL;
  for (int i = 0; i < col; i++) {
    rowarr = realloc(rowarr, row * sizeof(*rowarr));
    arr[i] = rowarr;
    rowarr = NULL;
  }

  //fill each row
  for (int j = 0; j < col; j++) {
    fillRow(arr[j], row, 3);
  }
}

void print(unsigned *** arr, size_t col, size_t row) {
  int j;
  for (int i = 0; i < col; i++) {
      printf("[");
     for (j = 0; j < row; j++) {
       for (int k = 0; k < 3; k++) {
	 printf("%d ", arr[i][j][k]);
       }
       printf("]");
       printf("\n");
     }
     printf("\n");
   }
}
x
void freeArr(unsigned *** arr, size_t col, size_t row) {
   for (int i = 0; i < col; i++) {
     for (int j = 0; j < row; j++) {
       //  for (int k = 0; k < 3; k++) {
       //free(arr[col][row][k]);
       //}
       free(arr[col][row]);
       }
     free(arr[col]);
     }
   free(arr);
}

// testing an array representing an image
int main(int argc, char ** argv) {
  if (argc < 3) {
    fprintf(stderr, "Usage: col row");
    return EXIT_FAILURE;
  }

  size_t col = atoi(argv[1]);
  size_t row = atoi(argv[2]);
  //  size_t col = 5, row = 5;
  unsigned *** colarr = malloc(col * sizeof(*colarr));

  fillCol(colarr, col, row);
   // changing random values
  colarr[3][3][1] = 255;
  
  print(colarr, col, row);
  // check memory!
  freeArr(colarr, col, row);
      
  return EXIT_SUCCESS;
}

  
  
  
