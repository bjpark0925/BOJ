#include <iostream>

using namespace std;

int main() {
	int a, b;
    while ((cin >> a >> b) && (a !=0 && b != 0)){
        if (b % a == 0){
            cout << "factor" << endl;
        }
        else if (a % b == 0){
            cout << "multiple" << endl;
        }
        else{
            cout << "neither" << endl;
        }
    }
	return 0;
}