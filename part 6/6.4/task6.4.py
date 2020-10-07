"""Implement get_dir_info function which return directory info (files info, etc.)
  Retrieve dir_path.
  Return dir info object (any data type). (files and their sizes)
- Handle IOException, and other possible exceptions.
- Use Exception handling. """
from datetime import datetime
import os


class Error(Exception):
    """Base class for other exceptions"""
    pass


class EmptyDirectoryError(Error):
    """Raised when the given directory is empty"""
    pass


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date


def get_dir_info(dir_path):
    try:
        with os.scandir(dir_path) as entries:
            entry_count = 0
            for entry in entries:
                entry_count += 1
                info = entry.stat()
                size = os.stat(entry).st_size
                if size < 1024:
                    size_form = f'{size} bytes'
                elif size < 1048576:
                    size_form = f'{round((size / 1024), 2)} KB'
                elif size < 1073741824:
                    size_form = f'{round((size / 1048576), 2)} MB'
                else:
                    size_form = f'{round((size / 1073741824), 2)} TB'
                print(f'{entry.name}\t Last modified: {convert_date(info.st_mtime)}\t Size: {size_form}')
            if entry_count == 0:
                raise EmptyDirectoryError
    except FileNotFoundError:
        print('Error. The directory path does not exist!')
    except NotADirectoryError:
        print('Error. This is not a directory!')
    except EmptyDirectoryError:
        print('Error. The given directory is empty!')


get_dir_info(r'C:\Users\(username)\Desktop\Learning\Python basics\Homework\part 6\6.3')
# copy.txt  	 Last Modified: 07 Oct 2020
# result.txt	 Last Modified: 07 Oct 2020
# task6.3.py	 Last Modified: 07 Oct 2020

get_dir_info(r'C:\Users\(username)\Desktop\Learning\Lol\Kek\Cheburek')
# Error. The directory path does not exist!

get_dir_info(r'C:\Users\(username)\Desktop\Learning\Python basics\Homework\part 6\6.3\task6.3.py')
# Error. This is not a directory!

get_dir_info(r'C:\Users\(username)\Desktop\Learning\Python basics\Homework\part 6\empty')
# Error. The given directory is empty!
