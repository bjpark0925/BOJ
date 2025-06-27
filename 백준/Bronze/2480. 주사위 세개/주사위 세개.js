var fs = require('fs');
var numbers = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number);

var a = numbers[0];
var b = numbers[1];
var c = numbers[2];

if(a == b && b == c){
    console.log(10000+(a*1000));
}
else{
    if (a == b){
        console.log(1000+(a*100));
    }
    else if (b == c){
        console.log(1000+(b*100));
    }
    else if (a == c){
        console.log(1000+(c*100));
    }
    else if ((a != b) && (b != c)){
        console.log(Math.max(a,b,c)*100);
    }
}