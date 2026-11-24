# Related skill patterns

These are optional references, not dependencies or endorsements. The core workflow is original, runs against supplied evidence, and does not need any third-party skill installed. Read and review licenses before reusing text or code.

| Reference | Pattern worth adopting | Boundary |
| --- | --- | --- |
| [STEM Project Review](https://github.com/nikbearbrown/stem-project-review) | Evidence references, severity, and findings usable by both a human and another agent. | This skill audits the evidence for AI claims and decisions. It does not assign an overall project score. |
| Bear Brown catalog: `verification-before-completion`, `systematic-debugging`, `peer-review` | Check actual outcomes before claiming completion; isolate changes; make reviewers cite evidence. | A second model alone is not verification. Keep the authority to approve with the designated reviewer. |
| OpenDataHub [agent-eval-harness](https://github.com/opendatahub-io/agent-eval-harness), `eval-review` and `eval-dataset` | Review each test case and its trace before accepting an aggregate score; version synthetic cases and answer keys. | Do not import sensitive production traces. A judge score is a signal, not the ground truth. |
| [DeepEval](https://github.com/confident-ai/deepeval) | An optional evaluation runner for already-defined checks. | Calibrate against independent examples and human decisions before using model-based scores. |
| [PyPICT](https://github.com/omkamal/pypict-claude-skill) | Plan pairwise coverage of conditions such as input completeness, version, and output format. | Add meaningful edge cases, high-risk combinations, and subgroup checks explicitly. Pairwise coverage is not equity evidence. |

No fetched skill instructions are executed by this package. No external tools are required for the synthetic exercise.

## Data validation extensions

The Bear Brown inventory pointed to these additional source patterns. The checks below are adapted as review questions, with no copied implementation or required service.

| Source and pinned Git blob | Checks to carry into a supplied-project audit |
| --- | --- |
| [DataHub Skills](https://github.com/datahub-project/datahub-skills), `datahub-quality` `583a7cac03555f96fe185583a22403bb13902e7c`; `datahub-lineage` `6541e6deb46d3c1898e7088d2771a8b07e121d1f` | Ask for approved freshness windows and expected volume by relevant segment; inspect historical schema/nullability assertion results. Link a consequential output field to its source column and transformation, and record where upstream/downstream lineage is unknown. |
| [Data Agent Kit Starter Pack](https://github.com/gemini-cli-extensions/data-agent-kit-starter-pack), `data-autocleaning` `a3182b47d78413cd62da47d23d9baee0bbe7db6e`; `dbt-bigquery` `2afb361687549f783884d67ab7fa7370e98ae395` | Compare pre/post row counts, null rates and distinct keys. Explain new nulls where input was non-null; compare supplied synthetic inputs and expected outputs for transformations. |
| [SynthData](https://github.com/rappdw/synthdata), `synthdata-generate` `0e38e1aac7a93b1341307c9f0290c4d78d211ea0` | Use invented, schema-fixed fixtures with reproducible seeds and explicit row/key expectations. Passing an invented fixture is not evidence of empirical representativeness or privacy guarantees. |
