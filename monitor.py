import numpy as np
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

rng = np.random.default_rng(42)
reference = pd.DataFrame({"age": rng.normal(30, 5, 300), "salary": rng.normal(50000, 8000, 300)})
current   = pd.DataFrame({"age": rng.normal(38, 5, 300), "salary": rng.normal(50500, 8000, 300)})

report = Report([DataDriftPreset()])
result = report.run(current_data=current, reference_data=reference)
result.save_html("drift_report.html")
print("Evidently report saved: drift_report.html")