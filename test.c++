#include<bits/stdc++.h>
using namespace std;
int power(int a,int b)
{
    if(b==0)return 1;
    if(b&1)
    {
        int val = power(a,b/2);
        return a * val*val;
    }
    int val = power(a,b/2);
    return val * val;
}
int power2(int a,int b)
{
    int ans = 1;
    int val = a;
    while(b)
    {
        if(b&1)
        {
            ans*=val;
        }
        val*=val;
        b>>=1;
    }
    return ans;
}
int main()
{
    cout<<power2();



    return 0;
}