## read a file and push every word to a list

#f = open("Shakespeare.txt", "r")

text = " This is the 100th Etext file presented by Project Gutenberg, and is presented in cooperation with World Library, Inc., from their Library of the Future and Shakespeare CDROMS.  Project Gutenberg often releases Etexts that are NOT placed in the Public Domain!! "

x = text.split()
newstr = []

for word in x:
    if word not in newstr:
        newstr.append(word)

for word in range(0, len(newstr)):
    print(newstr[word], text.count(newstr[word]))
