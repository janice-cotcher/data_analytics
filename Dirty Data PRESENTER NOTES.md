DIRTY DATA PRESENTER NOTES
Topic: Data Quality, Governance, and the Data-to-Value Pipeline

================================================================
SLIDE 1 — THE FIREPLACE (Opening Hook)
================================================================
Opening question to audience: "What makes good firewood?"
  - Density
  - Water content
  - Denser, drier wood burns better and produces more heat

Transition into the core analogy — value builds progressively:

1. DATA = FUEL
   - Raw data has no inherent meaning on its own

2. KNOWLEDGE = FIRE
   - Knowledge is drawn from raw data through processing and understanding
   - The quality of the raw data directly controls the quality of the analysis
   - Involves: finding patterns/relationships, building models, creating
     operational definitions
   - Key line: "We transform raw data to fuel our knowledge. Knowledge is
     power, and we use it to benefit ourselves and others."

3. VALUE = HEAT (warmth and cooking)
   - Applying insights to real-world decisions and applications
   - Requires the right conditions, tools, and knowledge to convert data
     into value
   - Quote: "Chance favours the prepared mind."

Closing line for this slide: "Garbage in, garbage out."

================================================================
SLIDE 2 — DATA / KNOWLEDGE / WISDOM FRAMEWORK
================================================================
Simple three-line framework to reinforce Slide 1:

  Data is a resource        →  Make data available
  Knowledge is power        →  Make data meaningful
  Wisdom is value            →  Make data valuable

Talking point: each stage requires a different action from us — first
access, then interpretation, then application.

================================================================
SLIDE 3 — METHODS OF ACQUIRING KNOWLEDGE
================================================================
Five methods, framed as a progression toward rigor:

1. INTUITION — "Feels true"
   Relying on gut, emotion, or instinct rather than facts or reasoning.
   Belief based on what feels true.

2. AUTHORITY — "Because I say so"
   Accepting ideas because an authority figure says they're true. Most
   knowledge comes this way since we can't independently verify
   everything — but we can learn to evaluate credentials, methods, and
   possible motives to mislead.

3. RATIONALISM — Logic and reasoning (watch for faulty logic)
   Using stated premises and logical rules to reach conclusions. Risk:
   if premises are wrong or logic has an error, the conclusion is
   invalid.

4. EMPIRICISM — Observation and experience
   Acquiring knowledge through direct observation. Limited by what we
   can perceive, and senses/prior experience can distort perception.
   Distinguish anecdotal observation from systematic (structured)
   observation — the latter underlies real science.

5. SCIENTIFIC METHOD — Testing ideas under controlled conditions
   Systematically collecting and evaluating evidence to test ideas.
   Combines intuition, authority, rationalism, and empiricism, but
   goes further: uses systematic empiricism for controlled
   observation, then rationalism to reach valid conclusions.

Source: Jhangiani, Chiang, Cuttler, & Leighton (2019). Methods of
knowing. Research Methods in Psychology.

================================================================
SLIDE 4 — DATA ON DATA (Governance Intro)
================================================================
Visual: row of robots with increasing percentages

Why Data Governance Matters:
  - Defines who owns data, how it's handled, and what rules it follows
  - Analogy: governance is "air traffic control" for data
  - Orchestrates access, quality standards, and compliance

Key stat: 54% of executives say effective data governance/management
is a top priority (IBV survey)

Source: Jonker, A., & Aquino, J. (2026, Feb 10). What is dirty data? IBM.

================================================================
SLIDE 5 — GOVERNANCE IN THE DATA LIFE CYCLE (ETL)
================================================================
Visual: mining/gem imagery representing Extract, Transform, Load

Characteristics of Good Data:
  - Falsifiable
  - Reproducible

Data Governance Framework — three pillars:

  1. Defined Roles & Responsibilities
     - Governance council / steering committee sets strategy
     - Data owners: accountable for quality within their domain
     - Data stewards: handle day-to-day quality management

  2. Clear Policies & Standards
     - Documented rules for formatting, naming, access, and protection

  3. Auditing & Monitoring Procedures
     - Ongoing audits to assess quality, compliance, and standards
       adherence

