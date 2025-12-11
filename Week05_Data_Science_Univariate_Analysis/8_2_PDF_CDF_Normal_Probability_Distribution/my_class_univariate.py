import pandas as pd
import numpy as np
#---univariate Class----
class myunivariate():
    #QuanQual list split
    def df_cat_num_split(df):
        cat_cals=[cal for cal in df if df[cal].dtype==object]
        num_cals=[cal for cal in df if df[cal].dtype!=object]       
        return cat_cals, num_cals
        
    #--------------------------------------------------
    #create New Table for central Tendency & descriptive#create New Table for central Tendency & descriptive
    def UnivariateTable(df,num_cals):
        import pandas as pd
        import numpy as np
        descriptive=pd.DataFrame(index=["Mean","Median","Mode",
                                        "Min","Q1-25%","Q2-50%","Q3-75%","Max",
                                       "IQR","1.5-Rule","Lower-Bound","Upper-Bound",
                                       "Skew","Kurtosis",
                                       "Variance","Std"]
                                 ,columns=num_cals)
        for cal in num_cals:
            #print(cal)
            descriptive.loc["Mean", cal] = round(df[cal].mean(), 2)
            descriptive.loc["Median", cal] = df[cal].median()
            descriptive.loc["Mode", cal] = round(df[cal].mode()[0], 2)
            descriptive.loc["Min",cal]=df.describe().loc['min',cal]
            descriptive.loc["Q1-25%",cal]=df.describe().loc['25%',cal]
            descriptive.loc["Q2-50%",cal]=df.describe().loc['50%',cal]
            descriptive.loc["Q3-75%",cal]=df.describe().loc['75%',cal]
            descriptive.loc["Max",cal]=df.describe().loc['max',cal]
            descriptive.loc["IQR",cal]=descriptive.loc["Q3-75%",cal]-descriptive.loc["Q1-25%",cal]
            descriptive.loc["1.5-Rule",cal]=1.5*descriptive.loc["IQR",cal]
            descriptive.loc["Lower-Bound",cal]=descriptive.loc["Q1-25%",cal]-descriptive.loc["1.5-Rule",cal]
            descriptive.loc["Upper-Bound",cal]=descriptive.loc["Q3-75%",cal]+descriptive.loc["1.5-Rule",cal]
            descriptive.loc["Skew",cal]=round(descriptive[cal].skew(), 2)
            descriptive.loc["Kurtosis",cal]=round(descriptive[cal].kurtosis(), 2)
            descriptive.loc["Variance",cal]=round(descriptive[cal].var(), 2)
            descriptive.loc["Std",cal]=round(descriptive[cal].std(), 2)
        
        #return descriptive
        
        print("\n-------------- Outlier info --------------\n")
        lesser=[]
        greater=[]
        for cal in num_cals:
            if descriptive.loc["Min",cal]<descriptive.loc["Lower-Bound",cal]:
                lesser.append(cal)
                print(f"Lower outlier in :'{cal}' value :", descriptive.loc["Min",cal])
            if descriptive.loc["Max",cal]>descriptive.loc["Upper-Bound",cal]:
                greater.append(cal)
                print(f"Upper outlier in :'{cal}' value :", descriptive.loc["Max",cal])
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

    #---------------------------------------------------
    # Check each categorical (object) if uppercase exists
    def df_check_uppercase(df):
        print("\nuppercase present 'yes'/'no'\n-----------------------------")
        for col in df.select_dtypes(include="object").columns:
            has_upper = df[col].str.contains(r'[A-Z]').any()    
            print(f"{col}: {"uppercase present 'yes'" if has_upper else 'no'}")
        print("\ndataset = uppercase present 'yes'" if has_upper else '\ndataset = uppercase not present')
        
    #---------------------------------------------------
    # Check each categorical (object) column and convert all text values to lowercase
    def df_convert_lowercase(df):
        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].str.lower()
        return df

    #---------------------------------------------------
    #Detect missing values with order and %
    def df_missing_info(df):
        missing_info = df.isnull().sum().to_frame(name='Missing')
        missing_info['% Missing (null)'] = (missing_info['Missing'] / len(df) * 100).round(2)
        missing_info = missing_info[missing_info['Missing'] > 0].sort_values(by='Missing', ascending=False)
        print(missing_info)
        
    #---------------------------------------------------
    # looking at unique values in columns
    def df_uni_val_info(df):
        for col in df:
            print(f"{col} {df[col].unique()} unique values | Type :{df[col].dtype}\n")

    #---------------------------------------------------
    # Clean the data based unique values, replace incorrect values eg. '\t6200', '\t?', '\tno','\tyes' etc
    def df_clean_all(df):
        for col in df.columns:
            # convert everything to string
            df[col] = df[col].astype(str)
            # remove tabs
            df[col] = df[col].str.replace('\t', ' ', regex=False)
            # Step 3: remove newlines (\n newlines, \r carriage returns)
            df[col] = df[col].str.replace('\n', ' ', regex=False)
            df[col] = df[col].str.replace('\r', ' ', regex=False)
            # replace multiple spaces with a single space
            df[col] = df[col].str.replace(' +', ' ', regex=True)
            # strip leading and trailing spaces
            df[col] = df[col].str.strip()
            # replace empty or "nan" strings with real NaN
            df[col] = df[col].replace(['', ' ', 'nan', 'NaN', 'None'], np.nan)
            #Extra string remove
            df[col] = df[col].replace(['?'], np.nan)
            # try converting back to numeric if possible
            df[col] = pd.to_numeric(df[col], errors='ignore')
        
        return df

    #---------------------------------------------------
    #Impute missing values in a DataFrame.
    def df_simple_impute(df, strategy="mean"):
        """
        Impute missing values in a DataFrame.    
        Parameters:
            df (pd.DataFrame): Input DataFrame
            strategy (str): "mean", "median", "most_frequent", or "constant"   
        Returns:
            pd.DataFrame: DataFrame with imputed values
        """
        import pandas as pd
        from sklearn.impute import SimpleImputer
        imputer = SimpleImputer(strategy=strategy)
        imputed_array = imputer.fit_transform(df)
        return pd.DataFrame(imputed_array, columns=df.columns)

    #---------------------------------------------------
    # Handle missing values using the KNNImputer method
    def df_fill_missing_values_knn(df):
        import pandas as pd
        import numpy as np
        from sklearn.preprocessing import LabelEncoder
        from sklearn.impute import KNNImputer
        from sklearn.model_selection import train_test_split,cross_val_score
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
        
        # --- STEP 1: Identify categorical and numeric columns ----
        cat_cols = df.select_dtypes(include=['object']).columns
        num_cols = df.select_dtypes(exclude=['object']).columns
        #print("Categorical columns:\n", list(cat_cols))
        #print("Numeric columns:\n", list(num_cols))
        
        # --- STEP 2: Encode categorical columns ----------------
        encoders = {}
        for col in cat_cols:
            le = LabelEncoder()
            df[col] = df[col].astype(str)  # ensure string
            df[col] = df[col].replace("nan", np.nan)
            mask = df[col].notna()
            if mask.sum() > 0:
                df.loc[mask, col] = le.fit_transform(df.loc[mask, col])
                encoders[col] = le
        
        # --- STEP 3: Apply KNN Imputer for categorical and numeric columns----
        df = df.apply(pd.to_numeric, errors='coerce')
        imputer = KNNImputer(n_neighbors=5)
        df_imputed = imputer.fit_transform(df)
        df_imputed = pd.DataFrame(df_imputed, columns=df.columns)
        
        #Encoded and imputed dataset (dataset contain numeric value only) for any model creation
        df_imputed_encoded=df_imputed.copy()
        
        #--- STEP 4: Valiation with KNeighborsClassifier Model--------
        
        #traget columns for prediction
        # get the last column name as target
        target_col = df.columns[-1]  
        # X, y split
        X=df_imputed.drop(target_col, axis=1)
        y=df_imputed[target_col]
        
        #split train and test set 20% test data 80% train data
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=42)
        
        #model creation 
        model=KNeighborsClassifier(n_neighbors=5) #5
        model.fit(X_train,y_train)
        
        #y prediction for valitation
        y_pred = model.predict(X_test)
        
        # Valitation result
        print(f"\nImpute valiation: based on KNN model\nTrain Set:")
        print(f"Model accuracy: {model.score(X_train,y_train):.2f}")
        print(f"Test Set:")
        print(f"Accuracy: {accuracy_score(y_test, y_pred, average='macro'):.2f}")
        print(f"F1_score: {f1_score(y_test, y_pred):.2f}")
        print(f"ROC-AUC : {roc_auc_score(y_test, y_pred):.2f}")
        cv_scores = cross_val_score(model, X, y, cv=10)  # 10 cross-fold CV
        print("Model Cross-validation accuracy:", cv_scores.mean())
        
        # --- STEP 4: Decode categorical columns -------
        # Decode for data analysis
        for col in cat_cols:
            if col in encoders:
                df_imputed[col] = df_imputed[col].round().astype(int)
                df_imputed[col] = encoders[col].inverse_transform(df_imputed[col])
        
        # df_imputed_encoded = dataset after encoding all categorical and numerical columns
        # df_imputed = dataset after decoding categorical columns back to original labels
        return df_imputed, df_imputed_encoded
    #---------------------------------------------------
