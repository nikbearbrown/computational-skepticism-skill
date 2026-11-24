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
