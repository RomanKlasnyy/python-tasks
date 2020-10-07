"""Implement function which copying only uniq lines from one file two other.
  Retrieve source_file_path, target_file_path, returns number of lines copied."""


def unique_line_copy(source_file_path, target_file_path):
    with open(source_file_path) as f:
        content = f.readlines()
    # remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    result = []
    while content:
        el = content.pop(0)
        if el not in result:
            result.append(el)
    with open(target_file_path, "w") as tf:
        tf.writelines(map(lambda line: line + '\n', result))
    return len(result)


print(unique_line_copy("source.txt", "result.txt"))
