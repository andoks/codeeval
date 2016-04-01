/* Sample code to read in test cases: */
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;
int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    while (getline(stream, line)) {
        // Do something with the line
        stringstream strStream;
        strStream.str(line);
        
        int F, B, N;
        strStream >> F >> B >> N;
        
        cout << "f: " << F << ", b: " << B << ", n: " << N << endl;
        
        for(int i = 1; i <= N; i++)
        {
            if((i % F) == 0)
                cout << "F";
            if((i % B) == 0)
                cout << "B";
            if(!((i%F) == 0) && !((i%B) == 0))
                cout << i;
            
            if(i < N)
                cout << " ";
        }
        
        cout << endl;
    }
    return 0;
}
