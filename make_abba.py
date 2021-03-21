
#Given two strings, a and b, return the result of putting them together in the order abba, e.g.
# #" and "Bye" returns "HiByeByeHi".
def make_abba(a, b):
  return a+b+b+a
