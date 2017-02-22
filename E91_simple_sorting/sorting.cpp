/* Sample code to read in test cases: */
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    
    cout << fixed;
    cout << setprecision(3);
    while (getline(stream, line)) {
        // Do something with the line
        double number;
        vector<double> numbers;
        stringstream s;
        s.str(line);

        while(s >> number)
        {
                numbers.push_back(number);
        }

        sort(numbers.begin(), numbers.end());

        for(auto number : numbers)
                cout << number << " ";

        cout << endl;
        
    }
    return 0;
}
