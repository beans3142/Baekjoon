#include <stdio.h>

double mysqrt(unsigned int number) // float 
{
    unsigned int NUM_REPEAT = 16;
    unsigned int k;
    double res;
    double tmp = (double)number;
    for (k = 0, res = tmp; k < NUM_REPEAT; k++)
    {
        if (res < 1.0)
            break;
        res = (res * res + tmp) / (2.0 * res);
    }
    return res;
}

int main()
{
    printf("%lf", mysqrt(2));
}