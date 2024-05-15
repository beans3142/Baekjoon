#include <stdio.h>
#include "BST.h"

int main()
{
	BST tree;
	while (1)
	{
		int input;
		printf("안녕\n");
		printf("사용 가능 명령어\n1 X : 트리에 X값을 갖는 노드 삽입 2 X : 트리에 X 값을 갖는 노드 제거 3 : 트리 모양 보이기 4 : 종료\n 입력 : ");
		scanf("%d", &input);
		if (input == 1)
		{
			scanf_s("%d", &input);
			if (tree.Index(input)!=-1)
			{
				tree.Append(input);
			}
		}
		else if (input == 2)
		{
			scanf_s("%d", &input);
			if (tree.Index(input))
			{
				int idx = tree.Index(input);
				tree.Delete(idx);
			}
		}
		else if (input==3)
		{
			tree.Show();
		}
		else
		{
			break;
		}
	}
}