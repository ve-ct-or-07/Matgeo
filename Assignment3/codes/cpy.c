#include <stdio.h>
#include <math.h>

double f1(double x) {
    return x * x;
}

double f2(double x) {
    return x + 6;
}

double diff_func(double x) {
    return f2(x) - f1(x);
}

double integrate(double (*func)(double), double a, double b, int n) {
    double h = (b - a) / n;
    double sum = (func(a) + func(b)) / 2.0;
    for (int i = 1; i < n; i++) {
        sum += func(a + i * h);
    }
    return h * sum;
}

double discriminant(double a, double b, double c) {
    return b*b - 4*a*c;
}

double rootp(double a, double b, double c) {
    return (-b+sqrt(c))/(2*a);
}

double rootn(double a,double b,double c){
	return (-b-sqrt(c))/(2*a);
}

