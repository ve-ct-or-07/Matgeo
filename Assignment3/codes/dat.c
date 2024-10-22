#include <stdio.h>
#include <math.h>

double f1(double x);
double f2(double x);
double diff_func(double x);
double discriminant(double a, double b, double c);
double rootp(double a, double b, double c);
double rootn(double a, double b, double c);
double integrate(double (*func)(double), double a, double b, int n);

int main() {
    char *filename = "dat.txt";
    double a = 1, b = -1, c = -6;
    
    double dlt = discriminant(a,b,c);

    double r1=rootp(a,b,dlt);
    double r2=rootn(a,b,dlt);

    double x1 = fmin(r1, r2);
    double x2 = fmax(r1, r2);

    int n = 1000;
    double area = integrate(diff_func, x1, x2, n);

    printf("%.2f\n", area);
    
    FILE *fp = fopen(filename, "w");
    if (fp == NULL)
    {
        printf("Error opening the file %s", filename);
        return -1;
    }
    fprintf(fp, "%lf;%lf;%lf\n",a,b,c);
    fclose(fp);

    return 0;
}
