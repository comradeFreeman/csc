#include <stdio.h>
#include <math.h>


#define N 500000000

double F (double x)
{
    double f;
    f = (4.035446554*(sin(x/0.553645) + 55.456533) + 43.65 * cos((x + 54.222)/3.1428)) / 467.334454 + 2.003363333*x;
    return f;
}

int main ()
{
    double S = 0, x, a, b, h;
    const double Pi = 3.14159;
    a = 0;
    b = 100*Pi;
    //îòðåçîê [a, b] ðàçîáüåì íà N ÷àñòåé
    h = (b - a)/N;
    x = a + h;
    while (x < b)
    {
        S = S + 4*F(x);
        x = x + h;
        //ïðîâåðÿåì íå âûøëî ëè çíà÷åíèå x çà ïðåäåëû ïîëóèíòåðâàëà [a, b)
        if (x >= b) break;
        S = S + 2*F(x);
        x = x + h;
    }
    S = (h/3)*(S + F(a) + F(b));
    printf ("%f", S);
    return 0;
}
