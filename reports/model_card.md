# Model Card — Healthcare Readmission Risk Prediction

## Model Details
- Task: Binary classification (risk of readmission within 30 days)
- Model: Logistic Regression (class_weight=balanced)
- Preprocessing: Median imputation + scaling (numeric), Most-frequent + one-hot (categorical)
- Dataset: Diabetes 130-US hospitals (public dataset)

## Intended Use
- Decision-support / triage insights (NOT for fully automated clinical decisions)

## Metrics (Test Set)
- Add: ROC-AUC, PR-AUC from `reports/performance_report.md`

## Fairness Evaluation
Sensitive attributes evaluated:
- Gender
- Age group
- Race

Metrics reported:
- Selection rate
- True Positive Rate (TPR)
See: `reports/fairness_report.md`

## Limitations
- Data is historical + may contain sampling bias
- Target label is based on recorded “readmitted”
- Missing values exist in multiple columns

## Ethical Considerations
- Risk of disparate impact across groups
- Must be monitored before real-world use

## Monitoring (Future Work)
- Data drift detection
- Periodic recalibration
- More fairness constraints/mitigation
