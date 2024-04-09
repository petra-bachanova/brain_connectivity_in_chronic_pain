import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import seaborn as sns
import glob

meta = pd.read_csv("Data/metadata.csv")

df = pd.DataFrame()
for link_density in [0.1, 0.2, 0.3, 0.4, 0.5]:
    file = glob.glob(f"Data/paingen as ref/HDI_res_paingen_{link_density}.csv")[0]
    per = pd.read_csv(file)
    per["link_density"] = link_density
    per = per.reset_index()
    df = pd.concat([df, per])


merged = pd.merge(df, meta, left_on="index", right_index=True)
merged = merged[merged['time'] == 1]

col = merged.pop('is_patient')
merged.insert(df.columns.get_loc("link_density")+1, "is_patient", col)
merged.to_csv("Data/240327_HDI_res_paingen_across_densities_w_meta.csv", index=False)

sns.violinplot(data=merged, x="link_density", y="betweenness_bin", hue="is_patient", split=True, gap=1, inner="quart")
sns.violinplot(data=merged, x="link_density", y="clustercoef_bin", hue="is_patient", split=True, gap=1, inner="quart")
sns.violinplot(data=merged, x="link_density", y="degree", hue="is_patient", split=True, gap=1, inner="quart")
sns.violinplot(data=merged, x="link_density", y="eigenvector_centrality_bin", hue="is_patient", split=True, gap=1, inner="quart")

sns.lmplot(data=merged[merged["is_patient"] == 1], y="clustercoef_bin", x="pain_avg")


