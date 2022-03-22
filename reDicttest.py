from reDict import reDict as dc

a = dc(**{'aaa':1, 'abc':2, 'bbc':3})
print(str(a))
print(a['aaa'])
print(a[r'a..'])
a.onlyOne = True
print(a['aaa'])
print(a[r'a..'])
a = None
a = dc(aaa=1, BBB=2)
print(str(a))
print(a['aaa'])
print(a[r'a..'])
a.onlyOne = True
print(a['aaa'])
print(a[r'a..'])
print(str(a.values()))
print(str(a.keys()))
