#include <iostream>

using namespace std;
/*
**std:cerr**
*Standard output stream for errors*
Object of class ostream that represents the standard error stream oriented to narrow characters (of type char). It corresponds to the C stream stderr.
The standard error stream is a destination of characters determined by the environment. This destination may be shared by more than one standard object (such as cout or clog).
As an object of class ostream, characters can be written to it either as formatted data using the insertion operator (operator<<) or as unformatted data, using member functions such as write.
The object is declared in header <iostream> with external linkage and static duration: it lasts the entire duration of the program.
By default, cerr is synchronized with stderr (see ios_base::sync_with_stdio).
*/

int main()
{
	cout<<"Count the number of pegions"<<endl;
	for (int i = 0; i < 12; i++)
	{
		cerr<<"i:"<<i<<endl;
		cout<<"Pegion "<<i<<endl;
	}
	#ifdef DEBUG
	cerr<<"Exited Loop"<<endl;
	#endif
	cout << "give me a bottle of rum!" << endl;
	return 0;
}
