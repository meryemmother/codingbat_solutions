
#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
#both arrays will be length 1 or more.

def common_end(a, b):
  if len(a) and len(b) >=1:
    if a[0]==b[0] :
      return True
    if a[-1]==b[-1]:
      return True
    else:
      return False