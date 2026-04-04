#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> arr(5);
    int sum = 0;
	for (int i=0;i<5;i++){
        cin >> arr[i];
        sum += arr[i];
    }
    sort(arr.begin(), arr.end());
    cout << sum / arr.size() << endl << arr[arr.size()/2] << endl;
	return 0;
}