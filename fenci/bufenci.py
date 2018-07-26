f = open("delete_html.txt").read()
f = f.lower()
with open("bufencitest.txt", "w") as nf:
    nf.write(str(f))