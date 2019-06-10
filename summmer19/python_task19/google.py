#!/usr/bin/python3
try:
    from googlesearch import search
except importError:
    print("no module named 'google'found")
# for search
query = "www.google.com"
for j in search(query, tld="co.in", num=10, stop=1, pause=2):
    print(j)
