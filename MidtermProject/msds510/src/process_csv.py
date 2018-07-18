import msds510.util as mod   #imports the utility module to help with the functions of the scripts
import sys
import csv


arg_list = sys.argv

file = arg_list[1]
modified_file = arg_list[2]


def main():  #function
    with open(file, 'r',newline='') as csv_file:
        lines = csv_file.readlines()

        fields  = mod.line_to_row(lines[0])


        nice_fields = mod.line_to_row(mod.make_nice_name(lines[0]))
        nice_fields.append('month_joined')

        lines.remove(lines[0])
        with open(modified_file, 'w',encoding='utf-8') as new_file:
            #List that contains the header of the csv file

            csv_writer = csv.DictWriter(new_file, fieldnames=nice_fields, delimiter=',')
            csv_writer.writeheader()

            #writing one line at a time in the new csv file
            for line in lines:
                row = mod.line_to_row(line)
                record = mod.row_to_record(row,nice_fields)

                transformed_record = mod.transform_record(record)

                transformed_record['month_joined'] = mod.get_month(str(transformed_record['full_reserve_avengers_intro']))
                csv_writer.writerow(transformed_record)

if __name__ == '__main__':
     main()
