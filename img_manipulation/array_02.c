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

int main() {
  int col = 5;
  int row = 5;

  unsigned *** colarr = malloc(col * sizeof(*colarr));
  
  fillCol(colarr, col, row);

  for (int i = 0; i < col; i++) {
    //      for (int j = 0; j < col; j++) {
    free(colarr[i]);
  }
  free(colarr);

  return 0;
}
