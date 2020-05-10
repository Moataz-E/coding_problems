#include <cmath>
#include<iostream>
using namespace std;

int main()
{
    int sum = 0;
    int number;
    for (int i = 0; i < 3; i++)
    {
        cin>> number;
        sum += number;
    }
    cout<< sum << endl;
    return 0;
}
