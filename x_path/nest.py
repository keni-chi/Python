import json
d = {"form":{"action":"sample.php","method":"get"}}

k = list(d.keys())
print(k)

'''
print(d)

print(d.keys()[0])


tempstr = "[form]"

print(d["form"])
print(dtempstr)
'''




def xpath_get(mydict, path):
    elem = mydict
    try:
        for x in path.strip("/").split("/"):
            try:
                x = int(x)
                elem = elem[x]
            except ValueError:
                elem = elem.get(x)
    except:
        pass

    return elem

foo = {
  'spam':'eggs',
  'morefoo': [{
               'bar':'soap',
               'morebar': {
                           'bacon' : {
                                       'bla':'balbla'
                                     }
                           }
              },
              'bla'
              ]
   }

print (xpath_get(foo, "/morefoo/0/morebar/bacon"))

print('---------')
x = {"action":"sample.php","method":"get"}
y = list(x.keys())[0]
print(y)
