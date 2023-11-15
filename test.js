const arr = [0,0,0,0,1,2,3,4];
let s = 0;
let e = 0;

while(e<arr.length)
{
    if(arr[e]!=0)
    {
        let temp = arr[s];
        arr[s] = arr[e];
        arr[e] = temp;
        s++;
    }
    e++;
}

console.log(arr);