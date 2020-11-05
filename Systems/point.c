#include <stdio.h>

int val = 17;
char str[12]="Hello World\n";

void main(void){
  int newval = 2;
  char newstr[12] = "Goodbye";

  printf("%d is at %p\n",val,&val);
  printf("%s is at %p\n",str,str);
  printf("%d is at %p\n",newval,&newval);
  printf("%s is at %p\n",newstr,newstr);
}
