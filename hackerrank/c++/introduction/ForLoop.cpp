#include <iostream>
#include <string>

using namespace std;

string numberToEnglish(int number)
{
    string english;
    switch (number)
    {
        case 1:
            english = "one";
            break;
        case 2:
            english ="two";
            break;
        case 3:
            english ="three";
            break;
        case 4:
            english ="four";
            break;
        case 5:
            english ="five";
            break;
        case 6:
            english ="six";
            break;
        case 7:
            english ="seven";
            break;
        case 8:
            english ="eight";
            break;
        case 9:
            english ="nine";
            break;
        default:
            (number % 2 == 0) ? english = "even" : english = "odd";
    }
    return english;
}

int main()
{
    int a;
    int b;
    cin >> a;
    cin >> b;

    for (int i = a; i < (b+1); i++)
    {
        cout << numberToEnglish(i) << endl;
    }
    return 0;
}
