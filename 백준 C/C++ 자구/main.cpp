#include <iostream>
#include "Rectangle.h"

int main()
{
	while (1)
	{
		Rectangle r1(0, 0, 0, 0);
		std::cin >> r1;
		//std::cout << r1;

		Rectangle r2(0, 0, 0, 0);
		std::cin >> r2;
		//std::cout << r2;

		Rectangle r3 = r1 and r2;
		std::cout << r3;
	}
}