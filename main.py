import wikipedia
# print (wikipedia.summary("Wikipedia"))
summary = wikipedia.summary("Wikipedia")
print(summary)
print("\n")
search1 = wikipedia.search("Pewdiepie")
print(search1)
print("\n")
getthecontent = wikipedia.page("Pewdiepie")

print(getthecontent.content)