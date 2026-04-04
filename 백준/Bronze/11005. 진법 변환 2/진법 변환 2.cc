#include <iostream>
#include <string>

using namespace std;

int main() {
	int n, b;
    cin >> n >> b;
    
    string result;
    
    while (n > 0){
        int remain = n % b;
        if (remain < 10){
            result = (char)('0'+remain) + result;
        }
        else{
            result = (char)('A' + remain - 10) + result;
        }
        n /= b;
    }
    
    cout << result << endl;
	return 0;
}