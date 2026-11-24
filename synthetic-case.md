# Worked case: audit an AI-drafted operations caption

All figures are invented. The case is administrative and does not involve clinical or patient data. The artifact under review is a proposed internal caption, not an operational system.

| Fictional center | Requests resolved on time | Eligible requests | Period |
|---|---:|---:|---|
| Harbor | 24 | 30 | October |
| Hill | Suppressed | Suppressed | October |

**AI caption v1:** “Harbor resolved 24% on time. Hill received zero eligible requests. Harbor’s operational log supports the October period.”

1. Recalculate Harbor from the table: 24/30 = 80%. The caption confuses a count and a percentage.
2. Hill's denominator is unknown from the packet. Suppression cannot be coded as zero; an assertion about the actual value is unresolved.
3. The table labels the period October, but it does not establish what a separate operational log says. The log claim is unresolved unless that approved artifact is supplied.

**Recommended disposition:** hold the caption, retain the original, correct Harbor to “24 of 30 eligible requests (80%) in the supplied October table,” and remove any implication that the suppressed count is zero or that an operational log was checked. Do not infer why, or whether, the apparent result differs across centers. A staff reviewer should independently verify the corrected wording before release. See [example audit](example-audit.json).
