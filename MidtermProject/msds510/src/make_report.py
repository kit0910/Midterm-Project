import msds510.util as mod
import csv
import sys

arg_list = sys.argv

filename = arg_list[1]    #fieldname variable set to the first argument
mark_down = arg_list[2]   #mark_down variable set to the second argument

lines = []                 #lines is a list
rank = 1                    #the ranking

file = open(mark_down, 'w')  #file is open to mark_down in writemode

with open(filename,'r') as csv_file:                #open file in readmode
    csv_reader = csv.DictReader(csv_file)            #read as a dictionary entry

    for line in csv_reader:                      #for each line in the reader

        if rank == 11:                       #if rank is equal to 11 then break. Stop because mark_down is for the top 10
            break

        file.write('# '+str(rank)+'. '+line['name_alias']+'\n')            #conditions of the mark_down: ranking, number of appearances, strip of newline character, include year joined, years since joining, URL and notes.
        file.write('* Number of Appearances: '+str(line['appearances'])+'\n')
        file.write('* Year Joined: '+str(line['year'])+'\n')
        file.write('* Years Since Joining: 55'+str(line['years_since_joining'])+'\n')
        file.write('* URL: '+line['url']+'\n')
        file.write('## Notes'+'\n')
        file.write(line['notes']+'\n')
        file.write('\n')

        rank += 1                  #add the ranking from 1

    file.close()                  #close file
