#include <iostream>
#include <algorithm>
#include <math.h>

int mxdp[100001] = { 0, };
int mndp[100001] = { 0, };
int arr[100001];
int n;

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	for (int i = 1; i < n; i++)
	{
		if (arr[i] >= arr[i - 1])
		{
			mxdp[i] = mxdp[i - 1] + 1;
		}
		if (arr[i] <= arr[i - 1])
		{
			mndp[i] = mndp[i - 1] + 1;
		}
	}
	
	/*for (int i = 0; i < n; i++)
	{
		cout << mxdp[i] << " ";
	}
	cout << endl;
	for (int i = 0; i < n; i++)
	{
		cout << mndp[i] << " ";
	}
	cout << endl;*/
	if (n == 1)
	{
		cout << 1;
		return 0;
	}
	cout<<max(2,max(*max_element(mndp,mndp+n),(*max_element(mxdp,mxdp+n)))+1);
}