================================================================
SLIDE 6 — FOUR TYPES OF PROBLEM DATA
================================================================
Definitions (source: IBM, "What is data quality?"):

  BAD DATA
    - Inaccurate, incomplete, inconsistent, outdated, duplicate,
      invalid, or biased information that compromises decisions

  STALE DATA
    - Outdated information, misaligned with current conditions
    - One of the most pervasive, under-addressed data problems

  DARK DATA
    - Information organizations collect but never use for analytics
      or decision-making

  DIRTY DATA
    - Inaccurate, invalid, incomplete, or inconsistent — unreliable
      for business use

Additional talking points:
  - Bad data often originates at the point of collection (guesses,
    dubious entries, cleverly-worded/leading survey questions)
  - Example: federal government AI survey with no "negative" response
    options built in
  - Stale data quality degrades over time
  - Dark data connects to the "File Drawer Effect" — a null result
    (no relationship/effect) is NOT the same as bad data
  - Reference the Replication Crisis: "Many Labs Replication Project"
    (Klein et al., 2013) — produced mixed results and raised ethical
    concerns

================================================================
SLIDE 7 — KERMIT'S MIXED-UP MESSAGE (Dirty Data as Miscommunication)
================================================================
Story analogy: The Muppets are rehearsing loudly, so no one can hear
Kermit clearly on the phone. In the confusion, other Muppets each
think they heard something different:
  - Termites in Miss Piggy's ball gown
  - Gonzo will fall from the tightrope
  - Kermit doesn't like Fozzie's new jokes

Core point: Dirty data is a form of miscommunication — it is
inaccurate, invalid, incomplete, and inconsistent.

Consequence: Dirty data can distort analytics, increase scaling
errors, degrade AI model performance, and lead to poor decisions.

================================================================
SLIDE 8 — THE SNOWBALL EFFECT
================================================================
Visual: rolling snowball — dirty data compounds as it moves through
the data life cycle.

Downstream effects:
  - Outdated data / duplicate records → poor decision-making & planning
  - Incomplete data → ineffective marketing, sales, customer experience
  - Lower confidence in analysis → delayed decisions
  - Time-consuming data cleaning & reconciliation
  - Increased dependency on highly skilled individuals
  - Slower innovation
  - Reduced ROI / lost competitive advantage

================================================================
SLIDE 9 — THE COST OF DIRTY DATA
================================================================
Visual: stacking coins showing escalating cost

Key statistics:
  - IBM survey, 2025
  - 25%+ of organizations estimate annual losses exceeding $5 million
    USD due to poor data quality (Forrester)

Source: Jonker, A., & Aquino, J. (2026, Feb 10). What is dirty data? IBM.

================================================================
SLIDE 10 — ROOT CAUSES ("Roots" Tree Diagram)
================================================================
Visual: tree stump with six labeled root causes branching out.

1. HUMAN ERROR
   - Manual entry is error-prone (repetition, time pressure, cognitive
     load)
   - Results in typos, transposed characters, misread sources,
     copy-paste mistakes
   - Systematic errors multiply quickly → costly cleanup

2. DATA SILOS
   - Fragmented information across departments
   - Isolated datasets → duplicate and misaligned records
   - Difficult to resolve once entrenched

3. WEAK DATA GOVERNANCE
   - No centralized oversight or defined ownership
   - Leads to conflicting formats, naming conventions, definitions

4. FLAWED DATA INTEGRATION
   - Schema mismatches, faulty transformations, incomplete transfers
   - Increased risk in cloud/hybrid architectures

5. TECHNICAL DEBT
   - Outdated data models, limited validation, brittle legacy
     interfaces
   - Forces manual workarounds; introduces unflagged outliers

6. LACK OF VALIDATION & QUALITY CONTROLS
   - No range checks, format enforcement, required fields, or
     uniqueness constraints
   - Errors enter silently and propagate downstream

7. MISALIGNED PRIORITIES
   - Speed/volume rewarded over accuracy → rising error rates

8. MACHINE LEARNING FEEDBACK LOOPS
   - Models trained on flawed/biased data
   - Outputs reintegrated as inputs without validation → errors
     amplify over time

