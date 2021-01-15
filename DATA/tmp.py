res=[]
dul=[]
with open("test.txt") as f,open("out.txt", "a") as o:
    for i in f.readlines():
        i=i.strip()
        if(i==""):
            res.append("pause")
            dul.append(12)
        else:
            note,dur=i.split(":")
            res.append(note)
            dul.append(float(dur)*100)
    o.write(res.__repr__())
    o.write('\n')
    o.write(dul.__repr__())

         