#include "BST.h"
#include "node.h"
#include <math.h>
#include <stdio.h>

int BST::Index(int value)
{
	int idx = 1;
	while (idx<1000 && Tree[idx].fill)
	{
		if (Tree[idx].Value == value) return idx;
		
		if (Tree[idx].Value > value) idx=idx*2;
		else idx=idx*2+1;
	}
	return -1;
}


int BST::Append(int value)
{
	printf("1321381278981274897129847\n");
	Node Newnode;
	Newnode.Value = value;
	Newnode.fill = true;
	int idx = 1;
	while (idx < 1000)
	{
		if (Tree[idx].fill == false)
		{
			Tree[idx] = Newnode;
			break;
		}
		if (Tree[idx].Value < Newnode.Value) idx = idx * 2 + 1;
		else idx = idx * 2;
	}
	if (idx > 1000)
	{
		return -2;
	}
	return 0;
}

int BST::Delete(int idx)
{
	// 자식 노드가 없는 경우
	if (idx * 2 > 1000 ||( (Tree[idx * 2].fill == false) && (Tree[idx * 2 + 1].fill == false)))
	{
		Node clear;
		Tree[idx] = clear;
	}
	// 왼쪽이 있는 경우
	else if (Tree[idx * 2].fill)
	{
		Tree[idx] = Tree[idx * 2];
		Delete(idx * 2);
	}
	// 오른쪽이 있는 경우
	else if (Tree[idx * 2 + 1].fill)
	{
		Tree[idx] = Tree[idx * 2 + 1];
		Delete(idx * 2 + 1);
	}
	return 0;
}

void BST::Show()
{
	int idx = 1;

	for (int i = 0; i < 20; i++)
	{
		bool treeEnd=true;

		for (int j = pow(2, i); j < pow(2, i + 1); j++)
		{
			if (Tree[j].fill==true)
			{
				treeEnd = false;
				printf("%d\t", Tree[j].Value);
			}
			else
			{
				printf("\t");
			}
		}
		if (treeEnd) break;

		printf("\n");

		for (int j = pow(2, i); j < pow(2, i + 1); j++)
		{
			printf("├────┐");
		}
		printf("\n");
	}
}