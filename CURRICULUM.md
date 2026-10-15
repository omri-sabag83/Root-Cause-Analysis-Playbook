# Root-Cause Analysis Playbook — Learning Program

**Goal:** a working command of the named root-cause analysis (RCA) techniques,
so that an investigation can be described as "I used technique X, because the
problem looked like Y" rather than "I just investigated it". Every technique is
worked through on real numbers.

**Starting point:** a Product Analyst background (B2C marketplace, B2B
security). Several earlier investigations were already root-cause work in all
but name: a one-step funnel drop, an activation cliff on a calendar date, and a
mid-year category relabeling in public service-request data. This playbook
names the techniques those investigations used without naming them, and adds
the ones they did not use.

**Scope boundary:** this is about finding and preventing the causes of
problems that have already happened (or could happen) in a process. Designing
experiments to prove a cause is covered in the
[A/B Testing Playbook](https://github.com/omri-sabag83/A-B-Testing-Playbook);
diagnosing a metric movement with a fixed checklist is covered in Module 10 of the
[Product Analytics Playbook](https://github.com/omri-sabag83/Product-Analytics-Playbook).
Both are referenced here and not repeated.

---

## Progress

`🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜` **67% complete (8/12 modules)**

⬜ Not started · 🟨 In progress · 🟩 Completed

| # | Module | Segment / DMAIC phase | Status | Completed On |
|---|--------|-----------------------|--------|---------------|
| 1 | DMAIC: the Structure of a Root-Cause Project | DMAIC spine | 🟩 Completed | 2026-10-12 |
| 2 | Pareto Analysis | DMAIC: Define | 🟩 Completed | 2026-10-13 |
| 3 | Timeline & Events-and-Causal-Factors Reconstruction | DMAIC: Measure | 🟩 Completed | 2026-10-13 |
| 4 | Change Analysis & Kepner-Tregoe "Is / Is-Not" | DMAIC: Measure → Analyze | 🟩 Completed | 2026-10-13 |
| 5 | The 5 Whys | DMAIC: Analyze | 🟩 Completed | 2026-10-14 |
| 6 | Fishbone (Ishikawa) Diagram | DMAIC: Analyze | 🟩 Completed | 2026-10-14 |
| 7 | Apollo Root Cause Analysis & Cause Mapping | DMAIC: Analyze | 🟩 Completed | 2026-10-14 |
| 8 | Fault Tree Analysis | DMAIC: Analyze | 🟩 Completed | 2026-10-15 |
| 9 | Barrier Analysis | DMAIC: Improve | ⬜ Not started | |
| 10 | FMEA (Failure Mode and Effects Analysis) | DMAIC: Control | ⬜ Not started | |
| 11 | 8D (Eight Disciplines) | Competing approach | ⬜ Not started | |
| 12 | Capstone: the `investigator` Skill and its test | Capstone | ⬜ Not started | |

---

## How this program works

**Three segments.**
- **Segment 1, the DMAIC spine (Modules 1–10).** DMAIC (Define, Measure,
  Analyze, Improve, Control) is a five-phase structure for a root-cause project.
  Module 1 teaches it in full. Modules 2–10 each teach one technique and place
  it inside the DMAIC phase where it naturally does its work, without
  re-explaining DMAIC.
- **Segment 2, 8D (Module 11).** A different, complete, competing approach,
  taught on its own and compared against DMAIC. It is not blended into
  Segment 1.
- **Capstone (Module 12).** An AI-assistant Skill (an instruction file that an AI
  assistant loads on demand) that chooses or follows these techniques, plus a
  test of whether it changes the assistant's behaviour.

**Why this phase order for the techniques.**
- **Define:** Pareto analysis chooses *which* problem deserves a project.
- **Measure:** timeline reconstruction fixes the facts and their order;
  "is / is-not" fixes the problem's exact boundary. Change analysis then asks
  what changed at that boundary, which is the bridge into Analyze.
- **Analyze:** the four cause-finding techniques run from simplest to most
  formal. The 5 Whys is a single chain. The fishbone adds breadth. Cause
  mapping turns the chain into a graph of causes that act together. Fault tree
  analysis adds formal AND/OR logic and probabilities.
- **Improve:** barrier analysis asks which defences failed or were missing, so
  it points directly at what to build.
- **Control:** FMEA ranks every way the fixed process could still fail, and
  becomes the control plan that keeps the fix in place.

**Data: chosen per module.** No single dataset runs through the whole
program, because different techniques suit different kinds of incidents.
- **Reuse:** an earlier real investigation, framed as "here is where this was
  already done, unnamed". Those source files come from a private workspace and
  are not in this repo (see the README). The notebooks keep their outputs.
- **Fresh:** a new incident, either a published public postmortem or simulated
  data with a known, planted cause.

Each module states its choice and the reason in one line.

**Standards applied in every notebook:**
- Findings are tagged **Observation** (what the data shows), **Hypothesis**
  (a proposed explanation, not yet tested) or **Conclusion** (what the
  evidence supports).
- Mechanism vs. real-world cause is stated explicitly. "The rate fell because
  the traffic mix moved" is a mechanism; "because someone edited the campaign"
  would be a cause.
- Data-quality issues come first, not last.
- Every printed number gets a plain-English sentence.
- Every chosen number (a threshold, a window) is labelled as chosen, with the
  reason.
- Simulated data is always labelled as simulated.

---

## <u>Module 1 — DMAIC: the Structure of a Root-Cause Project</u>

**Concepts**
- What DMAIC is: the five-phase project structure at the core of Six Sigma (a
  quality-improvement method started at Motorola in 1986). DMAIC is for
  *improving an existing process*; its sister DMADV (Define, Measure, Analyze,
  Design, Verify) is for designing a new one.
- **Define:** the problem statement (what, where, when, how big; never *why*,
  never the fix), the scope (in / out), the goal, and SIPOC (Suppliers,
  Inputs, Process, Outputs, Customers), a one-line map of the process.
- **Measure:** operational definitions (exactly how each number is counted),
  checking the measurement itself before trusting it, and a baseline with its
  normal variation.
- **Statistical process control:** a p-chart (a control chart for a
  proportion) separates normal day-to-day variation from a real signal. It
  sets control limits at 3 standard errors around the baseline rate.
- **Analyze:** locate the problem, list candidate causes, verify each with
  data; separate the **mechanism** (how the number moved) from the **root
  cause** (why, in the real world).
- **Improve:** choose and test a fix, and check the improvement in the same
  measure that defined the problem.
- **Control:** the control plan (what is monitored, by whom, with which limit,
  and what to do when it fires), so the problem cannot silently return.
- **Tollgates:** the review at the end of each phase, with a fixed list of
  deliverables, before the next phase starts.
- When DMAIC fits (an existing, measurable process with an unknown cause) and
  when it does not (an emergency that needs containment today; a cause that is
  already known).

**Why it matters**
Most investigations fail by skipping phases: jumping from "the number dropped"
straight to a favourite cause (no Measure), or stopping at the explanation and
never building the monitor that would catch the next one (no Control). DMAIC
is a checklist of the phases a complete investigation needs. Every later
module places its technique inside one of these phases.

**Worked example**
The E01 funnel drop (a take-home exercise with artificial data, 8,766 starters,
15–20 Oct 2021), re-run phase by phase:
- **Define:** the bottom line, the share of starters who became closed-won
  deals, fell from 0.087 to 0.058 on 18–19 Oct. The statement names no step.
- **Measure:** the funnel computed from the raw rows matches the file's own
  summary sheet, and a p-chart puts both incident days outside the control
  limits.
- **Analyze:** the drop starts mostly at the first step (onboarding to lead
  form) and sits in one campaign's mobile traffic, and a rate-vs-mix
  split (did each segment convert worse, or did the segments' shares of
  traffic change?) shows it is a traffic-mix shift, not a conversion failure.
- **Improve:** recovery on 20 Oct is checked in the Define measure.
- **Control:** the original investigation never built one. A traffic-share
  monitor is built and back-tested here, and it would have fired on the first
  incident day.

A tollgate scorecard then shows which DMAIC deliverables the original
investigation produced and which it skipped.

**Resources**
- [Six Sigma](https://en.wikipedia.org/wiki/Six_Sigma) (Wikipedia, ~15 min,
  verified): origin at Motorola (1986) and GE (1995), and the DMAIC and DMADV
  project methods.
- [Proportions Control Charts (p-charts)](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc332.htm)
  (NIST/SEMATECH e-Handbook of Statistical Methods, ~10 min, verified): the
  p-chart control-limit formula used in the Measure and Control phases.

**Exercise type:** sort the original investigation's statements into DMAIC
phases; decide with a p-chart whether a second, smaller dip is a signal or
noise. Fully worked.

**Interview angle:** "Walk me through how you would investigate a sudden drop
in conversion." / "How would you make sure it doesn't happen again?"

---

## <u>Module 2 — Pareto Analysis</u>

**DMAIC phase:** Define (choosing which problem deserves a project).

**Concepts**
- The Pareto chart: categories sorted from largest to smallest, bars plus a
  cumulative-share line, and the "vital few" categories that carry most of
  the effect
- The Pareto principle (the "80/20 rule") as a rule of thumb to check, not a
  law
- Counting the right thing: a Pareto by number of incidents and a Pareto by
  impact (time lost by users) can rank the same causes very differently
- One huge incident can put a category on top of an impact Pareto; check the
  largest single incident before choosing
- Second-level (nested) Pareto: drilling into the top bar
- Before-and-after Pareto: checking a fix by re-running the chart

**Why it matters**
A team can only run a few root-cause projects at once. Pareto analysis picks
the one where a fix removes the most pain, and it is the usual first chart in
a DMAIC Define phase.

**Worked example**
Fresh, simulated: one year of incidents on a company's data platform (649
incidents), with cause, minutes to resolve and users affected. It is
simulated because the lesson needs a known case where the count ranking and
the impact ranking disagree. Jan–Jun is used to choose a project, Jul–Dec to
check the fix:
- By count, late upstream files are the top cause (39.8% of incidents).
- By impact, upstream schema changes are (71.8% of user-hours lost, from
  8.2% of incidents).
- A nested Pareto inside schema changes points at renamed columns. After a
  fix from 1 Jul, renamed-column incidents fall from 12 to 2, though the
  untargeted kinds fall too.
- The Jul–Dec impact Pareto has a new top category, mostly one incident,
  though that kind of incident happened in both halves.

Sidenote: the E02 margin investigation (an earlier exercise), which used a
loss Pareto without naming it.

**Resources**
- [Pareto chart](https://en.wikipedia.org/wiki/Pareto_chart) (Wikipedia,
  ~5 min, verified): the chart, its cumulative line, and its place among the
  seven basic tools of quality.
- [Pareto principle](https://en.wikipedia.org/wiki/Pareto_principle)
  (Wikipedia, ~10 min, verified): origin (Vilfredo Pareto, 1906), Joseph
  Juran's "vital few", and why 80/20 is a rule of thumb, not a law.

**Exercise type:** pick the project when the goal changes from user pain to
on-call workload. Fully worked.

**Interview angle:** "You have 400 open bugs and capacity to fix 20. Which
ones?"
---

## <u>Module 3 — Timeline & Events-and-Causal-Factors Reconstruction</u>

**DMAIC phase:** Measure (establishing the facts and their order before
asking why).

**Concepts**
- The timeline as the first fact base of an incident: every event with its
  time, its source, and how sure we are of it (stated, derived, recalled, or
  no time)
- The key durations: time to detect, time to diagnose, time to mitigate,
  time to recover fully
- Events-and-causal-factors (E&CF) charting: the chain of events in time
  order, the conditions that made each event possible, and the causal
  factors: the events or conditions without which the outcome would not have
  happened, or would have been much smaller
- Conditions often predate the incident window by weeks; a timeline that
  starts at the first alert misses them
- Ordering pitfalls: the order a report tells events in is not the order
  they happened; "after" is not "because"; an "event" can be a phase, not a
  single moment

**Why it matters**
Arguments about causes often turn out to be arguments about order. A timeline
built from timestamped evidence settles the order, and the durations show
where the time was really lost, before anyone argues about causes.

**Worked example**
Fresh and real: Cloudflare's published postmortem of its 2 July 2019 global
outage (a firewall rule with a runaway regular expression took down most of
its traffic for 27 minutes). Chosen because it publishes exact timestamps and
an honest list of contributing conditions:
- The timeline is rebuilt from the post's own timestamps, and it reproduces
  the post's 27 minutes (13:42 deploy to 14:09 recovery).
- The four standard durations show where the time went: 3 minutes to
  detect, 15 to diagnose, 9 to mitigate, 70 to recover fully.
- The E&CF chart links each event to the conditions behind it, including a
  CPU protection removed weeks before the incident.

Sidenote: the E12 NYC 311 investigation (an earlier exercise) dated a label
change to 29 July, but an independent check found it was phased from 1 June: an event
that was really a phase.

**Resources**
- [Details of the Cloudflare outage on July 2, 2019](https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/)
  (Cloudflare Blog, 2019, ~25 min, verified): the source of this module's
  worked example.
- [DOE-STD-1197-2024, Causal Analysis](https://www.energy.gov/documents/doe-std-1197-2024-finalpdf)
  (U.S. Department of Energy, 2024, PDF, ~15 min for the E&CF charting
  section, verified): how E&CF charts show the conditions and events needed
  for an incident.

**Exercise type:** mark how sure each number in the postmortem is (stated,
derived, recalled, or no time). Fully worked.

**Interview angle:** "Tell me about an incident you investigated: what
happened, in what order?"
---

## <u>Module 4 — Change Analysis & Kepner-Tregoe "Is / Is-Not"</u>

**DMAIC phase:** Measure into Analyze (fixing the problem's boundary, then
asking what changed at that boundary).

**Concepts**
- Kepner-Tregoe problem analysis (from Charles Kepner and Benjamin Tregoe's
  work on management decisions): specifying the problem on four dimensions
  (what, where, when, extent), each as "is" vs. "could be, but is not"
- Distinctions: what is true only on the "is" side
- Changes: what changed in, on, or around each distinction, and when
- Testing a possible cause: it must explain both the "is" and the "is not";
  a cause that explains the problem but also predicts problems that never
  happened is rejected
- Change analysis as a stand-alone technique: comparing the problem
  situation with a similar situation that had no problem

**Why it matters**
The "is not" column is the strongest elimination tool in RCA. It kills causes
that explain the problem but also predict problems that never happened.

**Worked example**
The E04 activation cliff (a take-home exercise with artificial data, 24,436
product events, 1 Dec 2025 to 25 Jan 2026), recomputed. It was a textbook
is / is-not case, done unnamed:
- **What:** only the `share_room` event fell (85% fewer per day); every other
  event, room creation included, held up.
- **Where:** every segment fell together.
- **When:** a calendar date, 12 Jan. Even long-standing users stopped
  sharing that day.
- **Testing the causes:** six candidate causes are tested against the
  is / is-not table. The original analysis left two open: the share action broke, or
  only its tracking event broke. A check the original recommended but never
  ran settles it: buyers kept viewing new rooms after 12 Jan at the same
  rate, so rooms were still being shared, and only the tracking event broke.

**Resources**
- [Kepner-Tregoe Matrix](https://digital.ahrq.gov/health-it-tools-and-resources/evaluation-resources/workflow-assessment-health-it-toolkit/all-workflow-tools/kepner-tregoe-matrix)
  (U.S. Agency for Healthcare Research and Quality, ~5 min, verified): the
  is / is-not columns, the distinction step, and testing each cause against
  every observation.

**Exercise type:** test a teammate's proposed cause against the is / is-not
table. Fully worked.

**Interview angle:** "The metric dropped for some users but not others. How
do you narrow it down?"
---

## <u>Module 5 — The 5 Whys</u>

**DMAIC phase:** Analyze (the simplest causal drill-down).

**Concepts**
- Asking "why?" until the answer is a cause that can be acted on (five is a
  rule of thumb, not a rule), with an origin at Toyota (Sakichi Toyoda;
  Taiichi Ohno made it part of the Toyota Production System)
- Each "why" answered with evidence, not opinion
- Known failure modes: one chain when there are several causes, stopping at a
  symptom or at "human error", answers that cannot be checked, and different
  people reaching different chains
- When the 5 Whys is enough, and when to move to a fishbone or a cause map

**Why it matters**
It is the most widely used RCA technique and the most often criticised. A
learner should be able to use it well and also say exactly where it breaks.

**Worked example**
Fresh, simulated: an online store's revenue dashboard down 17.8% week over
week. It is simulated so that the two planted causes are known.
- The first chain of whys, each answered by a query, follows the biggest
  fall to Android: a new app version cannot take two card types.
- That chain explains only about half of the drop. A second chain, starting
  from a different first answer, finds the rest: a store moved to a new id
  that the dashboard does not know.
- A money waterfall splits the 16,788 drop between the two causes.

**Resources**
- [Five whys](https://en.wikipedia.org/wiki/Five_whys) (Wikipedia, ~10 min,
  verified): the method, its origin at Toyota, and its known criticisms.
- [The problem with "5 whys"](https://psnet.ahrq.gov/issue/problem-5-whys)
  (U.S. Agency for Healthcare Research and Quality, a summary of Alan Card's
  2017 critique in BMJ Quality & Safety, ~5 min, verified): why the method
  oversimplifies problems with several causes.

**Exercise type:** ask the next "why" on the second chain, and avoid stopping
at "human error". Fully worked.

**Interview angle:** "What are the limits of the 5 Whys?"
---

## <u>Module 6 — Fishbone (Ishikawa) Diagram</u>

**DMAIC phase:** Analyze (listing candidate causes with breadth).

**Concepts**
- The diagram (Kaoru Ishikawa, popularised in the 1960s): the problem as the
  head, cause categories as bones, causes and sub-causes as branches
- Category sets: the manufacturing "Ms" (Manpower, Machine, Material, Method,
  Measurement, often extended with Mother Nature and others), and a
  data-and-product adaptation (customer, product use, support, commercial,
  time, measurement)
- The fishbone as a hypothesis inventory: every branch is something to test,
  not a finding
- Scoring each branch by the evidence once tested, and correcting for testing
  many branches at once

**Why it matters**
A fishbone protects against the most common investigation error: testing
only the first cause anyone thought of.

**Worked example**
The E08 churn exercise (a take-home exercise with artificial data: 500
accounts, 22.0% flagged as churned), recomputed (reuse). 22 candidate causes
on five bones, each tested, plus checks of the churn label on a sixth:
- No customer, product, support or commercial branch clears its significance
  bar once the number of tests is accounted for.
- The measurement bone holds the real finding: the tables disagree on who
  churned at all.

An honest case where the fishbone ends with "no validated driver", and the
measurement bone explains why.

**Resources**
- [Ishikawa diagram](https://en.wikipedia.org/wiki/Ishikawa_diagram)
  (Wikipedia, ~10 min, verified): the diagram, its origin, and the category
  sets used in manufacturing, marketing and services.

**Exercise type:** decide whether the lowest p-value is a driver, given how
many branches were tested. Fully worked.

**Interview angle:** "How do you make sure you haven't missed a cause?"
---

## <u>Module 7 — Apollo Root Cause Analysis & Cause Mapping</u>

**DMAIC phase:** Analyze (causes as a graph, each backed by evidence).

**Concepts**
- Apollo RCA (Dean Gano's method, described in his book *Apollo Root Cause
  Analysis*): every effect has at least two causes acting together, an
  action (something that happened) and a condition (something that was
  true)
- Cause-and-effect charts that branch and join, rather than one line of
  "whys"
- Evidence attached to every cause, and causes with no evidence marked as
  such
- Solutions placed at any cause in the chart, not only at the "root": often
  the cheapest fix is at the condition
- Cause mapping (ThinkReliability's variant): starting from the impact on a
  goal

**Why it matters**
Real incidents usually need several causes at once. A map shows which
combination was needed, so a fix can target the cause in the combination that
is easiest to change.

**Worked example**
The E09 / E12 NYC 311 investigation (reuse), on public data re-fetched from
NYC Open Data and frozen. An August 2026 report on 311 service requests had
three alarming headlines, and each turns out to need its own pair of causes:
- **A water-and-sewer "surge":** a July label change at the
  Department of Environmental Protection (DEP), combined with a report that
  counts labels separately.
- **A closure-rate "collapse":** a young month compared with an old one,
  combined with requests that keep closing for weeks.
- **A rise in housing requests:** more were filed, but the condition behind
  it is unknown, and the map marks it as missing evidence.

**Resources**
- [Apollo Root Cause Analysis](https://realitycharting.com/apollo-root-cause-analysis-problem-solving-methodology)
  (Reality Charting, ~5 min, verified): the method's four steps, from the
  company Dean Gano founded. The actions-and-conditions principle is in his
  book, not on this page.
- [Cause Mapping](https://www.thinkreliability.com/cause-mapping/)
  (ThinkReliability, ~5 min, verified): the cause-mapping variant, which
  starts from the goal that was hurt and looks for several causes working
  together.

**Exercise type:** place a manager's claim on the cause map and check it
against the evidence. Fully worked.

**Interview angle:** "What if there's more than one root cause?"
---

## <u>Module 8 — Fault Tree Analysis</u>

**DMAIC phase:** Analyze (formal logic and probability of failure).

**Concepts**
- The top event, and the AND and OR gates beneath it, down to basic events
- Minimal cut sets: the smallest combinations of basic events that cause the
  top event
- Top-event probability from basic-event probabilities (assuming
  independence), and what breaks that assumption (common causes)
- Fault trees for diagnosis (after an incident) vs. for design (before one)

**Why it matters**
Fault tree analysis turns "it failed because A or B, but only if C" into
arithmetic. It shows which single failures can cause the problem alone, which
is where redundancy (a backup) pays off.

**Worked example**
Fresh, simulated: a daily KPI (Key Performance Indicator) email that is not
sent or is stale, over a 365-day run log. The analytic top-event probability
is checked against the simulated frequency. The prediction comes out far too
low, and the gap leads to a hidden common cause: both of the report's data
loads read the same source file.

**Resources**
- [Fault Tree Handbook with Aerospace Applications](https://extapps.ksc.nasa.gov/reliability/Documents/Fault_Tree_Handbook_with_Aerospace_Applications_August_2002.pdf)
  (NASA, 2002, verified): the standard reference. Read sections 3.8 (cut
  sets), 5.2 (common cause failures), 7.3 (top event probability), and 9.2–9.3
  (fault trees for a system in design vs. one already running).
- [Intro to Fault Tree Analysis](https://accendoreliability.com/intro-to-fault-tree-analysis/)
  (Accendo Reliability, ~5 min, verified): a short overview of the approach.

**Exercise type:** rank three fixes by the failure days each would have
saved, and compare with what the tree as designed would have said. Fully
worked.

**Interview angle:** "How would you make a daily report more reliable?"

---

## <u>Module 9 — Barrier Analysis</u>

**DMAIC phase:** Improve (deciding which defences to build or strengthen).

**Concepts**
- Hazard, target, barrier: what can do harm, what it harms, and what stands
  in between
- Barrier types: physical, administrative (procedures), and detection
  (monitoring)
- Barrier states: present and worked, present but failed, missing
- The "Swiss cheese" model: an incident needs the holes in several layers to
  line up

**Why it matters**
Cause-finding asks why the problem happened. Barrier analysis asks why
nothing stopped it, and so leads straight to what to build.

**Worked example**
Fresh and real: GitLab's published postmortem of its 31 January 2017 database
incident, in which several backup and replication barriers all failed. The
numbers and URL are verified at build time.

**Exercise type:** to be set when the module is built.

**Interview angle:** "The fix is in. How do you make sure it can't happen
again?"

---

## <u>Module 10 — FMEA (Failure Mode and Effects Analysis)</u>

**DMAIC phase:** Control (ranking what could still fail, and turning it into
the control plan).

**Concepts**
- Failure mode, effect, cause, current control
- The three ratings: Severity, Occurrence, Detection (1–10)
- RPN (Risk Priority Number = S × O × D) and its known pitfalls (equal RPNs
  hiding very different risks)
- AIAG-VDA (Automotive Industry Action Group / German Association of the
  Automotive Industry) Action Priority as the modern replacement
- From FMEA to control plan: each high-priority mode gets a monitor, a limit,
  an owner and a response

**Why it matters**
FMEA is the forward-looking twin of root-cause analysis: instead of "why did
it fail?" it asks "how could it fail next, and would we notice?" It closes the
DMAIC loop.

**Worked example**
Fresh, simulated: an FMEA for the data platform from Module 2. Occurrence is
rated from the incident-log frequencies and Detection from the logged
time-to-detect, so the ratings come from data, not opinion.

**Exercise type:** to be set when the module is built.

**Interview angle:** "How do you prioritise which risks to monitor?"

---

## The DMAIC segment ends here

Modules 1–10 used one structure: every technique was placed inside a DMAIC
phase. **That segment is complete.**

Module 11 begins a **different, complete, competing approach**: 8D. It is not
a second spine for the same techniques and is not blended with DMAIC. It is a
separate problem-solving structure with different priorities, and it is
compared against DMAIC as a whole.

---

## <u>Module 11 — 8D (Eight Disciplines)</u>

**Segment:** competing approach, standalone.

**Concepts**
- The disciplines: D0 plan, D1 team, D2 problem description, D3 interim
  containment, D4 root cause and escape point, D5 permanent corrective
  action, D6 implement and validate, D7 prevent recurrence, D8 recognise the
  team
- Where 8D differs from DMAIC: containment before analysis (D3), the escape
  point (why detection missed it) as a required second root cause (D4), and
  systemic prevention (D7)
- When to choose 8D (a customer-facing defect that needs containment now) vs.
  DMAIC (a chronic process-performance gap)

**Why it matters**
8D is the standard in manufacturing and supplier quality, and many companies'
incident-review formats are 8D in disguise. Knowing both structures means
choosing one on purpose.

**Worked example**
The E01 funnel drop again (reuse), deliberately: the same incident run through
8D gives a like-for-like comparison with Module 1's DMAIC version.

**Exercise type:** to be set when the module is built.

**Interview angle:** "Your customers are seeing wrong numbers right now. What
do you do first?"

---

## <u>Module 12 — Capstone: the `investigator` Skill and its test</u>

**Concepts**
- A decision layer: "if the problem looks like X, use technique Y, because
  Z", with pointers back to this playbook's notebooks for depth
- Two modes: follow a named technique faithfully; or, on an open "investigate
  why this happened", choose and justify the technique(s)
- Testing an AI behaviour change: pre-registered cases with a known planted
  cause, a with-Skill vs. without-Skill comparison, and blind grading

**Deliverable**
The Skill (saved outside this repo, in the user's general skills folder) and
`12_capstone_investigator_test.md`: the test design, the rubric, per-case
scores and the result.
