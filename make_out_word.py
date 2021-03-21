
#Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in
#the middle of the out string, e.g.
#"<<word>>".

def make_out_word(out, word):
  ilk=out[:2]
  son=out[-2:]
  return ilk + word + son
