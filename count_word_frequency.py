"""
count word frequency
"""
text="i love bangladesh and dhaka and gazipur"
words=text.split()
word_count={}
for word in words:
    word_count[word]=word_count.get(word,0)+1
    print(f"word frequency:{word_count}")
