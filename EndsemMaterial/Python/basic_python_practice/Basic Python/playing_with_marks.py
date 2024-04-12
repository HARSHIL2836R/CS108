sections = {}
f=open("buggy_marksheet.txt","r")
studs=f.readlines()
f.close()
for stud in studs:
    marks=int(stud.split()[1])
    roll_no=stud.split()[0]
    sec=int(roll_no.split('_')[2])
    try:
        sections[sec].append((roll_no,marks))
    except KeyError:
        sections[sec] = [(roll_no,marks)]

curfile = open("fixed_marksheet.txt","w")
for i in range(max(sections.keys())):
    try:
        final_tup_list = sorted(sections[i+1],key=lambda tup: tup[1], reverse=True)
        for stud in final_tup_list:
            curfile.write(' '.join([stud[0],str(stud[1])]))
            curfile.write("\n")
    except KeyError:
        continue
curfile.close()