import pandas as pd
from datetime import date
def groupSms(debts):
    
    data = pd.DataFrame.from_dict(debts['sms'])
    
    #data['date'] = data['date'].apply(lambda x:'{}'.format(date(x)))
    data['product'] = data['product'].str.upper() + ' '
    print(data['date'])
    """ 
    testValue = data.groupby('name').agg(sum_value=('value', 'sum'),
                                     product=('product', 'sum'),
                                     date=('date', 'sum')
                                     )
    tel = data.groupby(['name', 'contact'])['value'].sum()
    tel = tel.reset_index()

    testValue = testValue.reset_index()
    testValue['contact'] = tel['contact']
    
    print(testValue) """
    #return testValue

    return 'Hello'