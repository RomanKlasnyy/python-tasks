"""Implement copy function which copying files into new location.
  Retrieve source_file_path, target_file_path.
  built in module for coping files should be used"""
import shutil


def copy_file(source_file, target_file):
    return shutil.copyfile(source_file, target_file)


copy_file('result.txt', 'copy.txt')
