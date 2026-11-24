# Book-to-audit crosswalk

The [textbook repository](https://github.com/nikbearbrown/computational-skepticism-for-ai) is the reading reference. The overview below is operational guidance, not an assertion that every book topic can be certified by an automated test.

| Reading | Audit question | Evidence or check |
|---|---|---|
| Intro A · Agents | Who can do what, and what was actually observed? | Separate intent, authority, attempt, receipt and external result in a supplied trace. |
| Intro B · Agentic Loops | Where does new evidence enter, and when must work stop? | Review recorded budgets, stopping conditions and handoff gates using benign offline fixtures. |
| 1 · Skeptic's Toolkit | What claim could change the decision? | State the claim, frame, counterexample and independent check before assigning confidence. |
| 2 · Probability and Uncertainty | Does the conclusion respect base rates and sample size? | Recompute proportions and distinguish a raw score from calibrated probability; show uncertainty. |
| 3 · Data Validation | Which population, period and cases are actually in the data? | Record provenance, collection rules, exclusions, missingness and denominator. |
| 4 · Robustness | Does the behavior hold under normal variation? | Compare results across prespecified benign input changes or supplied time slices; log failures and coverage. |
| 5 · Explainability | Does an explanation describe a verified mechanism or merely sound plausible? | Compare claimed drivers with independently supplied attribution, sensitivity or ablation evidence. |
| 6 · Bias | Where could an uneven outcome enter the workflow? | Map selection, measurement, labeling and use; distinguish observed differences from hypotheses. |
| 7 · Fairness Metrics | Which definition matches the real decision and affected groups? | Record the human-chosen comparison, numerators, denominators and small-cell protections; do not infer protected attributes. |
| 8 · Validating Agentic AI | Does a recorded success survive independent checks? | Match each step to approved inputs, expected state and observed output; review recorded failure/recovery. |
| 9 · Delegation and Trust | Is authorization explicit and review possible? | Identify permitted actions, accountable supervisor and approval boundaries. |
| 10 · Visualization | Does the chart or caption faithfully encode the underlying data? | Check axes, scales, baselines, unit, aggregation, dates and what suppression means. |
| 11 · Communicating Uncertainty | Is wording stronger than the evidence? | Tie confidence language and scope to the finding; distinguish absence from zero. |
| 12 · Accountability | Who handles a missed failure or resulting harm? | Record named sign-off, correction route, follow-up date, stop/rollback owner and evidence retention. |
| 13 · Limits of AI | What remains outside the system's evidence or jurisdiction? | Explicitly mark unsupported or out-of-scope claims, preserve limitations, and request human judgment. |
