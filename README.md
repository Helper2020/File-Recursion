# File-Recursion
Show Me The Data Structures Udacity Project

Finding Files.

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is the test directory!
./testdir <br>
./testdir/subdir1  <br>
./testdir/subdir1/a.c  <br>
./testdir/subdir1/a.h <br>
./testdir/subdir2 <br>
./testdir/subdir2/.gitkeep <br>
./testdir/subdir3 <br>
./testdir/subdir3/subsubdir1 <br>
./testdir/subdir3/subsubdir1/b.c <br>
./testdir/subdir3/subsubdir1/b.h <br>
./testdir/subdir4 <br>
./testdir/subdir4/.gitkeep <br>
./testdir/subdir5 <br>
./testdir/subdir5/a.c <br>
./testdir/subdir5/a.h <br>
./testdir/t1.c <br>
./testdir/t1.h <br>

Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().
