def reverseStr(istr):
    iarr = istr.split(" ")
    opstr = ""
    for i in range(len(iarr)-1, -1, -1):
      word = iarr[i]
      opstr = opstr+ " " + word + " "
    return opstr

print reverseStr("This! is a string")