#include <iostream>
#include <cmath>

using namespace std;

void update(int *a, int *b)
{
    int oldA = *a;
    *a = (*a) + (*b);
    *b = abs(oldA - *b);
}

int main()
{
    int a;
    int b;
    int *pa = &a;
    int *pb = &b;

    cin >> a;
    cin >> b;

    update(pa, pb);

    cout << a << endl;
    cout << b << endl;

    return 0;
}
