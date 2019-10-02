#include <iostream>

using namespace std;

int main()
{
    int n,k,u;
    int a[1000],b[1000],max=0;
    cin>>n>>k>>u;
    int c[1000000],d[1000000];
    for(int i=0;i<k;i++)
    {
        cin>>a[i];
    }
    for(int i=0;i<u;i++)
    {
        cin>>b[i];
    }
    for(int i=0;i<k;i++)
    {
        for(int j=0;j<u;j++)
        {
            for(int l=0;l<(u+k);l++)
            {
                c[l]=n-(a[i]+b[j]);
                d[l]=a[i]+b[j];
            }
        }
    }
    for(int i=0;i<(u+k);i++)
    {
        if(c[i]>0)
        {
           if(d[i]>max)
            max=d[i];
        }
    }
    if(max>0)
        cout<<max;
    else
        cout<<-1;
}
