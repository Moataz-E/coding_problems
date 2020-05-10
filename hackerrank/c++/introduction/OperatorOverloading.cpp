#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

class Matrix
{
    public:
        Matrix();
        virtual ~Matrix();
        typedef vector<vector<int>> a;
    protected:
    private:
}

Matrix::Matrix() { }
Matrix::~Matrix() { }

type operator + (Matrix matrix1, Matrix matrix2) 
{
    Matrix result;
    
    for (int i = 0; i < matrix1.a.size(); i++)
    {
        for (int j = 0; j < matrix1.a[i].size(); j++)
        {
            result.a[i][j] = matrix1.a[i][j] + matrix2.a[i][j]
        }
    }
}

