import pandas as pd
import numpy as np

for metric in ['degree', 'betweenness_bin', 'clustercoef_bin', 'eigenvector_centrality_bin']:
    # metric = 'degree'
    di = {}
    for i in range(1, 6):
        # print(i)
        # i=1
        per = pd.read_csv(f"Data/HDIs with metadata/HDIat0{i}_w_meta_240910.csv")
        per = per[per['time']==1]

        hc = per[per['is_patient'] == 0][metric].values
        hc = list(hc)
        hc.extend([np.nan]*(121-len(hc)))

        lomo = per[(per['is_patient'] == 1) & (per['HiMo_subject'] == 0)][metric].values
        lomo = list(lomo)
        lomo.extend([np.nan]*(121-len(lomo)))

        himo = per[(per['is_patient'] == 1) & (per['HiMo_subject'] == 1)][metric].values
        himo = list(himo)
        himo.extend([np.nan]*(121-len(himo)))

        full_line = hc + lomo + himo
        di[f"{i*10}%"] = full_line
        formatted = pd.DataFrame.from_dict(di, orient='index')
        formatted.to_csv(f'Data/supp1 tables for prism/{metric}.csv')



