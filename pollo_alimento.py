import pandas as pd
from tabla_de_alimentos import table

bulto_kilo = 40
iniciacion= 100458
engorde = 99766
redondeando = 100000

crecentina_dias = 20


index_ = ['semana 1','semana 2','semana 3','semana 4','semana 5','semana 6','semana 7','semana 8']

df = pd.DataFrame(table,index=index_)

#Crecentina
semana1 = df.loc['semana 1'].sum()
semana2 = df.loc['semana 2'].sum()
semana3 = df.loc['semana 3'][0:6].sum()

#Engorde
sem3 = df.loc['semana 3'][6].sum()
semana4 = df.loc['semana 4'].sum()
semana5 = df.loc['semana 5'].sum()
semana6 = df.loc['semana 6'].sum()
semana7 = df.loc['semana 7'].sum()
semana8 = df.loc['semana 8'].sum()

#1109
iniciacion_gramos20 = int(semana3 +semana2 + semana1)

#7582
engorde_gramos36 =  int (sem3+ semana4 + semana5 + semana6 + semana7 + semana8 )


#8691 => 
gramos_comidos_total = int(df.iloc[:,0:8].sum().sum())

#8,691kg
kilos_comidos = float(gramos_comidos_total /1000)

#21%
porcentaje_en_bulto = float((kilos_comidos / bulto_kilo) * 100)

#21,727
valor_por_bulto = float((porcentaje_en_bulto * redondeando)/100)

toSend = {
    "iniciacion_gramos20":iniciacion_gramos20,
    "engorde_gramos36":engorde_gramos36,
    "gramos_comidos_total":gramos_comidos_total,
    "kilos_comidos":kilos_comidos,
    "porcentaje_en_bulto": porcentaje_en_bulto,
    }

#print(valor_por_bulto)






#gramos_iniacion = bulto_kilo * 1000
##print(gramos_iniacion)
