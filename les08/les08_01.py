class Date:
    def __init__(self, str_date):
        self.str_date = str(str_date)

    @classmethod
    def extract(cls, string):
        string = string.split('-')
        date = [int(itm) for itm in string]
        return date

    @staticmethod
    def dtvalidation(string):
        days_in_month1 = {'1': '31', '2': '28', '3': '31', '4': '30', '5': '31', '6': '30', '7': '31', '8': '31', '9': '30', '10': '31', '11': '30', '12': '31', }
        days_in_month2 = {'1': '31', '2': '29', '3': '31', '4': '30', '5': '31', '6': '30', '7': '31', '8': '31', '9': '30', '10': '31', '11': '30', '12': '31', }
        extracted = Date.extract(string)
        print(extracted)
        if (extracted[1] > 0) & (extracted[1] < 13):
            if extracted[2] > 0:
                if extracted[2] % 4:
                    if (extracted[0] > 0) & (extracted[0] < int(days_in_month1[str(extracted[1])])):
                        return 'Date is valid'
                    else:
                        return 'dd is not valid'
                else:
                    if (extracted[0] > 0) & (extracted[0] < int(days_in_month2[str(extracted[1])])):
                         return 'Date is valid'
                    else:
                        return 'dd is not valid'
            else:
                return 'yy is not valid'
        else:
            return 'mm is not valid'



testdate = '29-02-2021'
# print(Date.extract(testdate))
print(Date.dtvalidation(testdate))
