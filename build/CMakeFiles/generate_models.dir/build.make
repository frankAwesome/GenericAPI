# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/homebrew/Cellar/cmake/3.26.4/bin/cmake

# The command to remove a file.
RM = /opt/homebrew/Cellar/cmake/3.26.4/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/francois/Documents/GenericAPI

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/francois/Documents/GenericAPI/build

# Utility rule file for generate_models.

# Include any custom commands dependencies for this target.
include CMakeFiles/generate_models.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/generate_models.dir/progress.make

CMakeFiles/generate_models:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/Users/francois/Documents/GenericAPI/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating Python models from Swagger JSON"
	cd /Users/francois/Documents/GenericAPI && /opt/homebrew/Cellar/cmake/3.26.4/bin/cmake -E env PYTHONPATH=/Users/francois/Documents/GenericAPI python generate_models.py

generate_models: CMakeFiles/generate_models
generate_models: CMakeFiles/generate_models.dir/build.make
.PHONY : generate_models

# Rule to build all files generated by this target.
CMakeFiles/generate_models.dir/build: generate_models
.PHONY : CMakeFiles/generate_models.dir/build

CMakeFiles/generate_models.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/generate_models.dir/cmake_clean.cmake
.PHONY : CMakeFiles/generate_models.dir/clean

CMakeFiles/generate_models.dir/depend:
	cd /Users/francois/Documents/GenericAPI/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/francois/Documents/GenericAPI /Users/francois/Documents/GenericAPI /Users/francois/Documents/GenericAPI/build /Users/francois/Documents/GenericAPI/build /Users/francois/Documents/GenericAPI/build/CMakeFiles/generate_models.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/generate_models.dir/depend

