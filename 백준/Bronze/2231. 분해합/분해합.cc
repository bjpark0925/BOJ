#include <iostream>

using namespace std;

int main() {
	int n, answer = 0;
    cin >> n;
    for (int i=0;i<n;i++){
        int sum = i, num = i;
        while (num){
            sum += num % 10;
            num /= 10;
        }
        if (sum == n){
            answer = i;
            break;
        }
    }
    cout << answer << endl;
	return 0;
}