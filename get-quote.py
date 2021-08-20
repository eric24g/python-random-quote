import random

def primary():
  last = 13
  f = open("quotes.txt") #this opens the file
  quotes = f.readlines() #this reads from the file
  f.close()              #this closes the file

  rnd = random.randint(0, last)
  last = len(quotes) - 1
  print(quotes[rnd])

if __name__== "__main__":
  primary()
