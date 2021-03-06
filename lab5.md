# Lab 5
Alexander Monaco

## Part 1

### Step 1
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step1-code.png)

![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step1-results.png)


### Step 2
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step2-code.png)

![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step2-results.png)


### Step 3
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step3-code.png)

![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step3-results.png)


### Step 4
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step4-code.png)

![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step4-code-mathfunctions.png)

![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step4-results1.png)
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step4-results2.png)
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step4-results3.png)
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step4-results4.png)


### Step 5
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step5-code.png)

![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step5-code-mathfunctions.png)

![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step5-results1.png)
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step5-results2.png)
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step5-results3.png)
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step5-results4.png)
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab5/lab5-part1/step5-results5.png)







## Part 2

### My Makefile
```
all: static_block dynamic_block
clean:
	rm *.o *.so dynamic_block *.a static_block
dynamic_block: program.o lib_shared.so
	cc program.o lib_shared.so -o dynamic_block -Wl,-rpath='$$ORIGIN'
static_block: program.o lib_static.a
	cc program.o lib_static.a -o static_block
program.o: program.c
	cc -c program.c -o program.o
lib_shared.so: block.o
	cc -shared -o lib_shared.so block.o
lib_static.a: block.o
	ar qc lib_static.a block.o
block.o: source/block.c
	cc -fPIC -c source/block.c -o block.o
```


### CMakeLists.txt
```
cmake_minimum_required(VERSION 3.3)
project(static_dynamic)

add_library(lib_static STATIC source/block.c)
add_library(lib_shared SHARED source/block.c)

add_executable(static_block program.c)
add_executable(dynamic_block program.c)

target_link_libraries(static_block lib_static)
target_link_libraries(dynamic_block lib_shared)
```


