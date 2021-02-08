import pandas as pd

class myClass:

    # This function is to simply initialize the dataframe.
    # The CSV file contains some useless rows, so I deleted them and set the column names.
    def initializeDataframe(self,csvpath,col_name):
        df = pd.read_csv(csvpath)
        df.drop(df.index[:4],inplace=True)
        df.drop(df.columns[2:58],axis = 1,inplace=True)
        df.drop(df.columns[-2:],axis = 1,inplace=True)
        df.columns = col_name
        df.dropna(inplace=True)
        df.reset_index(drop=True,inplace=True)
        return df

    # This function is to change the structure of the dataframe.
    # We need a "tidy" data structure: each variable is a column, each observation is a row.
    def changeStru(self,frame,col_name):
        d = pd.DataFrame(frame['2014'])
        d = d.append(d)
        d = d.append(d)
        dd = pd.DataFrame(frame['2014'])
        d = d.append(dd)
    
        ndf = pd.concat([d,pd.DataFrame(columns = col_name)]) 
        del ndf['2014']  
        ndf.reset_index(drop=True,inplace=True)
        
        k=0
        y=[0,0,0,0,0]
        
        for i in range(0, len(ndf), 5):
            for j in range(0,5):
                ndf.Country[i+j] = frame.Country[k]
                ndf[col_name[1]][i+j] = frame[col_name[1]][k]
                if j==0:
                    ndf.Year[i+j] = '2014'
                    ndf[col_name[3]][i+j] = frame['2014'][y[j]]
                    y[j] = y[j]+1
                elif j==1:
                    ndf.Year[i+j] = '2015'
                    ndf[col_name[3]][i+j] = frame['2015'][y[j]]
                    y[j] = y[j]+1
                elif j==2:
                    ndf.Year[i+j] = '2016'
                    ndf[col_name[3]][i+j] = frame['2016'][y[j]]
                    y[j] = y[j]+1
                elif j==3:
                    ndf.Year[i+j] = '2017'
                    ndf[col_name[3]][i+j] = frame['2017'][y[j]]
                    y[j] = y[j]+1
                elif j==4:
                    ndf.Year[i+j] = '2018'
                    ndf[col_name[3]][i+j] = frame['2018'][y[j]]
                    y[j] = y[j]+1
            k=k+1
        
        ndf[col_name[3]]=ndf[col_name[3]].astype('float64')
        return ndf

    # Use this function to call the initializeDataframe function and the changeStru function
    # To avoid heavy code
    def getDataframe(self,csvPath, col_name, ind):
        
        df = self.initializeDataframe(csvPath,col_name)
        col_name2 = ['Country','Country Code', 'Year', ind]
        df_final = self.changeStru(df,col_name2)

        return df_final

    # In order to display the data more clearly and quickly, we can combine the two dataframes.
    # Because each data file contains different countries with data, we need to do some filtering to keep the same country data.
    def uniteDataframe(self,df,df2,ind,m):
        if m==0:
            df = df[df.Country.isin(df2['Country'])]
            df2 = df2[df2.Country.isin(df['Country'])]
            df.reset_index(drop=True,inplace=True)
            df2.reset_index(drop=True,inplace=True)
            df[ind] = df2[ind]
        else:
            df['lat']=None
            df['lon']=None
            df_geo = pd.read_csv(df2)
            df_geo = df_geo[df_geo.name.isin(df['Country'])]
            df_geo.reset_index(drop=True,inplace=True)
            for i in range(0,len(df_geo)):
                df['lat'][df.Country==df_geo['name'][i]] = df_geo['latitude'][i]
                df['lon'][df.Country==df_geo['name'][i]] = df_geo['longitude'][i]
        return df

