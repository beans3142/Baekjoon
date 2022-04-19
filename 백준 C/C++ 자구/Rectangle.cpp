#include "Rectangle.h"
#include <iostream>
//using namespace std;

int Rectangle::id = 0;

Rectangle::Rectangle(int x, int y, int w, int h) {
	xLow = x;
	yLow = y;
	width = w;
	height = h;

	//std::cout << ++id << "th Rectangle object create\n\n";
}

Rectangle::~Rectangle() {
	//std::cout << "coordinate (" << xLow << ',' << yLow << ')' << "\n" << "width and height (" << width << ',' << height << ")\n" << "ID : "<< id-- << " Rectangle object deleted\n\n";
}

std::ostream& operator <<(std::ostream& os, Rectangle& r) {
	os << r.xLow << " " << r.yLow << " " << r.width << " " << r.height << std::endl;
	/*
	os << "height : " << r.height << std::endl
		<< "width : " << r.width << std::endl
		<< "x : " << r.xLow << std::endl
		<< "y : " << r.yLow << std::endl << std::endl;
		*/

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

Rectangle Rectangle::operator&(Rectangle& r)
{
	//겹치는 부분을 저장하기 위해 새로운 변수를 생성함.
	int cross_x, cross_y, cross_w, cross_h;
	// Rectangle생성자로 인해 생성된 변수들을 이 함수에서 쓸 이름들에 대입.
	int x = xLow, rx = r.xLow, y = yLow, ry = r.yLow, w = width, rw = r.width, h = height, rh = r.height;
	//가로 길이와 세로 길이에 대한 수를 받아줄 배열 생성(r1).
	int nw[w], nh[h];
	//가로 길이와 세로 길이에 대한 수를 받아줄 배열 생성(r2).
	int rnw[rw], rnh[rh];
	//배열의 위치를 잡아주고 동시에 배열의 크기까지 정해줄 변수 생성.
	int count = 0, rcount = 0;
	//겹치는 부분이 없을 경우에 0값을 리턴해주기위해 변수 생성.
	int howmany = 0;
	//가로 길이를 배열에 저장(작은 수부터)(r1)
	for (int i = x; i <= x + w; i++)
	{
		nw[count] = i;
		count++;
	}
	//가로 길이를 배열에 저장(작은 수부터)(r2)
	for (int i = rx; i <= rx + rw; i++)
	{
		rnw[rcount] = i;
		rcount++;
	}
	//겹치는 부분이 있으면 howmany가 1이되고, 겹치는 가장 작은 수를 cross_x에. 저장한다.
	for (int i = 0; i <= count; i++)
	{
		for (int j = 0; j <= rcount; j++)
		{
			if (nw[i] == rnw[j])
			{
				cross_x = nw[i];
				howmany++;
				/* cross_x를 통해 새로운 가로길이인 cross_w를 구한다.
				기존 xLow + width가 r.xLow + r.width보다 클 경우는 r.xLow + r.width에서 cross_x를 빼고 r.xLow + r.width가 더 클 경우에는 xLow + width에서 cross_x를 뺀다.*/
				cross_w = x + w > rx + rw ? rx + rw - cross_x : x + w - cross_x;
				// x위치를 지정시->더 돌릴 필요가 없음->반복문 밖의 xfinish로 이동.
				goto xfinish;
			}
			// x위치를 지정하지 못했을 경우->코드를 계속 진행시킨다.
			else
				continue;
		}
	}
xfinish:
	//겹치는 x값이 없었을 경우->겹치는 구간이 없는 것이므로 (0,0,0,0)을 반환한다.
	if (howmany == 0)
		return Rectangle(0, 0, 0, 0);
	// y값과 height를 구하기 위해 필요한 변수들을 0으로 초기화한다.
	howmany = 0, count = 0, rcount = 0;
	//세로 길이를 배열에 저장(작은 수부터)(r1)
	for (int i = y; i <= y + h; i++)
	{
		nh[count] = i;
		count++;
	}
	//세로 길이를 배열에 저장(작은 수부터)(r2)
	for (int i = ry; i <= ry + rh; i++)
	{
		rnh[rcount] = i;
		rcount++;
	}
	//겹치는 부분이 있으면 howmany가 1이되고, 겹치는 가장 작은 수를 cross_y에 저장한다.
	for (int i = 0; i <= count; i++)
	{
		for (int j = 0; j <= rcount; j++)
		{
			if (nh[i] == rnh[j])
			{
				cross_y = nh[i];
				howmany++;
				/* cross_y를 통해 새로운 세로길이인 cross_h 구한다.
				기존 yLow + height 가 r.yLow + r.height 보다 클 경우는 r.yLow + r.height에서 cross_y를 빼고 r.yLow + r.height가 더 클 경우에는 yLow + height에서 cross_y를 뺀다.*/
				cross_h = y + h > ry + rh ? ry + rh - cross_y : y + h - cross_y;
				// y위치를 지정시->더 돌릴 필요가 없음->반복문 밖의 yfinish로 이동
				goto yfinish;
			}
			else
				continue;
		}
	}
yfinish:
	//겹치는 y값이 없을 경우->겹치는 부분이 없는 것이므로(0,0,0,0)을 반환한다.
	if (howmany == 0)
		return Rectangle(0, 0, 0, 0);
	//높이나 가로길이가 0일경우->(0,0,0,0)을 반환한다.
	if (cross_h == 0 || cross_w == 0)
		return Rectangle(0, 0, 0, 0);
	//겹치는 부분을 반환하여 새로운 객체를 만든다.
	return Rectangle(cross_x, cross_y, cross_w, cross_h);
}


Rectangle Rectangle::operator and(Rectangle& r) // 이거 교차 거시기 구하느거,
{
	int nx, ny, nw, nh;
	// 밑에 4개 if문은 겹치지 않는 경우 반환시키는 거
	if (xLow + width <= r.xLow) return Rectangle(0, 0, 0, 0);	
	if (r.xLow+r.width<=xLow) return Rectangle(0, 0, 0, 0);
	if (r.yLow+r.height<=yLow) return Rectangle(0, 0, 0, 0);
	if (yLow+height<=r.yLow) return Rectangle(0, 0, 0, 0);
	nx = xLow > r.xLow ? xLow : r.xLow;
	ny = yLow > r.yLow ? yLow : r.yLow;
	nw = xLow + width < r.xLow + r.width ? xLow + width : r.xLow + r.width;
	nh = yLow + height < r.yLow + r.height ? yLow + height : r.yLow + r.height;
	return Rectangle(nx, ny, nw-nx, nh-ny);
}

