"""Implement function which merge two files line by line into one new file.
  Empty lines should be skipped optionally (use default fn parameter).
  Retrieve source_file_path1, source_file_path2, target_file_path, skip_empty(default True)."""


def files_merge(source_file1, source_file2, target_file, skip_empty=True):
    with open(source_file1) as f1:
        content1 = f1.readlines()
    content1 = [x.strip() for x in content1]
    with open(source_file2) as f2:
        content2 = f2.readlines()
    content2 = [x.strip() for x in content2]
    merge = []
    while content1 or content2:
        if content1:
            el1 = content1.pop(0)
        elif not content1:
            el1 = ''
        if content2:
            el2 = content2.pop(0)
        elif not content2:
            el2 = ''
        if el1 and el2:
            merge.append(f'{el1} {el2}')
        elif el1:
            merge.append(el1)
        elif el2:
            merge.append(el2)
        else:
            if skip_empty:
                continue
            else:
                merge.append('')
    with open(target_file, "w") as tf:
        tf.writelines(map(lambda line: line + '\n', merge))


files_merge('source1.txt', 'source2.txt', 'result.txt', False)
