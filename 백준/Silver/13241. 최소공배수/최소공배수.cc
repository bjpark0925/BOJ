#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    long long a, b;
    cin >> a >> b;
    
    long long g = gcd(a, b);
    cout << a/g*b;
    
    return 0;
}