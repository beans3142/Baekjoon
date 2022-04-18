#include "Rectangle.h"
#include <iostream>
//using namespace std;

int Rectangle::id = 0;

Rectangle::Rectangle(int x, int y, int w, int h) {
	xLow = x;
	yLow = y;
	width = w;
	height = h;

	std::cout << ++id << "��° Rectangle ��ü ����\n\n";
}

Rectangle::~Rectangle() {
	std::cout << "��ǥ (" << xLow << ',' << yLow << ')'
		<< " Rectangle ��ü �Ҹ�\n\n";
}

std::ostream& operator <<(std::ostream& os, Rectangle& r) {
	os << "height : " << r.height << std::endl
		<< "width : " << r.width << std::endl
		<< "x : " << r.xLow << std::endl
		<< "y : " << r.yLow << std::endl << std::endl;

	return os;
}

Rectangle Rectangle::operator +(Rectangle& r) {

	int sum_x, sum_y, sum_w, sum_h;

	sum_x = xLow + r.xLow;
	sum_y = yLow + r.yLow;
	sum_w = width + r.width;
	sum_h = height + r.height;

	return Rectangle(sum_x, sum_y, sum_w, sum_h);
}