import csv

ep1 = []
ep2 = []
ep3 = []
ep4 = []
ep5 = []
ep6 = []

nums1 = []
nums2 = []
nums3 = []
nums4 = []
nums5 = []
nums6 = []

changeLoc1 = []
changeLoc2 = []
changeLoc3 = []
changeLoc4 = []
changeLoc5 = []
changeLoc6 = []

sameLoc1 = []
sameLoc2 = []
sameLoc3 = []
sameLoc4 = []
sameLoc5 = []
sameLoc6 = []

trap1 = []
trap2 = []
trap3 = []
trap4 = []
trap5 = []
trap6 = []

strat1 = []
strat2 = []
strat3 = []
strat4 = []
strat5 = []
strat6 = []

run1 = (1,180)
run2 = (181,339)
run3 = (340,498)
run4 = (499,657)
run5 = (658,816)
run6 = (817,975)

with open('PROBE_trials.csv','rU') as trialFile:
    trialInfo = csv.reader(trialFile,delimiter=',')
    rowNum=0
    for row in trialInfo:
        #for run 1
        if rowNum > 0 and rowNum < run2[0]:
            ep1.append(row[0])
            nums1.append(row[1])
            changeLoc1.append(row[2])
            sameLoc1.append(row[3])
            trap1.append(row[4])
            strat1.append(row[5])
        #for run 2
        elif rowNum > run1[1] and rowNum < run3[0]:
            ep2.append(row[0])
            nums2.append(row[1])
            changeLoc2.append(row[2])
            sameLoc2.append(row[3])
            trap2.append(row[4])
            strat2.append(row[5])
        #for run 3
        elif rowNum > run2[1] and rowNum < run4[0]:
            ep3.append(row[0])
            nums3.append(row[1])
            changeLoc3.append(row[2])
            sameLoc3.append(row[3])
            trap3.append(row[4])
            strat3.append(row[5])
        #for run 4
        elif rowNum > run3[1] and rowNum < run5[0]:
            ep4.append(row[0])
            nums4.append(row[1])
            changeLoc4.append(row[2])
            sameLoc4.append(row[3])
            trap4.append(row[4])
            strat4.append(row[5])
        #for run 5
        elif rowNum > run4[1] and rowNum < run6[0]:
            ep5.append(row[0])
            nums5.append(row[1])
            changeLoc5.append(row[2])
            sameLoc5.append(row[3])
            trap5.append(row[4])
            strat5.append(row[5])
        #for run 6
        elif rowNum > run5[1]:
            ep6.append(row[0])
            nums6.append(row[1])
            changeLoc6.append(row[2])
            sameLoc6.append(row[3])
            trap6.append(row[4])
            strat6.append(row[5])
        else:
            print 'HELP'
            print rowNum
        rowNum += 1

#print ep1
#print ep2
#print ep3
#print ep4
#print ep5
#print ep6

#print nums1
#print nums2
#print nums3
#print nums4
#print nums5
#print nums6

#print changeLoc1
#print changeLoc2
#print changeLoc3
#print changeLoc4
#print changeLoc5
#print changeLoc6

#print sameLoc1
#print sameLoc2
#print sameLoc3
#print sameLoc4
#print sameLoc5
#print sameLoc6

#print trap1
#print trap2
#print trap3
#print trap4
#print trap5
#print trap6

print strat1
print strat2
print strat3
print strat4
print strat5
print strat6