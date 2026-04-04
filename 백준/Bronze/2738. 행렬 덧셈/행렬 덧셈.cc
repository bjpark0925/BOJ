#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    int matrix[2][n][m];
    int answer[100][100] = {0};
    for (int k=0;k<2;k++){
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                cin >> matrix[k][i][j];
            }
        }
    }
    
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            for (int k=0;k<2;k++){
                answer[i][j] += matrix[k][i][j];
            }
            cout << answer[i][j];
            if (j == m-1) cout << endl;
            else cout << " ";
        }
    }
    
	return 0;
}