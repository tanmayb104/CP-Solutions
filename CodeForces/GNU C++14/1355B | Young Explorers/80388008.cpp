#include <bits/stdc++.h> 
using namespace std; 
 
int main() 
{ 
    int t;
    cin>>t;
    while(t--){
        int n;
         cin>>n;
        int arr[n];
        for(int i=0;i<n;i++){
             cin>>arr[i];
        }
        sort(arr, arr+n); 
        int c=0;
        int s=0;
        for(int j=0;j<n;j++){
            if(arr[j]<=(j+1-s)){
                c++;
                s=j+1;
            }
        }
        cout<<c<<"\n";
    }
    return 0; 
} 