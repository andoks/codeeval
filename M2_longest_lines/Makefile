CXXFLAGS := -std=c++14 -Wall -Werror
#CXXFLAGS := -std=c++03 -Wall -Werror

m2: main.o
	$(CXX) $(CXXFLAGS) -o m2 main.o

main.o:
	$(CXX) $(CXXFLAGS) -c main.cpp

.PHONY: clean
clean:
	rm *.o m2
	
