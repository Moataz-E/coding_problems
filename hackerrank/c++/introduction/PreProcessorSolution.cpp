#include <iostream>
#include <vector>
using namespace std;

#define INF 100000000
#define toStr(str) #str
#define io(v) cin >> v
#define FUNCTION(name, op) inline void name(int &num1, int num2) {(num2 op num1) ? num1 = num2 : false;}
#define foreach(v, i) for (int i = 0; i < v.size(); ++i)

#if !defined toStr || !defined io || !defined FUNCTION || !defined INF
#error Missing preprocessor definitions
#endif 


FUNCTION(minimum, <)
FUNCTION(maximum, >)

int main(){
	int n; cin >> n;
	vector<int> v(n);
	foreach(v, i) {
		io(v)[i];
	}
	int mn = INF;
	int mx = -INF;
	foreach(v, i) {
		minimum(mn, v[i]);
		maximum(mx, v[i]);
	}
	int ans = mx - mn;
	cout << toStr(Result =) <<' '<< ans;
	return 0;

}