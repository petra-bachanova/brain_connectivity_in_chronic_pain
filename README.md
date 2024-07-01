# README

## Code Execution Order

Follow the steps below to run the code in the correct order:

1. **metadata_prep.mlx**
   - **Description**: This script takes in a brainpathway object and adds the correct metadata to the metadata field.
   - **Output**: A new brainpathway object with corrected metadata.

2. **calculate_graph_props_and_HDI_paingen_ref.mlx**
   - **Description**: This script takes in brainpathway objects with trial and reference subjects. It calculates the graph properties and the HDI of those properties.
   - **Output**: `bs_with_calculated_graph_metrics_and_HDIs_{date}.mat` for the trial subjects.

3. **LMMs_HDI.mlx and LMMs_HDI_separate_models.mlx**
   - **Description**: These scripts run linear mixed models (LMMs). Initially, the focus is on mean-centering variables within HC and CBP groups to observe the true group effect. After identifying potential effects of sleep, disability, and age, separate models for HC and LM CBP groups are run to confirm the effects of these variables.

4. **make_table_for_LMM_heatmap*.mlx**
   - **Description**: This script takes the results (t-values) of multiple LMMs and reformats them for plotting a tidy heatmap in GraphPad Prism.
