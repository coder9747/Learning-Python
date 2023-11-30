// #include<bits/stdc++.h>
// using namespace std;
// bool check(int number)
// {
//     for(int i=2;i*i<=number;++i)
//     {
//         if(number%i==0)return false;
//     }
//     return true;
// }
// pair<bool,int> isP(int number)
// {
//     vector<int> arr;
//     int digitCount = 0;
//     while(number)
//     {
//         int r = number % 10;
//         arr.emplace_back(r);
//         number = number / 10;
//         digitCount++;
//     }
//     int s = 0;
//     int e = arr.size()-1;
//     pair<bool,int> pq;
//     while(s<=e)
//     {
//         if(arr[s]!=arr[e])
//         {
//             pq.first = false;
//             pq.second = -1;
//             return pq;
//         }
//         s++;
//         e--;
     
//     }
//     pq.first = true;
//     if(digitCount&1)
//     {
//         pq.second = 2;
//     }
//     else
//     {
//         pq.second = 1;
//     }
//     return pq;
    
// }

// int main() {
// 	// your code goes here
	
// 	    int n = 1e5;
// 	    // int even = 0;
// 	    // int odd = 0;
// 	    int number = 2;
// 	    while(n && number<=1e6)
// 	    {
// 	        if(check(number))
// 	        {
// 	            pair<bool,int> p = isP(number);
// 	            if(p.first)
//                 {
//                     cout<<number<<" ";
//                 }
// 	        }
// 	        number++;
// 	    }
// 	    // cout<<even<<" "<<odd<<endl;

// 	return 0;
// }
