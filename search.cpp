#include<iostream>
#include<vector>
#include<chrono>
using namespace std;
using namespace std::chrono;

int binarySearch(vector<int> a, int l, int h, int k){
    int mid;
    while(l<=h){
        mid=(l+h)/2;
        if(a[mid]==k){
            return mid+1;
        }else if(a[mid]<k){
            l=mid+1;
        }else{
            h

            =mid-1;
        }
    }
    return -1;
}

int main(){
    int n,t,x,pos,ele;
    vector<int> a;
    cin>>t;
    while(t--){
        pos=-1;
        cin>>n>>ele;
        for(int i=0;i<n;i++){
            cin>>x;
            a.push_back(x);
        }
        auto beginTime=high_resolution_clock::now();
        pos=binarySearch(a,0,n-1,ele);
        auto endTime=high_resolution_clock::now();
        auto duration=duration_cast<nanoseconds>(endTime-beginTime);
        if(pos>-1){
            cout<<1<<"\n";
        }else{
            cout<<-1<<"\n";
        }
        cout<<"Time taken is: ";
        cout<<duration.count()<<" nanoseconds\n";
        for(int i=0;i<a.size();i++){
            a.pop_back();
        }
    }
}
