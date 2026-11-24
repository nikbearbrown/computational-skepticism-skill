# Computational Skepticism

An agent skill for auditing supplied AI outputs, evaluation packets, datasets, dashboards, and recorded workflows. It turns broad assurances into claims a reviewer can check and keeps deployment decisions with a named human. The companion textbook is [Computational Skepticism for AI](https://github.com/nikbearbrown/computational-skepticism-for-ai).

## Start here

Give your agent [SKILL.md](SKILL.md) and the local paths to a copy of the material it may inspect. State the intended use, which checks it may perform, and who can accept residual risk. For example: “Audit this synthetic reporting packet against the supplied table. Use the Computational Skepticism skill. Return an evidence ledger and a staff-facing decision brief. Read-only; no external actions.”

- [Chapter-to-check crosswalk](book-crosswalk.md): two introductions and all 13 core chapters.
- [Human report template](report-template.md) and [machine-readable schema](audit.schema.json).
- [Synthetic reporting exercise](synthetic-case.md) and its [example audit](example-audit.json).

This first version is an instructions-and-templates package. It is not a standalone scanner, live penetration testing system, certification, or evidence that a particular deployment is safe.

See [related skill patterns](skill-references.md) for optional references behind the audit design.
