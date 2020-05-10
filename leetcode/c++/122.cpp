// Say you have an array for which the ith element is the price of a given stock on day i.
//
// Design an algorithm to find the maximum profit. You may complete as many transactions as 
// you like (ie, buy one and sell one share of the stock multiple times). However, you may
// not engage in //multiple transactions at the same time (ie, you must sell the stock 
// before you buy again).
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        int maxProfit(vector<int> &prices);
    private:
        int sumIntVector(vector<int> &ints);
};

int sumIntVector(vector<int> &ints) {
    int sum = 0;
    for (vector<int>::iterator it = ints.begin(); it != ints.end(); it++) {
        sum += *it;
    }
    return sum;
}

int maxProfit(vector<int> &prices) {

    if (prices.size() == 0) {
        return 0;
    }

    bool upturn(false);
    bool prevUpturn(false);
    int prevPrice = prices.front();
    int lastValley = 0;
    vector<int> profits;

    for (vector<int>::iterator it = prices.begin(); it != prices.end(); it++)
    {
        int price = *it;
        prevUpturn = upturn;

        // If price is less than previous price, then we've found a peek and the trend
        // has reversed.
        if (price < prevPrice)
        {
            upturn = false;
        }

        // Price is more than previous price, then we've found a valley and the trend
        // has reversed.
        if (price > prevPrice)
        {
            upturn = true;
        }

        if (!upturn and prevUpturn == true)
        {
            profits.push_back(prevPrice - lastValley);
        }
        else if (upturn and prevUpturn == false)
        {
            lastValley = prevPrice;
        }

        prevPrice = price;
    }

    if (upturn) {
        profits.push_back(prevPrice - lastValley);
    }

    return sumIntVector(profits);
}

int main() {

    const int pricesList[] = {};
    vector<int> vprices(pricesList, pricesList+sizeof(pricesList)/sizeof(int));

    cout << "Max profit: " << maxProfit(vprices) << endl;
}