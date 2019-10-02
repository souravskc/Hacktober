#include <iostream>

using namespace std;
class vect{
public:
    vect(int n);
    ~vect();


    void setdata(int n)
    {

        *(data + 5) = n;
    }
    vect(const vect&a)
    {
        size = a.size;
        data=new int[size];
        for(int i=0;i<size;i++)
        {
            data[i]= a.data[i];
        }
    }
    void printdata()
{
    cout<<*(data+5);
}
    int getsize()
{

    return size;}
   vect &operator=(vect &a)
    {
        if(this!=&a)
        {
            delete []data;
            size =a.size;
            data = new int[size];
            for(int i=0;int<size;i++)
                data[i]=a.data[i];
        }
        return *this;/* for any instance of a class oobjectr,this is defined to be this instance of currrently calling object
        every class that allocated its own object using new should
            define a destructor to free any allocated object
            define a copy constructor which allocates its pwn new member storage and copys the content of variable
            define an assignment operator which deallocates new storage and copies all member variable

            */
    }



private:


   int* data;
   int size;







   };
   vect::vect(int n=85)
   {
       size=n;
       data= new int[n];


   }
   vect::~vect()
   {
       delete [] data;
   }

int main()
{
    /* if the class object comes existance dynamically using new operator ,the destructor will be called where object will be destroyed using delete operator
    If a class variable comes into existance becoz it is a local variable,in a function that has been called e called when the fxn returns
*/
vect a(100);
vect b(a);

cout<< a.getsize()<<b.getsize()<<"\n";
cout<<"\n";
a.setdata(50);

a.printdata();
/*since u provide a no copy destructor the system uses its default.
the arose becoz v alocated memory and v used system default copy cons. and assign a to b
If a class allocate memory you should  provide a copy constructor and a assignment operator to allocate new memory for object*/

}
/*


complex data struct typically involves the interaction of many classes
in such cases ther are often issues cordinating the acess of these classes to allow sharing this classes
we can mention the fxn frnd which helps to access the private data of class

