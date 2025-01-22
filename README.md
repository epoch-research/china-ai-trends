# Trends in AI models from China vs. elsewhere

Code for the data insight ["Chinese language models have scaled up more slowly than their global counterparts."](https://epoch.ai/data/notable-ai-models#china-compute-trends)

You can install required packages using

```
pip install -r requirements.txt
```

Results can be reproduced by running `compute_analysis.ipynb`.

The notebook specifies a `results_dir` where results will be saved.
The notebook also has a set of parameters near the top.
These parameters can be modified for sensitivity analysis.
See the description of each parameter in the notebook for details.

The raw data used for analysis is in the `data/` folder.
`All ML Systems - full view.csv` is a snapshot of the Epoch AI database of models.
