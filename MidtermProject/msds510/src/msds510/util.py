import datetime
import calendar


def main():
    print(days_since_joined('2013', '13-Nov'))

def get_month(date):

    if len(date) == 0 or date == 'YES':
        return
    date = date.split('-')

    month = date[1] if date[0].isdigit() else date[0]

    return datetime.datetime.strptime(month,'%b').month

def get_date_joined(year,day):
    date = day.split('-')

    year = int(year)
    month = get_month(day)

    day = int(date[0] if date[0].isdigit() else date[1])%calendar.monthrange(year,month)[1]

    return datetime.date(year,month,day)

def days_since_joined(year,day):
    tday = datetime.date.today()

    return tday - get_date_joined(year,day)

def line_to_row(line):
    return line.split(',')

def row_to_record(row,fields):

     return dict(zip(fields,row))

def make_nice_name(name):
    return name.replace(' ','_').replace('/','_').lower().strip()

def transform_record(record_dict):

    record_dict['notes'] = record_dict['notes'].strip()
    for key, value in record_dict.items():
        if key == 'death' or key == 'return':
            record_dict[key] = to_bool(record_dict[key])
    return record_dict

if __name__ == "__main__":
    # execute only if run as a script
    main()
