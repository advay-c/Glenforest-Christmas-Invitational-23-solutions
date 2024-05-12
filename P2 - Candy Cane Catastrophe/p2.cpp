#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector <int> canes;
	for (int i = 0; i < n; i++)
	{
		int temp_cane; cin >> temp_cane;
		canes.push_back(temp_cane);
	}
	sort (canes.begin(), canes.end());
	reverse (canes.begin(), canes.end());
	int total = 0;
	for (int i = 0; i < canes.size()-1; i++)
	{
		total += canes[i];
	}
	cout << total +1 << endl;
}
