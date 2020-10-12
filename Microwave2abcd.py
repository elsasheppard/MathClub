string = ["abcd","abdc", "acbd","acdb","adbc","adcb","bacd","badc","bcad","bcda","bdac","bdca","cadb","cabd","cbab","cbda","cdab","cdba","dabc","dacb","dbac","bdca","dcab","dcba"]
substring = ["ab","ba","bc","cb","cd","dc"]
a = 26
for i in string:
  for j in substring:
  if string[i].find(substring[j]) = -1:
    a-=1
print(a)

# if the string contains any of the substrings, subtract 1
# should return 2

# doesn't actually work; this is basically what I want it to do
# need more python experience...
