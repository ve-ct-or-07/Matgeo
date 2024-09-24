#include <stdio.h>

float div(float);
float mod(float, float);
float sub(float, float);

int main()
{
    char *filename = "dat.txt";
    float x[3], y[3];
    x[0] = 3; x[1] = 0; y[1] = 2;
    y[2] = 5; y[0] = 0; x[2] = 0;

    float q, r, d, k;
    q = mod(x[0], y[0]);
    r = mod(x[2], y[2]);
    d = sub(q,r);
    k = div(d);
    y[0] = k; x[2] = k;
    printf("k=%.0f\nQ=(%.0f,%.0f)\nR=(%.0f,%.0f)\n",k,x[0],y[0],x[2],y[2]);

    FILE *fp = fopen(filename, "w");
    if (fp == NULL)
    {
        printf("Error opening the file %s", filename);
        return -1;
    }
    fprintf(fp, "%.0f;%.0f;Q[%.0f,%.0f]\n", x[0], y[0], x[0], y[0]);
    fprintf(fp, "%.0f;%.0f;P[%.0f,%.0f]\n", x[1], y[1], x[1], y[1]);
    fprintf(fp, "%.0f;%.0f;R[%.0f,%.0f]\n", x[2], y[2], x[2], y[2]);
    fclose(fp);
    return 0;
}

