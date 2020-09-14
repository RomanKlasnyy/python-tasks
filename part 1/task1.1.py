"""1) Write regular expression to parse coma separated value (CSV):"""

import re

example = 'Prescilla Winston,Development Director,(555)218-3981,said to call again next week'
result = re.split(",", example)
print(result)
