def versioncmp(v1, v2):
    if v1 == v2:
       return "the two versions are same"

    v1 = v1.split(".")
    v2 = v2.split(".")

    len1 = len(v1)
    len2 = len(v2)
    
    minlen = min(len1, len2)
    for i in range(0, minlen):
          if (int(v1[i]) > int(v2[i])):
             return "v1 is the greater version"
          elif (int(v2[i]) > int(v1[i])):
             return "v2 is the greater version"
          else:
             continue
    if len(v1) > len(v2):
       return "v1 is the greater version"
    else:
       return "v2 is the greater version"


v1 = "20.101.10.10"
v2 = "20.100"

print versioncmp(v1, v2)