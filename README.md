# Computational Skepticism

An agent skill for auditing supplied AI outputs, evaluation packets, datasets, dashboards, and recorded workflows. It turns broad assurances into claims a reviewer can check and keeps deployment decisions with a named human. The companion textbook is [Computational Skepticism for AI](https://github.com/nikbearbrown/computational-skepticism-for-ai).

## Start here

Give your agent [SKILL.md](SKILL.md) and the local paths to a copy of the material it may inspect. State the intended use, which checks it may perform, and who can accept residual risk. For example: “Audit this synthetic reporting packet against the supplied table. Use the Computational Skepticism skill. Return an evidence ledger and a staff-facing decision brief. Read-only; no external actions.”

- [Chapter-to-check crosswalk](book-crosswalk.md): two introductions and all 13 core chapters.
- [Human report template](report-template.md) and [machine-readable schema](audit.schema.json).
- [Synthetic reporting exercise](synthetic-case.md) and its [example audit](example-audit.json).

This first version is an instructions-and-templates package. It is not a standalone scanner, live penetration testing system, certification, or evidence that a particular deployment is safe.

See [related skill patterns](skill-references.md) for optional references behind the audit design.

## Audit a project rather than a single output

Point the skill at an authorized plan, code file, dataset summary, project directory, or GitHub repository and revision. For a local directory, the optional Python 3.10+ POSIX inventory helps start:

```sh
python3 intake.py /canonical/path/to/project --max-entries 500 --max-bytes 262144
```

This lists candidate paths and metadata only. It never reads file content, runs target code, follows symlinks, or uses the network. It omits common generated/dependency directories, sensitive-looking names, binary extensions, and large files. Names themselves may be sensitive, so keep inventory output with the authorized reviewer. The cap includes excluded names and discovery, so a bounded result is not a complete inventory. For macOS aliases such as `/tmp`, pass a canonical path obtained from the trusted target directory with `pwd -P`. For GitHub, use authorized read-only tool access to inspect the pinned revision, or supply an already available local snapshot.

The audit itself is performed by the agent following SKILL.md. It produces human feedback and an evidence ledger with next steps. The inventory does not score the project or certify it.
