#include "debug.h"

#include <iostream>
using namespace std;
int main(){
    //Counting Pegions again
    for (int i = 0; i < 10; i++)
    {
        dbgprint(i);
        cout<<"Pegion "<<i<<endl;
    }
    dbgmsg("Exited Loop");
    cout<<"Some Experimentation: "<<endl;
    cout<<"Exp1"<<endl;
    dbgprint(32);
    cout<<endl;
    cout<<"Exp2"<<endl;
    int x = 23;
    dbgprint(x);
    cout<<endl;
    char a[3]="me";
    cout<<"Exp3"<<endl;
    dbgprint(a);
    cout<<endl;
}