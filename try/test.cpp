#include <iostream>
#include <cmath>
using namespace std;
double f(double x) { return pow(tan(x*sin(x))*x,8); } // 要微分的函數
int main(){
    double x,a,b;
    cin>>x>>a>>b;
    double h = 1e-37; // 微小量
    double derivative = (f(x + h) - f(x)) / h; // 導數定義
    double integral = 0;
    for(double i=a; i<b; i+=h) {
        integral += f(i) * h; // 矩形面積累加
    }

    cout<< derivative <<"\n"<< integral << endl;
}