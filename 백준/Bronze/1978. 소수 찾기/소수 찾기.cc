#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
    cin >> n;
    
    vector<bool> isPrime(1001, true);
    isPrime[0] = isPrime[1] = false;
    
    for (int i=2;i*i<=1000;i++){
        for (int j=i*i;j<=1000;j+=i){
            isPrime[j] = false;
        }
    }
    
    int answer = 0;
    for (int i=0;i<n;i++){
        int num;
        cin >> num;
        if (isPrime[num]){
            answer++;
        }
    }
    
    cout << answer << endl;
    
	return 0;
}