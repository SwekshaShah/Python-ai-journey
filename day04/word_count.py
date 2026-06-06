#Take a paragraph string. Split into words. Count each word's frequency using .count(). Remove duplicates using a set. Print the top 5 most frequent sorted by count. Previews tomorrow's dict content.
para="Even with the advances in science and technology, many people lagged behind and were not able to cope with the pace of growth in many places around the world."
top5=[]
max_length=0
paragraph=para.split()
para_set=set(paragraph)
n=len(para_set)
for i in para_set:
  top5.append(i)
result=sorted(top5,key=len)
print(result[:(n-6):-1])
