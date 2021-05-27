#include <stdlib.h>
#include <stdio.h>
#define PXL 3

void fillCol(unsigned *** arr, size_t col, size_t row) {
  unsigned ** rowarr = NULL;
  for (int i = 0; i < col; i++) {
    rowarr = realloc(rowarr, row * sizeof(*rowarr));
    arr[i] = rowarr;
    rowarr = NULL;
  }
}

void fillRow(unsigned *** arr, size_t col, size_t row) {
  unsigned * pxlarr = NULL;
  for (int k = 0; k < col; k++) {
    for (int i = 0; i < row; i++) {
      pxlarr = realloc(pxlarr, PXL * sizeof(*pxlarr));
      // pass in 0 values to pxlarr
      for (int j = 0; j < PXL; j++) {
	pxlarr[j] = 0; // this is where the value is assigned
      }
      arr[k][i] = pxlarr;
      pxlarr = NULL;
    }
  }
}

void freeArr(unsigned *** arr, size_t col, size_t row) {
   for (int i = 0; i < col; i++) {
     for (int j = 0; j < row; j++) {
       free(arr[i][j]);
       }
     free(arr[i]);
     }
   free(arr);
}

// displayBuffer
/* int main(int argc, char ** argv) { */
/*   if (argc < 3) { */
/*     fprintf(stderr, "Usage: col row"); */
/*     return EXIT_FAILURE; */
/*   } */

/*   size_t col = atoi(argv[1]); */
/*   size_t row = atoi(argv[2]); */

/*   unsigned *** colarr = malloc(col * sizeof(*colarr)); */
  
/*   fillCol(colarr, col, row); */
/*   fillRow(colarr, col, row); */
/*   freeArr(colarr, col, row); */

void print(unsigned *** arr, size_t col, size_t row) {
  int j;
  for (int i = 0; i < col; i++) {
      printf("[");
     for (j = 0; j < row; j++) {
       for (int k = 0; k < PXL; k++) {
	 printf("%d ", arr[i][j][k]);
       }
       printf("]");
       printf("\n");
     }
     printf("\n");
   }
}

void displayBuffer(long * dimensions) {

  long col = dimensions[0];
  long row = dimensions[1];

  unsigned *** colarr = malloc(col * sizeof(*colarr));
  
  fillCol(colarr, col, row);
  fillRow(colarr, col, row);
  
  
  freeArr(colarr, col, row);
  free(dimensions);
  
  return EXIT_SUCCESS;
}
