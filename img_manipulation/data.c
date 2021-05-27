#define IDATBEG 37
#define IDATEND 41
#define IENDBEG 9

char * getData(char * buffer, size_t *result) {
  // check where IDAT begins
  if (buffer[IDATBEG] != 'I'){
    printf("IDATBEG: %d\n", buffer[IDATEND]);
    exit(EXIT_FAILURE);
  }
  // copy the buffer and return it
  size_t end = *result - IENDBEG +1;

  if (buffer[end] != 'I'){
    printf("IDATEND: %d\n", buffer[end+1]);
    exit(EXIT_FAILURE);
  }

  printf("result = %I64d\n", *result);
  size_t sz = *result - IDATEND - IENDBEG +1;
  char * data = malloc(sz * sizeof(*data));
  printf("IDATBEG: %d\n", buffer[IDATEND]);
  printf("IDATEND: %d\n", buffer[end]);
  
  size_t beg = IDATEND;
  size_t ind = 0;
  while (beg < end) {
    data[ind] = buffer[beg];
    ind++;
    beg++;
  }

  *result = sz;
  
  return data;
}
