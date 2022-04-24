#include <iostream>
#include <string>

class Polynomial
{
public:
	int pn[101] = { 0, };


	void input()
	{
		std::string s;
		getline(std::cin, s);
		int size = s.size();
		int cnt = 0;
		std::string coefficient="";
		std::string term="";
		for (int i = 0; i < size; i++)
		{
			if (s[i] == ' ')
			{
				cnt++;
			}
			else if (cnt == 0)
			{
				coefficient += s[i];
			}
			else
			{
				term += s[i];
			}
			if (cnt == 2)
			{
				int coef = stoi(coefficient);
				int te = stoi(term);
				pn[te] += coef;
				coefficient = "";
				term = "";
				cnt = 0;
			}
		}
		int coef = stoi(coefficient);
		int te = stoi(term);
		pn[te] += coef;
	}

	void print()
	{
		bool printed = false;
		for (int i = 100; i >= 0; i--)
		{
			if (pn[i] != 0)
			{
				if (printed) std::cout << " + ";
				std::cout << pn[i] << "x^" << i;
				printed = true;
			}
		}
		std::cout << std::endl;
	}

	long long int eval(int x)
	{
		long long int result = 0;
		for (int i = 0; i <= 100; i++)
		{
			result += pn[i] * pow(x,i);
		}
		return result;
	}

};

Polynomial merge(Polynomial polyA, Polynomial polyB)
{
	Polynomial polyC;
	for (int i = 0; i <= 100; i++)
	{
		if (polyA.pn[i] != 0)
		{
			for (int j = 0; j <= 100; j++)
			{
				if (polyB.pn[j] != 0)
				{
					polyC.pn[i + j] += polyA.pn[i] * polyB.pn[j];
				}
			}
		}
	}
	return polyC;
}

int main()
{
	Polynomial polyA;
	polyA.input();
	polyA.print();
	Polynomial polyB;
	polyB.input();
	polyB.print();
	Polynomial polyC = merge(polyA, polyB);
	polyC.print();
	int num;
	std::cin >> num;
	std::cout << polyA.eval(num) << " " << polyB.eval(num) << " " << polyC.eval(num);
}

// 2 6 3 4 -2 6 4 7