### Makefile created by cmake
```
# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Default target executed when no arguments are given to make.
default_target: all

.PHONY : default_target

# Allow only one "make -f Makefile2" at a time, but pass parallelism.
.NOTPARALLEL:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/parallels/Documents/Lab-Example2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/parallels/Documents/Lab-Example2

#=============================================================================
# Targets provided globally by CMake.

# Special rule for the target edit_cache
edit_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "No interactive CMake dialog available..."
	/usr/bin/cmake -E echo No\ interactive\ CMake\ dialog\ available.
.PHONY : edit_cache

# Special rule for the target edit_cache
edit_cache/fast: edit_cache

.PHONY : edit_cache/fast

# Special rule for the target rebuild_cache
rebuild_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake to regenerate build system..."
	/usr/bin/cmake -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : rebuild_cache

# Special rule for the target rebuild_cache
rebuild_cache/fast: rebuild_cache

.PHONY : rebuild_cache/fast

# The main all target
all: cmake_check_build_system
	$(CMAKE_COMMAND) -E cmake_progress_start /home/parallels/Documents/Lab-Example2/CMakeFiles /home/parallels/Documents/Lab-Example2/CMakeFiles/progress.marks
	$(MAKE) -f CMakeFiles/Makefile2 all
	$(CMAKE_COMMAND) -E cmake_progress_start /home/parallels/Documents/Lab-Example2/CMakeFiles 0
.PHONY : all

# The main clean target
clean:
	$(MAKE) -f CMakeFiles/Makefile2 clean
.PHONY : clean

# The main clean target
clean/fast: clean

.PHONY : clean/fast

# Prepare targets for installation.
preinstall: all
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall

# Prepare targets for installation.
preinstall/fast:
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall/fast

# clear depends
depend:
	$(CMAKE_COMMAND) -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
.PHONY : depend

#=============================================================================
# Target rules for targets named lib_static

# Build rule for target.
lib_static: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 lib_static
.PHONY : lib_static

# fast build rule for target.
lib_static/fast:
	$(MAKE) -f CMakeFiles/lib_static.dir/build.make CMakeFiles/lib_static.dir/build
.PHONY : lib_static/fast

#=============================================================================
# Target rules for targets named lib_shared

# Build rule for target.
lib_shared: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 lib_shared
.PHONY : lib_shared

# fast build rule for target.
lib_shared/fast:
	$(MAKE) -f CMakeFiles/lib_shared.dir/build.make CMakeFiles/lib_shared.dir/build
.PHONY : lib_shared/fast

#=============================================================================
# Target rules for targets named static_block

# Build rule for target.
static_block: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 static_block
.PHONY : static_block

# fast build rule for target.
static_block/fast:
	$(MAKE) -f CMakeFiles/static_block.dir/build.make CMakeFiles/static_block.dir/build
.PHONY : static_block/fast

#=============================================================================
# Target rules for targets named dynamic_block

# Build rule for target.
dynamic_block: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 dynamic_block
.PHONY : dynamic_block

# fast build rule for target.
dynamic_block/fast:
	$(MAKE) -f CMakeFiles/dynamic_block.dir/build.make CMakeFiles/dynamic_block.dir/build
.PHONY : dynamic_block/fast

program.o: program.c.o

.PHONY : program.o

# target to build an object file
program.c.o:
	$(MAKE) -f CMakeFiles/static_block.dir/build.make CMakeFiles/static_block.dir/program.c.o
	$(MAKE) -f CMakeFiles/dynamic_block.dir/build.make CMakeFiles/dynamic_block.dir/program.c.o
.PHONY : program.c.o

program.i: program.c.i

.PHONY : program.i

# target to preprocess a source file
program.c.i:
	$(MAKE) -f CMakeFiles/static_block.dir/build.make CMakeFiles/static_block.dir/program.c.i
	$(MAKE) -f CMakeFiles/dynamic_block.dir/build.make CMakeFiles/dynamic_block.dir/program.c.i
.PHONY : program.c.i

program.s: program.c.s

.PHONY : program.s

# target to generate assembly for a file
program.c.s:
	$(MAKE) -f CMakeFiles/static_block.dir/build.make CMakeFiles/static_block.dir/program.c.s
	$(MAKE) -f CMakeFiles/dynamic_block.dir/build.make CMakeFiles/dynamic_block.dir/program.c.s
.PHONY : program.c.s

source/block.o: source/block.c.o

.PHONY : source/block.o

# target to build an object file
source/block.c.o:
	$(MAKE) -f CMakeFiles/lib_static.dir/build.make CMakeFiles/lib_static.dir/source/block.c.o
	$(MAKE) -f CMakeFiles/lib_shared.dir/build.make CMakeFiles/lib_shared.dir/source/block.c.o
.PHONY : source/block.c.o

source/block.i: source/block.c.i

.PHONY : source/block.i

# target to preprocess a source file
source/block.c.i:
	$(MAKE) -f CMakeFiles/lib_static.dir/build.make CMakeFiles/lib_static.dir/source/block.c.i
	$(MAKE) -f CMakeFiles/lib_shared.dir/build.make CMakeFiles/lib_shared.dir/source/block.c.i
.PHONY : source/block.c.i

source/block.s: source/block.c.s

.PHONY : source/block.s

# target to generate assembly for a file
source/block.c.s:
	$(MAKE) -f CMakeFiles/lib_static.dir/build.make CMakeFiles/lib_static.dir/source/block.c.s
	$(MAKE) -f CMakeFiles/lib_shared.dir/build.make CMakeFiles/lib_shared.dir/source/block.c.s
.PHONY : source/block.c.s

# Help Target
help:
	@echo "The following are some of the valid targets for this Makefile:"
	@echo "... all (the default if no target is provided)"
	@echo "... clean"
	@echo "... depend"
	@echo "... edit_cache"
	@echo "... rebuild_cache"
	@echo "... lib_static"
	@echo "... lib_shared"
	@echo "... static_block"
	@echo "... dynamic_block"
	@echo "... program.o"
	@echo "... program.i"
	@echo "... program.s"
	@echo "... source/block.o"
	@echo "... source/block.i"
	@echo "... source/block.s"
.PHONY : help



#=============================================================================
# Special targets to cleanup operation of make.

# Special rule to run CMake to check the build system integrity.
# No rule that depends on this can have commands that come from listfiles
# because they might be regenerated.
cmake_check_build_system:
	$(CMAKE_COMMAND) -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
.PHONY : cmake_check_build_system
```


