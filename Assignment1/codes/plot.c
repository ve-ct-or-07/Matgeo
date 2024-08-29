#include<stdio.h>
float div(float,float);
float coord(float,float,float);
int main()
{
  float a1=1,a2=-4,b1=-5,b2=5,x,y,k;
  k=-div(b1,b2);
  x=coord(a1,a2,k);
  y=coord(b1,b2,k);
   printf("Ratio=%lf:1\n",k);
  printf("Point of division=(%lf,%lf)\n",x,y);
 }