================================================================
SLIDE 11 — "EVERYONE IS DIFFERENT... NOT ON FIRE" (Transition Slide)
================================================================
Visual: children's book illustration reworked with "not on fire" joke
— transition into the idea that data remediation isn't one-size-fits-all.

Key point: There is no single method for remediation — every
situation is unique.

Knowledge synthesis required to fix it draws from:
  - Mathematical and statistical knowledge
  - Computer science
  - Domain knowledge

================================================================
SLIDE 12 — THE DATA SCIENCE VENN DIAGRAM
================================================================
Three overlapping circles: Mathematics/Statistics, Computer Science,
Domain Knowledge — Data Science sits at the intersection of all three.

Talking point: each area shares a portion with the others, and data
science is the subsection where all three overlap. You need all three
domains to find meaning and create value from raw data.

1. Computer Science
   - Algorithms and programming
   - Data structures
   - System design

2. Mathematics / Statistics
   - Statistical analysis
   - Mathematical modeling
   - Probability theory

3. Domain Knowledge
   - Field-specific expertise
   - Understanding context
   - Problem definition

Closing point: the field requires understanding where data comes
from, what questions to ask, and how to apply insights.

================================================================
SLIDE 12 — HOW TO CLEAN DIRTY DATA
================================================================
Diagram flow: Raw Data → Feature Engineering → Feature Set & Model

Feature engineering defined as "the creative bridge between raw data
and models." It creates a reliable, unified dataset and transforms
raw, messy data into actionable insights.

Core cleaning tasks:
  - Fix errors
  - Standardize
  - Deduplicate
  - Impute (fill missing values)
  - Improve readability (e.g., formatting timestamps)

Underlying requirement: domain knowledge + creativity — there's no
purely mechanical fix.

Dirty Data & AI:
  - AI/LLMs learn statistical patterns at scale
  - Errors and biases in training data lead to flawed, misleading
    outputs
  - Gartner prediction: through 2026, organizations will abandon 60%
    of AI projects unsupported by AI-ready data
  - Payoff of clean data: enterprises with widely trusted data achieve
    nearly double the ROI on AI investments (IBV research)

================================================================
SLIDE 14 — TOOLS & PROGRAMMING LANGUAGES FOR DATA WRANGLING
================================================================
Programming Languages:

  PYTHON
    - Most widely used language for data wrangling
    - Key libraries: pandas (dataframes, cleaning, transformation),
      NumPy (numerical operations), Polars (faster, memory-efficient
      alternative to pandas)

  R
    - Strong in statistical computing
    - Tidyverse packages (dplyr, tidyr, stringr) built around a
      "tidy data" philosophy

  SQL
    - Essential for querying, filtering, joining, and aggregating
      data directly in databases before it reaches an analyst

Point-and-Click / Low-Code Tools:

  EXCEL / GOOGLE SHEETS
    - Most common entry point for data cleaning
    - Formulas, pivot tables, Power Query

  POWER BI
    - Uses Power Query under the hood for data wrangling
    - Automatically tracks every action you take as a step-by-step,
      editable list ("Applied Steps" pane)
    - Makes the entire cleaning process transparent, reversible, and
      reproducible without writing code

  OPENREFINE
    - Free tool built specifically for cleaning messy data
    - Clustering similar text values, facet-based filtering

  TABLEAU PREP / ALTERYX
    - Visual, drag-and-drop workflows for blending and cleaning data
      without code

  TRIFACTA (now Google Cloud Dataprep)
    - Uses machine learning to suggest cleaning transformations based
      on data patterns

Enterprise / Pipeline Tools:

  DBT (data build tool)
    - Transforms data already loaded into a warehouse
    - Brings software engineering practices (version control,
      testing) to data transformation

  TALEND / INFORMATICA
    - Enterprise-grade ETL platforms with built-in data quality and
      governance features

  APACHE SPARK
    - Handles wrangling at scale across distributed systems
    - Used when datasets are too large for a single machine

Version Control & Reproducibility:

  GIT
    - Tracks changes to wrangling scripts
    - Supports collaboration and rollback

  JUPYTER NOTEBOOKS
    - Documents the wrangling process step-by-step alongside the code
    - Supports reproducibility

