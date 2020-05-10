#include <cstdio>


int main()
{
    int intNum;
    long longNum;
    long long longlongNum;
    char character;
    float floatNum;
    double doubleNum;

    scanf("%d %ld %lld %c %f %lf", &intNum, &longNum, &longlongNum,
        &character, &floatNum, &doubleNum);

    printf("%d\n%ld\n%lld\n%c\n%f\n%lf\n", intNum, longNum, longlongNum,
        character, floatNum, doubleNum);

    return 0;
}
