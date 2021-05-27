// define a struct that holds information about a certain image
// e.g. format, size, color etc.x
// use a header file for that

size_t traverseData(unsigned char * arr, size_t arr_size) {
  // store temporary string in temp and the final string in str
  // using malloc so that we can free the memory later
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
        
    /* printf("the resulting string is: %s \n", str); */
    /* printf("str length is: %I64d \n", strlen(str)); */
    /* printf("temp length is: %I64d \n", strlen(temp)); */

    long int size = strtol(str, NULL, 0);

    // printf("the resulting string is: %ld \n", size);
    free(arr); // free allocated memory
    free(temp);
    free(str);
    return size;
  }

void readFormat(char * buffer) {
  // need only read from 1 to 3 inclusive
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

size_t readHeight(char * buffer) {
 // width stored as a c string
  unsigned char * hght = NULL;
  // size of wdth depends on how many bytes we need to write
  size_t l = 0;
  unsigned ind = 0;
  // generalize code !!!
  for (size_t h = 20; h < 24; h++) {
    // printf("%d ", buffer[w]);
    if (buffer[h] == 0) {
      continue;
    }
    else {
      l++; // increment wdth size
      hght = realloc(hght, l * sizeof(*hght));
      hght[ind] = buffer[h];
      ind++;
    }
  }
  printf("l: %I64d \n", l);
  size_t height = traverseData(hght, l);
  return height;
}

size_t readWidth(char * buffer) {
  // width stored as a c string
  unsigned char * wdth = NULL;
  // size of wdth depends on how many bytes we need to write
  size_t l = 0;
  unsigned ind = 0;
  for (size_t w = 16; w < 20; w++) {
    // printf("%d ", buffer[w]);
    if (buffer[w] == 0) {
      continue;
    }
    else {
      l++; // increment wdth size
      wdth = realloc(wdth, l * sizeof(*wdth));
      wdth[ind] = buffer[w];
      ind++;
    }
  }
  printf("l: %I64d \n", l);
  // traverseData fucntion call here
  size_t width = traverseData(wdth, l);
  return width;
}


void readBuffer(char * buffer, size_t sz) {
  readFormat(buffer);
  readWidth(buffer); // reads onlt width as a test
  readHeight(buffer);
}
