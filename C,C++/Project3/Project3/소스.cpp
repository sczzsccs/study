#include <stdio.h>
#include <iostream>
using namespace std;

void Func(int *pA) {
	printf("PointA가 가리키는 주소 값: %p\n", pA);
	printf("*PointA의 참조 값: %d\n", *pA);
	printf("&PointA의 주소: %p\n", &pA);
}

class MyClass
{
public:
    MyClass() = default;
	MyClass(string name) { this->name = name; 
		cout << "MyClass Create name:" << name; }
	virtual void Print_Name() {};
	virtual ~MyClass(){ cout << "Myclass Delete" << endl; };
protected:
    string name;
};

class MyClass_Son : public MyClass
{
public:
	MyClass_Son(string name) { this->name = name; 
		cout << "Myclass_Son Create "; }
	void Print_Name() { cout << "Myclass_Son name:" << name << endl; };
	~MyClass_Son(){ cout << "Myclass_Son Delete "; };
};

class MyClass_Son2 : public MyClass
{
public:
	MyClass_Son2(string name) { this->name = name; }
	void Print_Name() { cout << "Myclass_Son2 name:" << name << endl; };
	~MyClass_Son2() { cout << "Myclass_Son2 Delete "; };
};


//void main() {
//	/*int A = 32;
//	void(*pFunc)(int*);
//
//	Func(&A);
//	pFunc = Func;
//	printf("\n함수pFunc가 가리키는 함수의 주소: %p\n\n", pFunc);*/
//
//    // 2.) 
//    /*for (int i = 1; i < 5; i++)
//    {
//        for (int j = 4; j > i; j--)
//        {
//            printf(" ");
//        }
//        for (int j = 0; j < i*2-1; j++)
//        {
//            printf("*");
//        }
//        printf("\n");
//    }*/
//
//    int a = 16;
//    a *= 2;
//    a /= 2;
//    printf("%d", a);
//}

void main() {
	MyClass* A = new MyClass_Son("dds");
	A->Print_Name();
	delete A;
	A = new MyClass_Son2("sss");
	A->Print_Name();
	delete A;
}