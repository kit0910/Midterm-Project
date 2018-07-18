import msds510.util as mod   #imports the utility module to help with the functions of the scripts. Processes the avenger file
import sys
import csv


arg_list = sys.argv

file = arg_list[1]  #the file takes two arguments the original and the modified
modified_file = arg_list[2]


def main():
    with open(file, 'r',newline='') as csv_file: #open file in read, newline denoted by single quote.
        lines = csv_file.readlines()             #lines variable set to read each line in the file

        fields  = mod.line_to_row(lines[0])         #fields variable set to read each line in a row from the header


        nice_fields = mod.line_to_row(mod.make_nice_name(lines[0]))  #fields are unique name in the modified file header
        nice_fields.append('month_joined')                          #add the month joined to the fields

        lines.remove(lines[0])                                      #remove the lines in the header from lines
        with open(modified_file, 'w',encoding='utf-8') as new_file:   #open modfied and processed file in write mode
            #List that contains the header of the csv file             #

            csv_writer = csv.DictWriter(new_file, fieldnames=nice_fields, delimiter=',')  #write like a dictionary with the new file, fieldnames set to nice fields and with delimiter
            csv_writer.writeheader()

            #writing one line at a time in the new csv file
            for line in lines:
                row = mod.line_to_row(line)
                record = mod.row_to_record(row,nice_fields)

                transformed_record = mod.transform_record(record)  #the new file record is transformed record in the dictionary for each record

                transformed_record['month_joined'] = mod.get_month(str(transformed_record['full_reserve_avengers_intro']))  #new record month joined is changed
                csv_writer.writerow(transformed_record)   #use the row writer method to write the tranformed record for each row

if __name__ == '__main__':
     main()
