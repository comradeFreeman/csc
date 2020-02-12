#include <iostream>
#include <cstdlib>
using namespace std;
 
int main() {
    int n = 300; //100 + rand() % 1000;
    //cin >> n;                                             //ââîä èç ñòàíäàðòíîãî ïîòîêà
    double A[n][n];                                        
    double B[n][n];
    double Z[n][n];
    double H[n][n];
    double E[n][n];
    double C[n][n];
    double Ans[n][n];
    
    for (int i = 0; i < n; i++){             //ìàòðèöà À
        for (int j = 0 ; j < n ; j++){
            //cin >> A[i][j];
            A[i][j] = 3 + rand() % 50;
        }
    }
    
    for (int i = 0; i < n; i++){                            //ìàòðèöà Â
        for (int j = 0 ; j < n ; j++){
            //cin >> B[i][j];
            B[i][j] = 3 + rand() % 50;
        }
    }
    
    for (int i = 0; i < n; i++){                            //åäèíè÷íàÿ ìàòðèöà Å
        for (int j = 0 ; j < n ; j++){
            if (i == j) E[i][j] = 1;
            else E[i][j] = 0;
        }
    }
 
    for (int i = 0; i < n; i++){                 //ðàçíîñòü ìàòðèö Â è Å
        for (int j = 0; j < n; j++){
            Z[i][j] = 0;
            Z[i][j] = B[i][j] - E[i][j];
        }
    }
    
    for (int i = 0; i < n; i++){             //óìíîæåíèå ìàòðèö À è (Â - Å)
        for (int j = 0; j < n; j++){
            H[i][j] = 0;
            for (int t = 0; t < n; t++){
                H[i][j] += A[i][t] * Z[t][j];
            }
        }
    }
    
    for (int i = 0; i < n; i++){             //ìàòðèöà Ñ
        for (int j = 0; j < n; j++){
            C[i][j] = 0;
            C[i][j] = 1.0/(i+1 + j+1);
        }
    }
    
    for (int i = 0; i < n; i++){                 //ìàòðèöà A(B–E)+C
        for(int j = 0; j < n; j++){
            Ans[i][j] = H[i][j] + C[i][j];
            //printf("%1.2f", Ans[i][j]); 
            // cout << " " ;
        }
        //cout << endl;
    }
    //cout << "Dimensions: " << n << "x" << n << endl;
    return 0;
}
