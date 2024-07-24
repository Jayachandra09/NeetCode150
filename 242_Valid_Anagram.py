def ValidAnagram(s, t) :
  # it is a valid method
  if len(s)==len(t) :
    return False
  countS, countT = {}, {}
  for i in range(len(s)) :
    countS[s[i]] = 1+countS.get(s[i],0)
    countT[t[i]] = 1+countT.get(t[i],0)
  return countS==countT

  ]
#But we can solve this by using Counter also 
from collections import Counter
def ValidAnagram(s, t):
  return Counter(s)==Counter(t)

#Driver Code
s = "racecar"
t = "carrace"
result = ValidAnagram(s, t)
print(result)
