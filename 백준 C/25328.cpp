#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <vector>

using namespace std;

int k;
string S;
vector<string> arr;
vector<string> ans;
unordered_map<string,int> dict;

void recur(int idx, string s)
{
	if (s.length() == k)
	{
		dict[s]+=1;
	}
	for (int i = idx; i < S.length(); i++)
	{
		recur(i+1,s+S[i]);
	}
}

int main()
{
	for(int i = 0;i<3;i++)
	{
		cin >> S;
		arr.push_back(S);
	}
	cin >> k;
	for (auto i : arr)
	{
		S = i;
		recur(0, "");
	}
	for (pair<string, int> i : dict) if (dict[i.first] >= 2) ans.push_back(i.first);
	if (ans.size() == 0)
	{
		cout << -1;
	}
	else
	{
		sort(ans.begin(), ans.end());
		for (auto i : ans) cout << i << "\n";
	}
}