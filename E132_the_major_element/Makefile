#CXXFLAGS := -std=c++14 -Wall -Werror
CXXFLAGS := -std=c++03 -Wall -Werror

e132: main.o
	$(CXX) $(CXXFLAGS) -o e132 main.o

main.o:
	$(CXX) $(CXXFLAGS) -c main.cpp

.PHONY: clean
clean:
	rm *.o e132
	
