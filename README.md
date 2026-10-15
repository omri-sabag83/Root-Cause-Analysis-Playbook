# Root-Cause Analysis Playbook

A module-by-module reference for the named root-cause analysis (RCA)
techniques, each worked through on real numbers. Modules 1–10 are organised
by DMAIC (Define, Measure, Analyze, Improve, Control); Module 11 covers 8D
(Eight Disciplines), a competing approach; Module 12 turns the whole playbook
into a reusable AI-assistant Skill and tests whether it changes behaviour.

The program, progress table and per-module detail are in
[CURRICULUM.md](CURRICULUM.md).

| # | Notebook | Topic | Segment / phase |
|---|----------|-------|-----------------|
| 1 | `01_dmaic.ipynb` | DMAIC: the structure of a root-cause project | DMAIC spine |
| 2 | `02_pareto.ipynb` | Pareto analysis: choosing which problem gets a project | DMAIC: Define |
| 3 | `03_timeline.ipynb` | Timeline and events-and-causal-factors reconstruction | DMAIC: Measure |
| 4 | `04_is_is_not.ipynb` | Change analysis and Kepner-Tregoe "is / is-not" | DMAIC: Measure → Analyze |
| 5 | `05_five_whys.ipynb` | The 5 Whys: two chains, two causes | DMAIC: Analyze |
| 6 | `06_fishbone.ipynb` | Fishbone (Ishikawa): every candidate cause listed, tested and scored | DMAIC: Analyze |
| 7 | `07_cause_mapping.ipynb` | Apollo root cause analysis and cause mapping: every effect needs an action and a condition | DMAIC: Analyze |
| 8 | `08_fault_tree.ipynb` | Fault tree analysis: a tree's prediction checked against a run log exposes a hidden common cause | DMAIC: Analyze |
| 9 | `09_barrier_analysis.ipynb` | Barrier analysis: every defence in a real outage marked worked, failed or missing, and matched to the fix list | DMAIC: Improve |

Related repos: [A/B Testing Playbook](https://github.com/omri-sabag83/A-B-Testing-Playbook),
[Product Analytics Playbook](https://github.com/omri-sabag83/Product-Analytics-Playbook),
[Scikit-Learn Playbook](https://github.com/omri-sabag83/Scikit-Learn-Playbook).

## Data

Each module chooses its own data and says why:
- **Reused investigations** (Modules 1, 4, 6 and 11) re-run earlier
  take-home analyses from a private workspace. Their source files' licences
  do not clearly allow redistribution, so **they are not in this repo**. The
  notebooks keep their outputs, so every number can be read without them.
- **Public data** (NYC 311, published incident postmortems) is fetched or cited
  at its source.
- **Simulated data** is generated in code with a fixed seed and always
  labelled as simulated.

## Reproduce

```bash
conda activate base                 # tested env: Python 3.13.5, versions in requirements.txt
python data/get_data.py             # copies and checksum-verifies the reused source files
                                    # (needs the private workspace; set RCA_SOURCE_DIR)
python data/fetch_nyc311.py         # Module 7: fetches the NYC 311 counts once (public, no login)
jupyter nbconvert --to notebook --execute --inplace *.ipynb
```

## Process

A self-directed learning program: I set the objectives, scope and review
standard; an AI assistant served as curriculum designer and pair-programmer,
building each module for my review. Every module went through a structured
rigor checklist, a read-through by an AI reviewer instructed to read as an
analyst new to the topic, and an independent check of its headline result by a
verifier agent that saw only the claim and the data.
