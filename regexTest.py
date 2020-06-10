import re

arrTest = [123123, 512323, 500000, 239, 23490]

pattern = '[5]\d{5}'
pattern2 = '\d{6}'

for i in range(len(arrTest)):
    if re.match(pattern2, str(arrTest[i])):
        print(arrTest[i])