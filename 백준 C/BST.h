#include "node.h"

class BST
{
public:
	Node Tree[1000];

	int Append(int value);
	int Delete(int value);
	int Index(int value);
	void Show();
};