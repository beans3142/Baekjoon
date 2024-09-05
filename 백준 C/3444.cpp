#include <iostream>
#include <vector>
#include <algorithm>

struct node
{
	node* left, * right, * par;
	int key;
	int cnt;
	int sum, value, lazy;
	int inv;
} *tree,*pos[100001];

void rotate(node* x)
{
	node* parnode = x->par;
	node* xchild;
	if (x == parnode->left)
	{
		xchild = x->right;
		parnode->left = xchild;
		x->right = parnode;
	}
	else
	{
		xchild = x->left;
		parnode->right = xchild;
		x->left = parnode;
	}
	x->par = parnode->par;
	parnode->par = x;
	if (xchild) xchild->par = parnode;

	node* parparnode = x->par;
	if (parparnode != nullptr) {
		if (x == parparnode->left) {
			parparnode->left = x;
		}
		else {
			parparnode->right = x;
		}
	}
	else {
		tree = x;
	}
	update(parnode);
	update(x);
}

void splay(node* x)
{
	while (x->par != nullptr)
	{
		node* par = x->par;
		node* parpar = par->par;
		if (parpar)
		{
			if ((x == par->left) == (par == parpar->left))
			{
				rotate(par);
			}
			else
			{
				rotate(x);
			}
		}
	}
}

void insert(int key)
{
	node* par = tree;
	node** parpar;
	if (par == nullptr)
	{
		node* x = new node;
		tree = x;
		x->left = x->right = x->par = nullptr;
		x->key = key;
		return;
	}
	while (1)
	{
		if (key == par->key) return;
		if (key < par->key)
		{
			if (par->left == nullptr)
			{
				parpar = &(par->left);
				break;
			}
			par = par->left;
		}
		else
		{
			if (par->right == nullptr)
			{
				parpar = &par->right;
				break;
			}
			par = par->right;
		}
	}
	node* x = new node;
	*parpar = x;
	x->left = x->right = nullptr;
	x->par = par;
	x->key = key;
	splay(x);
}

bool find(int key)
{
	node* par = tree;
	if (!par) return false;
	while (par)
	{
		if (key == par->key) break;
		if (key < par->key)
		{
			if (par->left == nullptr) break;
			par = par->left;
		}
		else
		{
			if (par->right == nullptr) break;
			par = par->right;
		}
	}
	splay(par);
	return key == par->key;
}

void del(int key)
{
	if (find(key) == false) return;
	node* cur = tree;
	if (cur->left)
	{
		if (cur->right)
		{
			tree = cur->left;
			tree->par = nullptr;
			node* x = tree;
			while (x->right) x = x->right;
			x->right = cur->right;
			cur->right->par = x;
			splay(x);
			delete cur;
			return;
		}
		else
		{
			tree = cur->left;
			tree->par = nullptr;
			delete cur;
			return;
		}
	}
	else if (cur->right)
	{
		tree = cur->right;
		tree->par = nullptr;
		delete cur;
		return;
	}
	delete cur;
	tree = nullptr;
}

void update(node* x)
{
	x->cnt = 1;
	x->sum = x->value;
	if (x->left)
	{
		x->cnt += x->left->cnt;
		x->sum += x->left->sum;
	}
	if (x->right)
	{
		x->cnt += x->right->cnt;
		x->sum += x->right->sum;
	}
}

void find_k(int k)
{
	node* x = tree;
	lazy(x);
	while (1)
	{
		while (x->left && x->left->cnt > k)
		{
			x = x->left;
			lazy(x);
		}
		if (x->left) k -= x->left->cnt;
		if (!k--) break;
		x = x->right;
		lazy(x);
	}
	splay(x);
}

void init(int n)
{
	node* x;
	tree = x = new node;
	x->left = x->right = x->par = nullptr;
	x->cnt = n;
	x->sum = x->value = 0;
	for (int i = 1; i < n; i++)
	{
		x->right = new node;
		x->right->par = x;
		x = x->right;
		x->left = x->right = nullptr;
		x->cnt = n - i;
		x->sum = x->value = 0;
	}
}

void add(int idx, int value)
{
	find_k(idx);
	tree->sum += value;
	tree->value += value;
}

void add(int l, int r, int z)
{
	interval(l, r);
	node* x = tree->right->left;
	x->sum += x->cnt * z;
	x->lazy += z;
}

void interval(int l, int r)
{
	find_k(l - 1);
	node* x = tree;
	tree = x->right;
	tree->par = nullptr;
	find_k(r - l + 1);
	x->right = tree;
	tree->par = x;
	tree = x;
}

int sum(int l, int r)
{
	interval(l, r);
	return tree->right->left->sum;
}

/*
void lazy(node *x)
{
	x->value += x->lazy;
	if (x->left)
	{
		x->left->lazy += x->lazy;
		x->left->sum += x->left->cnt * x->lazy;
	}
	if (x->right)
	{
		x->right->lazy += x->lazy;
		x->right->sum += x->right->cnt*x->lazy;
	}
	x->lazy = 0;
}
*/

void lazy(node* x)
{
	if (x->inv == false) return;
	node* t = x->left;
	x->left = x->right;
	x->right = t;
	x->inv = false;
	if (x->left) x->left->inv = !x->left->inv;
	if (x->right) x->right->inv = !x->right->inv;
}

void reverse(int l, int r)
{
	interval(l, r);
	node* x = tree->right->left;
	x->inv = !x->inv;
}

using namespace std;
int n, arr[100001];

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);
	while (1)
	{
		cin >> n;
		if (!n) break;
		vector<int> vec;
		for (int i = 1; i <= n; i++)
		{
			cin >> arr[i];
			vec.push_back(arr[i]);
		}
		sort(vec.begin(), vec.end());
		vec.erase(unique(vec.begin(), vec.end()),vec.end());
		vector<vector<int>> tmp(vec.size());
		for(int i=1;i<=n;i++)
		{
			arr[i] = lower_bound(vec.begin(), vec.end(), arr[i]) - vec.begin();
			tmp[arr[i]].push_back(i);
		}
		int idx = 1;
		for (int i = 0; i < vec.size(); i++)
		{
			for (auto j : tmp[i + 1])
			{
				arr[j] == idx++;
			}
		}
		init(n);
		for (int i = 1; i <= n; i++)
		{
			splay(tree);
			cout << tree->left->cnt << " ";
			interval(tree->key, i);
		}
	}
}