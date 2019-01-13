import re
print re.match(r'o', 'google vs yahoo')  # None
print re.search(r'oo', 'google vs yahoo').group()  # oo
print re.match(r'go', 'google vs yahoo').start()  # 0
print re.search(r'google', 'google vs yahoo').end()  # 6
# google vs yahoo
print re.search(r'(([a-z]+)\svs\s([a-z]+))', 'google vs yahoo').group(1)
# google
print re.search(r'(([a-z]+)\svs\s([a-z]+))', 'google vs yahoo').group(2)
# yahoo
print re.search(r'(([a-z]+)\svs\s([a-z]+))', 'google vs yahoo').group(3)
print re.search(r'([a-z]+\svs\s[a-z]+)', 'google vs yahoo').span()  # (0, 15)
