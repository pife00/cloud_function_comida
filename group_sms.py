import pandas as pd
import datetime
def groupSms(debts):
    
    data = pd.DataFrame.from_dict(debts['noInclude'])
    
    data['date'] = data['date'].apply(lambda x:noUnixTime(x))+","
    data['product'] = data['product']+","
   
    
    testValue = data.groupby('name').agg(value=('value', 'sum'),
                                     product=('product', 'sum'),
                                     date=('date', 'sum')
                                     )
    tel = data.groupby(['name', 'contact'])['value'].sum()
    tel = tel.reset_index()

    testValue = testValue.reset_index()
    testValue['contact'] = tel['contact']
    
    
    testValue = testValue.to_json(orient='records')
    return testValue
    


def noUnixTime(data):
    mydate = datetime.datetime.fromtimestamp(data/1000).strftime('%b/%y')
    return mydate