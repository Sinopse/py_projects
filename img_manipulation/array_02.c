#include <stdlib.h>
#include <stdio.h>

void fillCol(unsigned *** arr, size_t col, size_t row) {
  unsigned ** rowarr = NULL;
  for (int i = 0; i < col; i++) {
    rowarr = realloc(rowarr, row * sizeof(*rowarr));
    arr[i] = rowarr;
    rowarr = NULL;
  }
}

void fillRow(unsigned *** arr, size_t col, size_t row) {
  size_t pxl = 3;
  unsigned * pxlarr = NULL;
  for (int k = 0; k < col; k++) {
    for (int i = 0; i < row; i++) {
      pxlarr = realloc(pxlarr, pxl * sizeof(*pxlarr));
      // pass in 0 values to pxlarr
      for (int j = 0; j < pxl; j++) {
	pxlarr[j] = 0;
      }
      arr[k][i] = pxlarr;
      pxlarr = NULL;
    }
  }
}

void freeArr(unsigned *** arr, size_t col, size_t row) {
   for (int i = 0; i < col; i++) {
     for (int j = 0; j < row; j++) {
       free(arr[col][row]);
       }
     free(arr[col]);
     }
   free(arr);
}

int main() {
  int col = 5;
  int row = 5;

  unsigned *** colarr = malloc(col * sizeof(*colarr));
  
  fillCol(colarr, col, row);
  fillRow(colarr, col, row);
  freeArr(colarr, col, row);

  return 0;
}
