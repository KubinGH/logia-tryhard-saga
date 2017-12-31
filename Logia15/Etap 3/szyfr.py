def deszyfr(alphabet, rects):
    alphabet = " " + alphabet
    return "".join(alphabet[rect[0]//10] for rect in sorted(rects, key=lambda p: p[1])).split(" ")

deszyfr('acdeh',[[10,20],[30,10],[50,40],[20,30]])
deszyfr('rklotam',[[60,10],[30,20],[60,30],[0,40],[70,50],[60,60],[0,70],[20,80],[40,90],[50,100],[60,110]])
