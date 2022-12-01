#include<iostream>

class Calculator
{
  public :
    int result;

    void printResult()
    {
      std::cout << result << std::endl;
    }
    void plus(int a, int b)
    {
      result = a + b;
    }
    void minus(int a, int b)
    {
      result = a - b;
    }
    void divide(int a, int b)
    {
      result = a / b;
    }
};

int main()
{
  Calculator* cal = new Calculator();
  cal->plus(1, 3);
  cal->printResult();
  cal->divide(7, 3);
  cal->printResult();
}