### Sizes
static_block = 8784

dynamic_block = 8600


### Results from my Makefile
```
parallels@parallels-vm:~/Documents/Lab-Example$ ./static_block 
d y n a m i c   o r   s t a t i c 
y n a m i c   o r   s t a t i c d 
n a m i c   o r   s t a t i c d y 
a m i c   o r   s t a t i c d y n 
m i c   o r   s t a t i c d y n a 
i c   o r   s t a t i c d y n a m 
c   o r   s t a t i c d y n a m i 
  o r   s t a t i c d y n a m i c 
o r   s t a t i c d y n a m i c   
r   s t a t i c d y n a m i c   o 
  s t a t i c d y n a m i c   o r 
s t a t i c d y n a m i c   o r   
t a t i c d y n a m i c   o r   s 
a t i c d y n a m i c   o r   s t 
t i c d y n a m i c   o r   s t a 
i c d y n a m i c   o r   s t a t 
c d y n a m i c   o r   s t a t i 
parallels@parallels-vm:~/Documents/Lab-Example$ ./dynamic_block 
d y n a m i c   o r   s t a t i c 
y n a m i c   o r   s t a t i c d 
n a m i c   o r   s t a t i c d y 
a m i c   o r   s t a t i c d y n 
m i c   o r   s t a t i c d y n a 
i c   o r   s t a t i c d y n a m 
c   o r   s t a t i c d y n a m i 
  o r   s t a t i c d y n a m i c 
o r   s t a t i c d y n a m i c   
r   s t a t i c d y n a m i c   o 
  s t a t i c d y n a m i c   o r 
s t a t i c d y n a m i c   o r   
t a t i c d y n a m i c   o r   s 
a t i c d y n a m i c   o r   s t 
t i c d y n a m i c   o r   s t a 
i c d y n a m i c   o r   s t a t 
c d y n a m i c   o r   s t a t i 
```


### Results from cmake
```
parallels@parallels-vm:~/Documents/Lab-Example2$ ./static_block 
d y n a m i c   o r   s t a t i c 
y n a m i c   o r   s t a t i c d 
n a m i c   o r   s t a t i c d y 
a m i c   o r   s t a t i c d y n 
m i c   o r   s t a t i c d y n a 
i c   o r   s t a t i c d y n a m 
c   o r   s t a t i c d y n a m i 
  o r   s t a t i c d y n a m i c 
o r   s t a t i c d y n a m i c   
r   s t a t i c d y n a m i c   o 
  s t a t i c d y n a m i c   o r 
s t a t i c d y n a m i c   o r   
t a t i c d y n a m i c   o r   s 
a t i c d y n a m i c   o r   s t 
t i c d y n a m i c   o r   s t a 
i c d y n a m i c   o r   s t a t 
c d y n a m i c   o r   s t a t i 
parallels@parallels-vm:~/Documents/Lab-Example2$ ./dynamic_block 
d y n a m i c   o r   s t a t i c 
y n a m i c   o r   s t a t i c d 
n a m i c   o r   s t a t i c d y 
a m i c   o r   s t a t i c d y n 
m i c   o r   s t a t i c d y n a 
i c   o r   s t a t i c d y n a m 
c   o r   s t a t i c d y n a m i 
  o r   s t a t i c d y n a m i c 
o r   s t a t i c d y n a m i c   
r   s t a t i c d y n a m i c   o 
  s t a t i c d y n a m i c   o r 
s t a t i c d y n a m i c   o r   
t a t i c d y n a m i c   o r   s 
a t i c d y n a m i c   o r   s t 
t i c d y n a m i c   o r   s t a 
i c d y n a m i c   o r   s t a t 
c d y n a m i c   o r   s t a t i 
```
