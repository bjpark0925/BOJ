#include <iostream>
using namespace std;
int main(){
    int types = 6;
    int arr[types];
    
    for (int i=0;i<types;i++){
        cin >> arr[i];
    }
    
    int chess[types] = {1,1,2,2,2,8};
    int result[types];
    for (int i=0;i<types;i++){
        result[i] = chess[i] - arr[i];
    }
    
    for (int i=0;i<types;i++){
        cout << result[i];
        if (i<types-1)
            cout << " ";
    }
    cout << endl;
    
    return 0;
}