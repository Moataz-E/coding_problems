#include <iostream>
#include <cstdio>

class HelloWorld
{
    public:
        HelloWorld();
        virtual ~HelloWorld();
    protected:
    private:
};

HelloWorld::HelloWorld() { }

HelloWorld::~HelloWorld() { }

int main()
{
    printf("Hello, World!\n");
    return 0;
}

