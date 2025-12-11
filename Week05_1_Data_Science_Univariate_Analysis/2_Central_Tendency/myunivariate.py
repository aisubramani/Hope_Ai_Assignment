#univariate Class
class myunivariate():
    
    #QuanQual list split
    def QuanQual(dataset):
        quan=[x for x in dataset if dataset[x].dtype!=object]
        qual=[x for x in dataset if dataset[x].dtype==object]
        return quan,qual
