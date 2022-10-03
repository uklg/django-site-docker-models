#!/usr/bin/python3


import urllib.request


fd=open('build','r')
lines=fd.readlines()
fd.close()


ACCESSPORT=None

for l in lines:
  if 'accessport=' in l:
    ACCESSPORT=(l.split('=')[-1].strip())
    
print(ACCESSPORT)


URL="http://127.0.0.1:%s" % ACCESSPORT

print(URL)

response=urllib.request.urlopen(URL)


#help(response)


code=response.getcode()

if code !=200: print('error code not 200')


responselines=response.read()

#for line in responselines:
#  if 'Professional wedding DJ' in line:
#    print(line)


print(responselines[3])

#for line in responselines:
  #if 'nextArrow'.casefold() in line.casefold():
#  print(line)


def caseless_match(searchstring,contenttosearch):
  if searchstring.casefold() in str(contenttosearch).casefold():
    return True
  else:
    return False


if caseless_match('nextArrow',responselines):
  print('yes next')

if caseless_match('Professional wedding DJ',responselines):

  print('yes')



