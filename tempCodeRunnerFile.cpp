#include<iostream>
using namespace std;

int main(){
    
    int choice;
    do{
        cout << "1-add 2 nums\n2-subtract 2 nums\n3-divide 2 nums\n4-exit";
        cout << "enter your choice : ";
        cin >> choice;
        if(choice == 1){
            cout << "enter two nums ";
            int a,b; cin >> a >> b;
            cout << a+b << endl;
        }else if(choice == 2){
            cout << "enter two nums ";
            int a,b; cin >> a >> b;
            cout << a-b << endl;
        }
    }while(choice != 4);

    return 0;
}
