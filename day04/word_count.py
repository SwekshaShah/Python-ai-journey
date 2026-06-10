#Take a paragraph string. Split into words. Count each word's frequency using .count(). Remove duplicates using a set. Print the top 5 most frequent sorted by count. Previews tomorrow's dict content.
"""
para="Even with the advances in science and technology, many people lagged behind and were not able to cope with the pace of growth in many places around the world."
top5=[]
result1=[]
paragraph=para.split()
para_set=set(paragraph)
n=len(para_set)
for i, item in enumerate(para_set):
  result=top5.append(item)
  print(sorted(result,key=lambda result:result[0:6],reverse=True))
  #top5.append((len(item),item))
#result=sorted(top5,key=len,reverse=True)
#print(result[0:6])
#print(result[:(n-6):-1])
#print(result[-6:-1:-1])
"""

para = "Even with the advances in science and technology, many people lagged behind and were not able to cope with the pace of growth in many places around the world."

paragraph = para.lower().split()
para_set = set(paragraph)

top5 = []

for i, item in enumerate(para_set):
    count = paragraph.count(item)
    top5.append((item, count))
top5 = sorted(top5, key=lambda x: x[1], reverse=True)

print("Top 5 frequent words:")
for word, count in top5[:5]:
    print(word, count)