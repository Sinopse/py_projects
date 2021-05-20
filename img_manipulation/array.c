#include <stdlib.h>
#include <stdio.h>

void fillCol(unsigned *** arr) {
  unsigned ** rowarr = NULL;


void fillRow(unsigned ** arr) {
  unsigned * pxlarr = NULL;
  for (int i = 0; i < row; i++) {
    pxlarr = realloc(pxlarr, pxl * sizeof(*pxlarr));
    // pass in 0 values to pxlarr
    for (int j = 0; j < pxl; j++) {
      pxlarr[j] = 0;
    }
    rowarr[i] = pxlarr;
    pxlarr = NULL;
  }
}  

// testing an array representing an image
int main() {
  size_t col = 5, row = 5, pxl = 3;
  unsigned *** colarr = malloc(col * sizeof(*colarr));
  unsigned ** rowarr = malloc(row * sizeof(*rowarr));
  

   // changing random values
  rowarr[3][1] = 255;
  
  for (int i = 0; i < row; i++) {
    for (int k = 0; k < pxl; k++) {
      printf("%d ", rowarr[i][k]);
    }
    printf("\n");
  }
  
      
  return EXIT_SUCCESS;
}
  
  
  
