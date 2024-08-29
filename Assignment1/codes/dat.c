#include <stdio.h>

int main()
{
	int i;
    char *filename = "dat.txt";
    float x[3],y[3];
    FILE *fp = fopen(filename, "w");
    if (fp == NULL)
    {
        printf("Error opening the file %s", filename);
        return -1;
    }
    for (i = 0; i < 3; i++)
    {
	    printf("Enter x-coord of %d point\n",i+1);
	    scanf("%f",&x[i]);
	    printf("Enter y-coord of %d point\n",i+1);
	    scanf("%f",&y[i]);
    }
	    fprintf(fp, "%.2f;%.2f;A[%.2f,%.2f]\n",x[0],y[0],x[0],y[0]);
	    fprintf(fp, "%.2f;%.2f;B[%.2f,%.2f]\n",x[1],y[1],x[1],y[1]);
	    fprintf(fp, "%.2f;%.2f;C[%.2f,%.2f]\n",x[2],y[2],x[2],y[2]);
    fclose(fp);

    return 0;
}
