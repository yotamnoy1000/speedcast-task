#ping_example: ping.c
#	$(CROSS_COMPILE)gcc -Wall -I../ -O3 -o ping_example  ping_common.c ping.c
#
#clean:
#	rm ./ping_example

#ping_example: newping.c
#	$(CROSS_COMPILE)gcc -std=c++11 -I../ -O3 -o ping_example newping.c
#
#clean:
#	rm ./ping_example

# Compiler settings
CC = gcc              # C compiler
CXX = g++             # C++ compiler
CFLAGS = -Wall -O2          # C compiler flags
CXXFLAGS = -Wall -O2  # C++ compiler flags

# Object files
C_OBJECTS = newping.o
CXX_OBJECTS = main.o

# Target executable
TARGET = program

# Rules to build the program

# Default rule: compile and link everything
all: $(TARGET)

# Rule to link C and C++ object files into an executable
$(TARGET): $(C_OBJECTS) $(CXX_OBJECTS)
	$(CXX) $(C_OBJECTS) $(CXX_OBJECTS) -o $(TARGET)

# Rule to compile C code into object files
newping.o: newping.c
	$(CC) $(CFLAGS) -c newping.c -o newping.o

# Rule to compile C++ code into object files
main.o: main.cpp
	$(CXX) $(CXXFLAGS) -c main.cpp -o main.o

# Clean up object files and the executable
clean:
	rm -f $(C_OBJECTS) $(CXX_OBJECTS) $(TARGET)

# Phony target to avoid conflicts with filenames
.PHONY: all clean