import pandas as pd

df = pd.read_csv('def_table.csv')
df.index.name='id'
#df.index =[int(n.split('_')[-1]) for n in df.index.values]

#df.index.name='peak_id'
bsf_cols = ['BSF_0{}'.format(n) for n in [3,4,5,6,7,8]]
pcf_cols = ['PCF_0{}'.format(n) for n in [2,3,4,5,6,7]]
other_cols = ['BSF_LR','PCF_LR','BSF_PValue','BSF_FDR',
'PCF_logCPM','PCF_PValue','PCF_FDR','closest_mygenome']

df=df.drop(bsf_cols+pcf_cols+other_cols,axis=1)
df.rename({'BSF_logCPM':'logCPM'},axis=1,inplace=True)
to_format = [m+n for n in ['_logFC'] 
                for m in ['BSF','PCF']]
to_format+=['mean_bsf_b',
'mean_bsf_g','mean_pcf_g','mean_pcf_b','logCPM']

for n in df.columns:
    if n in to_format:
        df[n]=df[n].round(3)
df.to_csv('selection.csv')
