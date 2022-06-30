#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

const char alphanumeric[] = "1234567890!@#$%^&*?ABCDEFGHIJKLMNOPQRSTUVWXYZ";
int str_len = sizeof(alphanumeric) -1;

int main()
{
    int n;
    cout<< "Length of Password: ";
    cin >> n;
    srand (time(0));
    cout << "Password Generated: ";
    for(int i = 0; i < n; i++)
    cout << alphanumeric[rand() % str_len];
    return 0;
}