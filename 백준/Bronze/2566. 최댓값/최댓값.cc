#include <iostream>

using namespace std;

int main() {
	int arr[9][9];
    int maxValue = -1;
    for (int i=0;i<9;i++){
        for (int j=0;j<9;j++){
            cin >> arr[i][j];
        }
    }
    
    int x, y;
    for (int i=0;i<9;i++){
        for (int j=0;j<9;j++){
            if (arr[i][j] > maxValue){
                maxValue = arr[i][j];
                x = i+1;
                y = j+1;
            }
        }
    }
    
    cout << maxValue << endl << x << " " << y << endl;
	return 0;
}