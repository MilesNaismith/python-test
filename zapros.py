import requests
import re
res = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
pattern = r"\w"
ans = re.findall(pattern, res.text)
p =str()
for i in range(len(ans)):
    p += ans[i]
print(p)