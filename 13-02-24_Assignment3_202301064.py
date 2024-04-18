#q1
import pandas as pd
dataset={
    "Tid":["1","2","3","4","5","6","7","8","9","10"],
    "Refund":["Yes","No","No","Yes","No","No","Yes","No","No","No"],
    "Marital Status":["Single","Marreid","Single","Marreid","Devorced","Marreid","Divorced","Single","Marreid","Single"],
    "Taxable Income":["125k","2100k","70k","120k","95k","60k","220k","85k","75k","90k"],
    "Cheat":["No","No","No","No","Yes","No","No","Yes","No","Yes"]

}
var = pd.DataFrame(dataset)
print(var)


#Q2
import pandas as pd

j=pd.read_csv('data.csv')
rows = j.iloc[[0, 4, 7, 8]]
print(rows)


#Q3
import pandas as pd
i=pd.read_csv('data.csv')
print(i)
