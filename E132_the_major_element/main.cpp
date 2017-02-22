#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <map>

using std::cout;
using std::string;
using std::fstream;
using std::stringstream;
using std::map;

void validateArguments(const int argc, char* argv[])
{
    if(argc != 2)
    {
        cout << "not correct amount of arguments: ";
        for(int i = 0; i < argc; ++i)
        {
            if (i != 0) cout << ", ";
            cout << "\"" << argv[i] << "\"";
        }

        cout << "\n";

        exit(1);
    }
}

fstream openFileOrExit(string& filename)
{
    fstream input;

    input.open(filename);

    if(!input.is_open())
    {
        cout << "unable to open file..." << '\n';
        exit(1);
    }

    return input;
}

void parseLine(string line)
{
        //cout << "line: " << line << '\n';

        stringstream linestream(line);

        int nextValue;
        int numberOfValues = 0;
        map<int, int> valueToCount;
        while( linestream >> nextValue)
        {
            valueToCount[nextValue] += 1;
            numberOfValues += 1;

            //cout << numberOfValues << ": ";
            //cout << nextValue << '\n';
            // consume comma
            linestream.ignore(1);
        }

        bool foundMajor = false;
        for(auto keyToValue : valueToCount)
        {
            //cout << keyToValue.first << ": " << keyToValue.second << '\n';
            if(keyToValue.second > (numberOfValues / 2))
            {
                //cout << keyToValue.first << " is major" << '\n';
                cout << keyToValue.first << '\n';
                foundMajor = true;
                break;
            }
        }

        if(!foundMajor)
            cout << "None\n";
}

int main(int argc, char* argv[])
{
    validateArguments(argc, argv);

    string filename(argv[1]);

    //cout << "filename: " << filename << "\n";

    fstream input = openFileOrExit(filename);

    string line;
    while(getline(input, line))
    {
        parseLine(line);
    }

    return 0;
}
