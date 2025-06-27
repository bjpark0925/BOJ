var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n,m] = input[0].split(' ').map(Number);

let arr = new Array(n).fill(0);

for (let i = 1; i <= m; i++){
    const [start, end, num] = input[i].split(' ').map(Number);
    for (j = start; j <= end; j++){
        arr[j-1] = num;
    }
}

console.log(arr.join(' '));