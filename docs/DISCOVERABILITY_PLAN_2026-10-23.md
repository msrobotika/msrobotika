# Discoverability & Community Plan · 23 October 2026

**Owner:** MS ROBOTIKA · **Purpose:** attract relevant developers and users to verifiable open-source work, without artificial stars or misleading claims.

## Verified baseline (snapshot, 2026-10-23)

A review of the 20 public repositories visible to the linked account found:
- 20 public repositories, 14 total repository stars and 0 forks at the snapshot (stars are not unique people);
- no GitHub Topics configured on those 20 repositories;
- no Homepage field configured on those 20 repositories;
- AB-BI Studio v0.4 and AB-Modbus Studio v0.1 provide downloadable GitHub Releases;
- some browser-first projects offer a downloadable single-file HTML edition;
- AB-GEN has no general open-source LICENSE yet: **do not describe it as redistributable under MIT/Apache/GPL without a deliberate licensing decision**;
- **AB-SCADA Studio was created on 2026-10-23 and is actively being developed**: it is not part of the release-ready shortlist and its early state is not a negative quality finding;
- many industrial repos were published on 2026-10-21 or 2026-10-22: a small audience after 1–2 days does not demonstrate failure.

This is a repository metadata and documentation audit, **not verified visitor traffic**. GitHub Traffic (views, unique visitors, clone counts and referrers) requires owner access in Insights → Traffic and is not inferred from stars.

## Priority 1: make projects findable

GitHub repository **About → Topics** should be populated manually by a maintainer with accurate, discoverable tags. Suggested *starting* tags (do not claim functionality beyond the source code):

| Repository | Suggested GitHub Topics |
|---|---|
| AB-PLC-Simulator | `plc`, `plc-simulator`, `industrial-automation`, `javascript`, `ladder-logic`, `simulation` |
| AB-GRAFCET-Studio-v0.1-c | `grafcet`, `sfc`, `industrial-automation`, `plc`, `javascript` |
| AB-KOP-Studio-v0.1 | `ladder-logic`, `plc`, `industrial-automation`, `simulator`, `javascript` |
| AB-SCL-Studio | `structured-text`, `ladder-logic`, `plc`, `javascript` |
| AB-Modbus-Studio | `modbus`, `modbus-tcp`, `industrial-automation`, `python`, `scada` |
| AB-Serial-Analyzer-v0.1- | `serial`, `modbus-rtu`, `rs485`, `python`, `industrial-automation` |
| -AB-Vision-Inspector | `computer-vision`, `image-processing`, `quality-control`, `metrology`, `javascript` |
| AB-BI-Studio | `business-intelligence`, `data-visualization`, `dashboard`, `python`, `open-source` |
| AB-Suite-Core-arquitectura-de-integraci-n | `industrial-automation`, `javascript`, `event-bus`, `sdk` |
| AB-GEN-Green-AI | `computer-vision`, `machine-learning`, `reproducibility`, `research` |

Do not tag AB-SCADA as a completed SCADA product before publication of an actual working release. Update topics as scope changes.

For each mature project, set About → **Website** only to a **confirmed working demo/documentation page**, not to a speculative GitHub Pages URL. A README link saying “when GitHub Pages is enabled” does **not** establish that a live demo is available.

## Priority 2: reduce the barrier to first use

For the three initial showcase candidates (AB-PLC Simulator, AB-BI Studio, AB-Modbus Studio), maintain:
1. one-line purpose at the top in Spanish **and English**;
2. one authentic screenshot above the fold, never a conceptual mockup sold as a run;
3. a precise 60-second **Quick Start** with prerequisites and a test dataset;
4. a **Releases** link when a real downloadable release exists; never advertise a release that does not exist;
5. build/CI status and exact verification scope; link to test commands;
6. a clear **Known limitations** section (no hardware safety assurance, no certified PLC compatibility).

For HTML-first projects, link to the **downloadable** portable HTML and explain that GitHub's blob page is not an interactive running demo. Publish a versioned release when validated and ready.

## Priority 3: community launch in two languages

Publish **one evidence-driven post per week** for 4 weeks, not 20 simultaneous promotional posts:

- **Week 1:** AB-PLC Simulator — 20–40 s screencast of a virtual conveyor and simulated fault; explain what is simulated and what is not. Audience: r/PLC and relevant professional automation communities *only when their rules allow self-promotion*, PLC/automation LinkedIn groups, dev forums.
- **Week 2:** AB-Modbus Studio — GIF or short video of read-only registers and local Modbus test server. Include protocol limitations and a test command.
- **Week 3:** AB-BI Studio — real dashboard screenshot and 1-minute CSV → dashboard walkthrough. Do not call it feature-compatible with Power BI.
- **Week 4:** AB-Vision Inspector — documented synthetic defect detection / camera auditing, with metrology limitations and a comparison to manual inspection workflow (no certification claim).

Every publication should show **problem → evidence → quick start → GitHub URL → specific request for feedback**, not “please star everything”. Use Spanish and English versions where useful. Respect community posting rules; no automated bulk messages, purchased followers or reciprocal-star schemes.

## Priority 4: improve contribution and credibility

- Create 3 starter issues per flagship project: one bug reproducibility issue, one documentation/translation issue, one self-contained feature test; label genuinely easy ones `good first issue` only when well-scoped.
- Use honest releases, changelog, versioned source archives, SHA-256 where relevant.
- Link to real demos or record GIFs from actual execution; distinguish simulated data from field data.
- For AB-GEN, complete audit/licensing decisions before scientific publicity; evidence categories **REPORTED / RECOVERED / RECONSTRUCTED / REPRODUCED / VALIDATED** must remain explicit.
- For industrial software, invite documented test reports from real devices but never suggest using simulators to control live machine safety functions.

## Measurement plan (4 weeks)

Set a baseline **per repository**, weekly on the same day:
- GitHub Insights → Traffic: views, unique visitors, clones, unique cloners, referrers (screenshots/export manually);
- stars and forks per repo (public API); issues opened by outsiders, non-owner pull requests;
- release downloads where GitHub assets exist;
- landing-page/demo click data only if instrumentation is privacy-conscious and disclosed.

Review how many **unique visitors start a meaningful action** (download, issue, question or clone) rather than optimizing stars alone.

## Week 1 acceptance criteria

- Profile README includes short bilingual landing section and links to runnable entry points;
- at least the initial flagship topics have been applied by an admin;
- release/demo status is accurate for all featured projects;
- at least one genuine demo video is available;
- first weekly traffic baseline is recorded.

**Scope of this PR:** GitHub profile documentation only. Topics, website metadata, GitHub Pages configuration, screenshots and outreach are **not changed by this PR**. No social posting is performed automatically.
