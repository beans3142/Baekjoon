#pragma once

#include <iostream>

class Rectangle

{
private:
	static int id;
	int width;
	int height;
	int xLow, yLow;

public:
	Rectangle(int, int, int, int);
	~Rectangle();

	int getAreaSize()
	{
		return width*height;
	}

	friend std::istream& operator   >>  (std::istream &in, Rectangle &Rectangle)
	{
		in >> Rectangle.xLow >> Rectangle.yLow >> Rectangle.width >> Rectangle.height;
		return in;
	}

	friend std::ostream& operator <<(std::ostream&, Rectangle&);
	Rectangle operator &(Rectangle&);
	Rectangle operator and(Rectangle&);
	Rectangle operator +(Rectangle&);
};