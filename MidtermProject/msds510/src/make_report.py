import msds510.util as mod
import csv
import sys

arg_list = sys.argv

filename = arg_list[1]
mark_down = arg_list[2]

lines = []
rank = 1

file = open(mark_down, 'w')

with open(filename,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:

        if rank == 11:
            break

        file.write('# '+str(rank)+'. '+line['name_alias']+'\n')
        file.write('* Number of Appearances: '+str(line['appearances'])+'\n')
        file.write('* Year Joined: '+str(line['year'])+'\n')
        file.write('* Years Since Joining: 55'+str(line['years_since_joining'])+'\n')
        file.write('* URL: '+line['url']+'\n')
        file.write('## Notes'+'\n')
        file.write(line['notes']+'\n')
        file.write('\n')

        rank += 1

    file.close()
