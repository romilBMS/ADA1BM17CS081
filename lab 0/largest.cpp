#include<iostream>
#include<vector>
using namespace std;

int main(){
    int n,mx=INT32_MIN,x;
    vector<int> a;
    cout<<"Enter size: ";
    cin>>n;
    cout<<"Enter elements: ";
    for(int i=0;i<n;i++){
        cin>>x;
        a.push_back(x);
        mx=max(a[i],mx);
    }
    cout<<"Largest number is: ";
    cout<<mx<<"\n";
}