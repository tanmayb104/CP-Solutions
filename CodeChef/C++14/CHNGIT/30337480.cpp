#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int i,n,j,k,l,p;
	cin>>i;
	for(j=0;j<i;j++)
	{
	    cin>>n;
	    int a[n],b[n];
	    for(k=0;k<n;k++)
	    {
	        cin>>a[k];
	        b[k]=0;
	    }
	    for(k=0;k<n;k++)
	    {
	        for(l=(k+1);l<n;l++)
	        {
	            if(a[k]==a[l])
	            {
	                b[k]++;
	            }
	        }
	    }
	    p=0;
	    for(k=0;k<n;k++)
	    {
	        if(b[k]>p)
	        {
	            p=b[k];
	        }
	    }
	    cout<<(n-p-1)<<endl;
	}
	return 0;
}
