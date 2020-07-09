gdp={}
with open('GDP','r',encoding='utf-8') as f :
    for line in f:
        line=line[:-1]
        l=line.split('：')
        gdp.update({l[0]:l[1]})
print(gdp)
print(gdp['山东'])
print(gdp.get('辽宁'))

