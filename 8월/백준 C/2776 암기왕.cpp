#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

//
//int binary_searching(vector<int> arr,int x,int n)
//{
//	int left = 0;
//	int right = n - 1;
//	while (left <= right)
//	{
//		int mid = (left + right) / 2;
//		if (arr[mid] == x)
//		{
//			return 1;
//		}
//		else if (arr[mid] > x)
//		{
//			right = mid - 1;
//		}
//		else
//		{
//			left = mid + 1;
//		}
//	}
//	return 0;
//}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int t;
	cin >> t;
	for (int j = 0; j < t; j++)
	{
		vector <int> arr;

		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			int num;
			cin >> num;
			arr.push_back(num);
		}
		sort(arr.begin(), arr.end());
		int m;
		cin >> m;
		for (int i = 0; i < m; i++)
		{
			int num;
			cin >> num;
			cout << binary_search(arr.begin(),arr.end(),num) << '\n';
		}
	}
	return 0;
}