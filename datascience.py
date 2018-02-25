import csv
import pandas as pd
file="/home/surya/Desktop/sample_dataset.csv"
out="/home/surya/Desktop/result.csv"

df=pd.read_csv(file)
# print(df)

rowcount=len(df.dob)
rowcount=rowcount

# print(df.ix[3])
# ln     SALTER JR
# dob     01/03/68
# gn             F
# fn       WILLIAM
# Name: 3, dtype: object

df['cluster']=0
# adding new column with value 0im
df.columns.name='index'
# changin name of the index column to 'index'
#
# for x in range (rowcount):
#     if df.gn[x]=='F':
#         print(df.index[x],"  ", end='')

# print(df.values[rowcount-1])
# ['SALTER JR' '01/03/68' 'F' 'WILLIAM' 1]


# To display a value at an index
# df.gn.values[3]='G'
k=1
for x in range (rowcount):
    if df.cluster.values[x]==0:
        df.cluster.values[x]=k
        for y in range (rowcount):
            if df.cluster.values[y]==0 and df.fn.values[x]==df.fn.values[y]:
                df.cluster.values[y]=k
        k=k+1
df=df.sort_values(['cluster'])
# for x in range (rowcount):
#     df.index.values[x]=x
# Reseting index values

df=df.reset_index(drop=True)



cluster_size=max(df.cluster.values)
for x in range (cluster_size):
    for y in range (rowcount):
        if df.cluster.values[y]==x:
            if df.gn.values[y]=='F':
                df.cluster.values[y]=x+cluster_size+1

df=df.sort_values(['cluster'])

df=df.reset_index(drop=True)

# print(cluster_size)
# print(df)

# df.drop(['3','7'])
# will delete index 3 & 7 from list

# df.drop(['cluster'], axis=1)
# drop column

cluster_size2=max(df.cluster.values)
# print(cluster_size2)
for x in range (rowcount):
    for y in range (x, rowcount):
        if df.cluster.values[y]==df.cluster.values[x]:
            if df.dob.values[y]!=df.dob.values[x]:
                df.cluster.values[y]=df.cluster.values[y]+cluster_size2
        else:
            break
df=df.sort_values(['cluster', 'dob']).reset_index(drop=True)

df['cluster2']=0
df.cluster2.values[0]=1
k=1
for x in range (rowcount-1):
    if df.cluster2.values[x]!=0 and df.cluster.values[x]==df.cluster.values[x+1]:
        df.cluster2.values[x+1]=k;
    else:
        df.cluster2.values[x+1]=k+1
        k=k+1
df=df.sort_values(['cluster2']).reset_index(drop=True)
df=df.drop(['cluster'], axis=1 )

cluster_size=max(df.cluster2.values)
df['visited']=0
k=0
df.visited.values[0]=0

for x in range (rowcount):
    k=k+1
    if df.visited.values[x]!=0:
        continue
    else:
        df.visited.values[x]=k
    str=df.ln.values[x]
    list1=str.split(' ')
    val2=int(df.cluster2.values[x])
    for y in range (x,rowcount):
        val1=int(df.cluster2.values[y])
        if val1!=val2:
            break
        str=df.ln.values[y]
        list2=str.split(' ')
        flag=0
        for x in (list1):
            if len(x)>2 and x in list2:
                flag=1
        if flag==0:
            df.visited.values[y]=k+1
        else:
            df.visited.values[y]=k

df=df.sort_values(['visited']).reset_index(drop=True)
df=df.drop(['cluster2'], axis=1)
df['patient_id']=0


df.patient_id.values[0]=1
k=1
for x in range (rowcount-1):
    if df.patient_id.values[x]!=0 and df.visited.values[x]==df.visited.values[x+1]:
        df.patient_id.values[x+1]=k;
    else:
        df.patient_id.values[x+1]=k+1
        k=k+1

df=df.drop(['visited'], axis=1)

df.to_csv(out, sep=',', encoding='utf-8', index=False)
print(data)
