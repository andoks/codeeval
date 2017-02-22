// Sample code to read in test cases:
#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    int numberOfLinesToShow;
    stream >> numberOfLinesToShow;
    map<int, string> linesToLength;
    getline(stream, line); // consume rest of first line
    while (getline(stream, line)) {
        // Do something with the line
        linesToLength[line.size()] = line;
    }
    
    int i = 0;
    auto it = linesToLength.rbegin();
    while(i < numberOfLinesToShow && it != linesToLength.rend())
    {
        cout << it->second << '\n';
        it++;
        ++i;
    }
    return 0;
}
