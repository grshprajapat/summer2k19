import webbrowser 
import time
import subprocess
 from googlesearch import search 
#except ImportError:  
option='''
print("press 1 for vlc")
print("press 2 for google search")
print("press 3 for time")
print("press 4 for ytsongs")
'''
print(option)
choice=input()
if choice=='1':

    subprocess.getoutput('vlc')

elif choice=='2':
    
    data=input("search---->")
    webbrowser.open('http://www.google.com/search?q='+data)
#     print("No module named 'google' found")

# to search
#query = "A computer science portal"

for j in search(query, tld="co.in", num=10, stop=1, pause=2):
    print(j)

elif choice=='3' :
    t=time.ctime()
    print(t)

else :
    data=input("search-->")
    webbrowser.open('http://www.youtube.com/results?search_query='+data)


