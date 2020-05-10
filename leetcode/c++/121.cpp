// Problem 121:
// ------------
// Say you have an array for which the ith element is the price of a given stock on day i.
//
// If you were only permitted to complete at most one transaction (ie, buy one and sell one share // of the stock), design an algorithm to find the maximum profit.
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        int maxProfit(vector<int> &prices);
};

int maxProfit(vector<int> &prices) {
    int diff = 0;
    int new_diff = 0;
    int max_price = 0;

    for (vector<int>::reverse_iterator rit = prices.rbegin(); rit != prices.rend(); ++rit)
    {
        max_price = max(*rit, max_price);
        new_diff = max_price - *rit;

        if (diff < new_diff)
        {
            diff = new_diff;
        }
    }

    return diff;  
}

int main() {

    const int list[] = {7, 1, 5, 3, 6, 4};
    vector<int> input(list, list+sizeof(list)/sizeof(int));

    cout << "Max profit is: " << maxProfit(input) << endl;
} 