Key talking point: The right tool depends on data volume, team
technical skill, and whether the goal is a one-time cleanup or a
repeatable pipeline. Code-based tools (Python/R/SQL) offer more
control and reproducibility; point-and-click tools lower the barrier
to entry. Tools like Power BI blur that line — a visual interface,
but each transformation is logged as a discrete, auditable step
(similar in spirit to version control), making it easy to trace
exactly how raw data became the final dataset. VS Code Extensions like Data Wrangler make repetitive tasks faster.

================================================================
SLIDE 15 — BEST PRACTICES & PROCEDURES FOR DATA WRANGLING
================================================================
1. UNDERSTAND THE DATA BEFORE TOUCHING IT
   - Profile the dataset first: check shape, types, ranges, missing
     values, duplicates
   - Understand where the data came from and how it was collected
     before deciding how to clean it

2. DEFINE THE END GOAL FIRST
   - Know what question the data needs to answer or what model it
     will feed
   - Prevents over-cleaning or removing information that turns out
     to matter

3. DOCUMENT EVERY TRANSFORMATION
   - Keep a clear, repeatable record of every step taken (scripts,
     Applied Steps pane, notebooks, changelogs)
   - Enables reproducibility and makes errors easier to trace back

4. VALIDATE AT EVERY STAGE, NOT JUST AT THE END
   - Build in range checks, format enforcement, required fields, and
     uniqueness constraints
   - Catch errors early so they don't silently propagate downstream

5. STANDARDIZE FORMATS EARLY
   - Consistent naming conventions, date/time formats, units, and
     categorical labels across all sources
   - Prevents mismatches during integration and joins

6. HANDLE MISSING DATA DELIBERATELY
   - Decide case-by-case: remove, impute, or flag missing values
   - Avoid silently filling gaps in ways that bias downstream
     analysis

7. DEDUPLICATE CAREFULLY
   - Identify true duplicates vs. legitimate repeat records
   - Use fuzzy matching cautiously — verify results, don't assume

8. KEEP RAW DATA UNTOUCHED
   - Always preserve an unedited copy of the original dataset
   - Perform cleaning on a separate working copy so steps can be
     redone or audited

9. INVOLVE DOMAIN EXPERTISE
   - Technical cleaning alone isn't enough — domain knowledge helps
     identify what counts as an "error" versus a legitimate outlier

10. BUILD FOR REPEATABILITY
    - Where possible, turn one-time cleanup scripts into reusable
      pipelines
    - Reduces manual work and human error on future data loads

11. COMMUNICATE DATA QUALITY LIMITATIONS
    - Be transparent with stakeholders about what was cleaned,
      what wasn't, and what assumptions were made
    - Prevents overconfidence in analysis built on imperfect data

Key talking point: Data wrangling isn't a single cleanup event —
it's a disciplined, repeatable procedure. The goal is not just clean
data once, but a trustworthy, auditable process that produces clean
data every time.

================================================================
CLOSING / REFERENCES SLIDE
================================================================
Corpuz, R. (Jan 2026). Research Methods. PSYC 204 [class slides].

Corpuz, R. (Jan 2026). Overview of the Scientific Method. PSYC 204
[class slides].

Jhangiani, R. S., Chiang, I.-C. A., Cuttler, C., & Leighton, D. C.
(2019). Methods of knowing. Research Methods in Psychology.
https://kpu.pressbooks.pub/psychmethods4e/chapter/methods-of-knowing/

Jhangiani, R. S., Chiang, I.-C. A., Cuttler, C., & Leighton, D. C.
(2019). Understanding Psychological Measurement. Research Methods in
Psychology.
https://kpu.pressbooks.pub/psychmethods4e/chapter/understanding-psychological-measurement/

Jonker, A., & Aquino, J. (Feb 10, 2026). What is dirty data? IBM.
https://www.ibm.com/think/topics/dirty-data

Jonker, A., & Krantz, T. (n.d.). What is data quality? IBM.
https://www.ibm.com/think/topics/data-quality

Sadeghilalimi, M. (Sept 3, 2026). Introduction to Data Wrangling.
CS 365 [class slides].