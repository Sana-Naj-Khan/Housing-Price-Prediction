#!/usr/bin/env python
# coding: utf-8

# In[1]:


def replacer(df):
    import pandas as pd
    Q = pd.DataFrame(df.isna().sum(),columns=["ct"])
    missing_cols = list(Q[Q.ct > 0].index)
    for i in missing_cols:
        if(df[i].dtypes == "object"):
            x = list(df[i].mode())[0]
            df[i] = df[i].fillna(x)
        else:
            x = df[i].mean()
            df[i] = df[i].fillna(x)
            
def outliers(df):
    T = []
    for i in range(0,len(df.columns)):
        for j in range(0,df.shape[0]):
            x = df.iloc[j,i]
            if((x>3)or(x<-3)):
                T.append(j)

    from numpy import unique
    rows_del = list(unique(T))
    return rows_del

def prep(df):
    cat = []
    con = []
    for i in df.columns:
        if(df[i].dtypes == "object"):
            cat.append(i)
        else:
            con.append(i)
    from sklearn.preprocessing import StandardScaler
    ss = StandardScaler()
    import pandas as pd
    df1 = pd.DataFrame(ss.fit_transform(df[con]),columns=con)
    ol=[]
    for i in con:
        ol.extend(df1[(df1[i]>3)|(df1[i]<-3)].index)
    from numpy import unique
    outliers = unique(ol)
    df1 = df1.drop(index=outliers,axis=0)
    df2 = pd.get_dummies(df[cat])
    df2 = df2.drop(index=outliers,axis=0)
    df1.index = range(0,df1.shape[0])
    df2.index = range(0,df2.shape[0])
    dfnew = df1.join(df2)
    return dfnew,outliers
   


# In[ ]:




