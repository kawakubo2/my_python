# regexp_sub.py
import re

tel_pattern = r"^(\d{2,4})-(\d{2,4})-(\d{4})$"

# reg = re.compile(tel_pattern)

tel = '092-292-9999'

print(re.sub(tel_pattern, r"*******-\3", tel))