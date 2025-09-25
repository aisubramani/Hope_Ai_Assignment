import pandas as pd
import numpy as np
#---univariate Class----
class myunivariate():
    #QuanQual list split
    def QuanQual(df):
        quan=[x for x in df if df[x].dtype!=object]
        qual=[x for x in df if df[x].dtype==object]
        return quan,qual
    #--------------------------------------------------
    #create New Table for central Tendency & descriptive
    def UnivariateTable(df,quan):
        import pandas as pd
        import numpy as np
        descriptive=pd.DataFrame(index=["Mean","Median","Mode",
                                        "Min","Q1-25%","Q2-50%","Q3-75%","Max",
                                       "IQR","1.5-Rule","Lower-Bound","Upper-Bound"]
                                 ,columns=quan)
        for x in quan:
            #print(x)
            descriptive.loc["Mean", x] = round(df[x].mean(), 2)
            descriptive.loc["Median", x] = df[x].median()
            descriptive.loc["Mode", x] = round(df[x].mode()[0], 2)
            descriptive.loc["Min",x]=df.describe().loc['min',x]
            descriptive.loc["Q1-25%",x]=df.describe().loc['25%',x]
            descriptive.loc["Q2-50%",x]=df.describe().loc['50%',x]
            descriptive.loc["Q3-75%",x]=df.describe().loc['75%',x]
            descriptive.loc["Max",x]=df.describe().loc['max',x]
            descriptive.loc["IQR",x]=descriptive.loc["Q3-75%",x]-descriptive.loc["Q1-25%",x]
            descriptive.loc["1.5-Rule",x]=1.5*descriptive.loc["IQR",x]
            descriptive.loc["Lower-Bound",x]=descriptive.loc["Q1-25%",x]-descriptive.loc["1.5-Rule",x]
            descriptive.loc["Upper-Bound",x]=descriptive.loc["Q3-75%",x]+descriptive.loc["1.5-Rule",x]
        
        #return descriptive
        print("\n-------------- Outlier info --------------\n")
        lesser=[]
        greater=[]
        for x in quan:
            if descriptive.loc["Min",x]<descriptive.loc["Lower-Bound",x]:
                lesser.append(x)
                print(f"Lower outlier in :'{x}' value :", descriptive.loc["Min",x])
            if descriptive.loc["Max",x]>descriptive.loc["Upper-Bound",x]:
                greater.append(x)
                print(f"Upper outlier in :'{x}' value :", descriptive.loc["Max",x])
        print("Lesser outlier :",lesser,"\nGreater outlier:",greater)
        print("\n-------------- Univariate Table  --------------\n")
        return descriptive 
    #---------------------------------------------------
    # Function to replace outliers using np.percentile
    def replace_outliers(df):
        print("\n-------------- Outliers Replaced info --------------\n")
        for col in df.select_dtypes(exclude="object").columns:
            # Q1 (25th percentile) and Q3 (75th percentile)
            #dropna() removes missing values (NaN) before calculating, 
            #Q1 = df[col].quantile(0.25) # other way in panda calculate Q1, Q2
            #Q3 = df[col].quantile(0.75)
            Q1 = np.percentile(df[col].dropna(), 25)
            Q3 = np.percentile(df[col].dropna(), 75)
            IQR = Q3 - Q1
    
            # Bounds
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
    
            # Replace lower outliers with lower bound
            df.loc[df[col] < lower_bound, col] = lower_bound
            
            # Replace higher outliers with upper bound
            df.loc[df[col] > upper_bound, col] = upper_bound
            print(f"{col}: Outliers replaced → lower < {lower_bound:.2f}, upper > {upper_bound:.2f}")
        
        return df
    #---------------------------------------------------
    #create Function for freqtable
    def FreqTable(df,column_name):
        print(f"\n---- Frequency Table for '{column_name}'------\n")
        freqtable = df[column_name].value_counts().reset_index()
        # Rename columns
        freqtable.columns = ["Unique_Values", "Frequency"]
        # Calculate relative frequency
        freqtable["Relative_Frequency"] = freqtable["Frequency"] / freqtable["Frequency"].sum()
        # Cumulative relative frequency
        freqtable["Cumulative_Rel_Freq"] = freqtable["Relative_Frequency"].cumsum()
        # Optional: sort by Frequency
        #freqtable = freqtable.sort_values(by="Frequency").reset_index(drop=True)
        return freqtable 
    