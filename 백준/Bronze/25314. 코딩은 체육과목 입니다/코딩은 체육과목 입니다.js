var fs = require('fs');
var n = fs.readFileSync('/dev/stdin').toString();

let end = parseInt(n)/4;
let str = '';
for(let i=0;i<end;i++){
    str+='long ';
}
console.log(str+'int');
