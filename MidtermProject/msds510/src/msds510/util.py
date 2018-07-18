import datetime
import calendar


def main():          #defines module
    print(days_since_joined('2013', '13-Nov'))   #display days since joined

def get_month(date):

    if len(date) == 0 or date == 'YES':                   #if date since joined is 0 or YES, return teh date rows
        return
    date = date.split('-')       #date split by delimiter

    month = date[1] if date[0].isdigit() else date[0]      #month is the date from second row if all the dates in the header are digits or else date will be same as in header row

    return datetime.datetime.strptime(month,'%b').month  #return datetime with month

def get_date_joined(year,day):                  #get date joined for year and day
    date = day.split('-')                       #date is set to the day split by delimiter

    year = int(year)                          #year is set to integer year
    month = get_month(day)

    day = int(date[0] if date[0].isdigit() else date[1])%calendar.monthrange(year,month)[1]  #get day number if same as header row or else the second row

    return datetime.date(year,month,day)                     #return the date in format year, month and day

def days_since_joined(year,day):
    today = datetime.date.today()                     #today's date

    return today - get_date_joined(year,day)           #subtract date joined year and day by today's date

def line_to_row(line):
    return line.split(',')                        #for each line in a row return the line split with delimiter, separated by commas

def row_to_record(row,fields):               #for each row in the record return dictioanry with fields and row

     return dict(zip(fields,row))

def make_nice_name(name):
    return name.replace(' ','_').replace('/','_').lower().strip()         #In the name, replace the spaces with underscore, the slashes with underscore and make lowercase

def transform_record(record_dict):                   #read transformed record as dictionary

    record_dict['notes'] = record_dict['notes'].strip()              #the strip the dictionary of notes
    for key, value in record_dict.items():                                #for key in dictionary items value
        if key == 'death' or key == 'return':                       #if key is death or return, the key will be True or False
            record_dict[key] = to_bool(record_dict[key])
    return record_dict

if __name__ == "__main__":
    # execute only if run as a script
    main()
