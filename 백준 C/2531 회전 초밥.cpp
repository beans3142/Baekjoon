#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	vector<int> sushi;
	unordered_map<int, int> kind;

	int n, d, k, c;
	cin >> n >> d >> k >> c;
	for (int i = 0; i < n; i++)
	{
		int num;
		cin >> num;
		sushi.push_back(num);
	}
	for (int i = 0; i < k; i++)
	{
		kind[sushi[i]] += 1;
	}

	int mx_kind = kind.size();

	for (int i = 0; i < n; i++)
	{
		kind[sushi[i]] -= 1;
		if (kind[sushi[i]] == 0)
		{
			kind.erase(sushi[i]);
		}
		kind[sushi[(i + k) % (n)]]+=1;

		int nowsize=kind.size()+(1-kind.count(c));

		//cout << "map -> ";
		//for (int j = 0; j < k; j++)
		//{
		//	cout << sushi[(i + 1 + j)%n] << ' ';
		//}
		//cout << '\n';

		//for (auto iter = kind.begin(); iter != kind.end(); iter++) 
		//{ 
		//	cout << iter->first << " " << iter->second << endl; 
		//} 
		//cout << endl;

		//printf("%d %d %d\n",nowsize,kind.size(),kind.count(c));
		mx_kind = nowsize > mx_kind ? nowsize : mx_kind;
	}
	cout << mx_kind;
}
// 1 2 2 3 2 4 => [] -> [2:2,3:1]