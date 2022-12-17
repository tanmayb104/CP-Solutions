#include <iostream>
#include<cstdlib>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<unordered_set>
#include<map>
#include<unordered_map>
#include<forward_list>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<utility>
#include<cmath>
#include<iomanip>

#define nl              cout<<"\n"
#define sp   			cout<<" " 
#define ll              long long
#define ld              long double
#define rep(i,k,n)      for(int i = k ; i < n ; i++ )
#define Rep(i,k,n)      for(int i = k ; k<n ? i<n : i>n ; k<n ? i++ : i-- )
#define si(x)           scanf("%d",&x)
#define sll(x)          scanf("%lld",&x)
#define sf(x)           scanf("%f",&x)
#define slf(x)          scanf("%f",&x)
#define sc(c)           scanf("%c",&c)
#define ss(s)           scanf("%s",&s)
#define pi(x)           printf("%d",&x)
#define pll(x)          printf("%lld",&x)
#define pf(x)           printf("%f",&x)
#define plf(x)          printf("%f",&x)
#define pc(c)           printf("%c",&c)
#define ps(s)           printf("%s",&s)
#define vi              vector<int>          
#define vc              vector<char>
#define pii             pair<int,int>
#define vpii            vector<pair<int,int> >
#define pb(x)           push_back(x)
#define mp(x,y)         make_pair{x,y}
#define F               first
#define S               second
#define srt(a,n)        sort(a,a+n)
#define sortall(v)      sort(v.begin(),v.end())
#define fa(a,i)         fill(a,a+n,i)
#define mm(a,i)         memset(a,i,sizeof(a))
#define tr(it,a,beg)    for(auto it = a.begin() ; it != a.end() ; it++ )
#define etr(it,a,end)   for(auto it = a.rbegin() ; it != a.rend() ; it++ )
#define PI              3.141592653589793116
#define mod             
#define mod             
#define fs(i)           fixed<<setprecision(i)
#define s(i)            setprecision(i)
#define FastIO          ios_base :: sync_with_stdio (0) ; cin.tie(NULL) ;

using namespace std;

const long long INF = 1e18 ;
const int32_t M = 1e9+7 ;
const int32_t MM = 998244353 ;


int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        ll n, x;
        cin >> n >> x;

        ll a[1000000];

        for(ll i = 0; i < n; i++)
        {
            cin >> a[i];
        }

        ll i = 0;
        ll z = 0;
        for(ll k = x; k > 0 && i < n-1; k--)
        {
            bool flag = 0;
            ll p = log(a[i])/log(2);
            ll r = 1 << p;
            a[i] = a[i] ^ r;

            for(ll j = i + 1; j < n; j++)
            {
                if((a[j] ^ r) < a[j])
                {
                    a[j] = a[j] ^ r;
                    flag = 1;
                    break;
                }
            }

            if(flag == 0)
            {
                a[n - 1] = a[n - 1] ^ r;
            }

            while(a[i] <= 0)
            {
                i++;
            }
            z = k + 1;
        }
        

        if(z > 0)
        {
            if((n < 3) && z % 2 > 0) 
            {
                a[n - 1] = a[n - 1] ^ 1;
                a[n - 2] = a[n - 2] ^ 1;
            }
        }

        for(int i = 0; i < n; i++)
        {
            cout << a[i] << " ";
        }

        cout << endl;
    }
}