#include "Rectangle.h"
#include <iostream>
//using namespace std;

int Rectangle::id = 0;

Rectangle::Rectangle(int x, int y, int w, int h) {
	xLow = x;
	yLow = y;
	width = w;
	height = h;

	std::cout << ++id << "th Rectangle object create\n\n";
}

Rectangle::~Rectangle() {
	std::cout << "coordinate (" << xLow << ',' << yLow << ')' << "\n" << "width and height (" << width << ',' << height << ")\n" << "ID : "<< id-- << " Rectangle object deleted\n\n";
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

Rectangle Rectangle::operator and(Rectangle& r) // 이거 교차 거시기 구하느거,
{
	int nx, ny, nw, nh;
	// 밑에 4개 if문은 겹치지 않는 경우 반환시키는 거
	if (xLow + width < r.xLow) return Rectangle(0, 0, 0, 0);	
	if (r.xLow+r.width<xLow) return Rectangle(0, 0, 0, 0);
	if (r.yLow+r.height<yLow) return Rectangle(0, 0, 0, 0);
	if (xLow+height<r.yLow) return Rectangle(0, 0, 0, 0);
	nx = xLow > r.xLow ? xLow : r.xLow;
	ny = yLow > r.yLow ? yLow : r.yLow;
	nw = xLow + width < r.xLow + r.width ? xLow + width : r.xLow + r.width;
	nh = yLow + height < r.yLow + r.height ? yLow + height : r.yLow + r.height;
	return Rectangle(nx, ny, nw-nx, nh-ny);
}