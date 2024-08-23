#include<stdio.h>
int main()
  {
  double x1=1,y1=-5,x2=-4,y2=5,x,y,k;
  k=-y1/y2;
  x=(k*x2+x1)/(k+1);
  y=(k*y2+y1)/(k+1);
   printf("Ratio=%lf:1\n",k);
  printf("Point of division=(%lf,%lf)\n",x,y);
 }

