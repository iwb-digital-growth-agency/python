'''Helper functions for CLV application'''

from datetime import datetime


def date_format(date):
    '''Recognizes Dutch date formats like day/month/year'''
    date_patterns = ['%d-%m-%Y', '%d/%m/%Y']

    for pattern in date_patterns:
        try:
            datetime.strptime(date, pattern).date()
            return pattern
        except ValueError as error:
            # Print for debugging only. Does not return anything
            print(type(error), error)

    return f'Error: could not recognize date format for "{date}"'