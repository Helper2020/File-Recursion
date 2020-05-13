import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    sub_files = os.listdir(path)  # O(nm)
    path_list = []

    for file_dir in sub_files:  # O(n)
        new_path = os.path.join(path, file_dir)  # O(n)

        if os.path.isdir(new_path):  # O(1)
            result = find_files(suffix, new_path)
            path_list.extend(result)  # O(k)
        elif suffix.lower() == new_path[-2:].lower():
            path_list.append(new_path)  # O(1)

    return path_list


print('---------------- Test case 1 ----------------')
# Test case 1
result1 = find_files('.c', './testdir')
print(result1)
# ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

print('---------------- Test case 2 ----------------')
# Case where nothing is found
result2 = find_files('.c', './testdir2')
print(result2)
# Should print []

print('---------------- Test case 3 ----------------')
# Case where some files end with c NOT .c
result3 = find_files('.c', './testdir3')
print(result3)
# Should print ['./testdir3/t1.c']

