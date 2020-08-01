def rev_words(line):
    words = line.split()
    # print(words)
    words.reverse()
    print(" ".join(words))

rev_words("Hello World")

site='www.programming-hero.com'
rev = '.'.join(reversed(site.split('.')))
print(rev)