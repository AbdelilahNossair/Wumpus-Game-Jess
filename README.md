# Wumpus World in Jess

A rule-based artificial-intelligence simulation written for the Jess Java expert-system shell. A hunter explores a cave world, reasons from perceptions, seeks gold, and avoids pits and a Wumpus.

## Core ideas

The world separates physical facts from the hunter's knowledge. Templates represent hunters, caves, hazards, gold, exits, desires, and goals. Rules infer safety/perceptions and select actions using priorities.

The project demonstrates symbolic reasoning and goal selection rather than machine learning. Scenario facts define fixed worlds; changing the cave file changes the experiment.

## Repository map

| Path | Purpose |
| --- | --- |
| `ww.jess` | Templates, helper functions, and hunter/world rules |
| `cave0.jess`–`cave3.jess` | Initial world facts |
| `jess.jar` | Bundled Jess runtime |
| `docs/` | Bundled Jess documentation/API reference |
| `examples/`, `jess/examples/` | Runtime examples, separate from the Wumpus simulation |
| `LICENSE` | Jess license agreement |

## Prerequisites

Use a Java runtime compatible with the bundled legacy Jess JAR. Check that `java -version` works. No Maven/Gradle installation or Python/npm dependency is involved.

Review [LICENSE](LICENSE) before using or redistributing the bundled runtime. The file is a restricted Jess license agreement, **not MIT**. An earlier README's MIT description did not match that file.

## Launch and load a scenario

```bash
git clone https://github.com/AbdelilahNossair/Wumpus-Game-Jess.git
cd Wumpus-Game-Jess
java -cp jess.jar jess.Main
```

At the Jess prompt, enter:

```clojure
(batch "ww.jess")
(batch "cave0.jess")
(reset)
(run)
```

The batch commands load rules and initial facts. Reset asserts scenario deffacts, and run fires the rule engine. Paths are relative to the current directory.

To try another world, start a fresh Jess process and replace `cave0.jess` with the chosen file. Loading several scenario files into an existing session can replace or mix definitions unexpectedly.

## Included scenarios

| File | World | Examples of contents |
| --- | --- | --- |
| `cave0.jess` | 4 × 4 | Xena, multiple pits, gold, a blocked cell |
| `cave1.jess` | 4 × 4 | Actaeon, gold at (2,2), pit and Wumpus |
| `cave2.jess` | 4 × 4 | Orion, gold at (3,2), colocated pit/Wumpus |
| `cave3.jess` | 6 × 5 | Seeker, larger layout, several blocked cells |

Coordinates in the scenarios start at 1. World definitions include `worldsize`, `hunter`, `wumpus`, `pit`, `gold`, `exit`, and optional `nocave` facts.

## Inspect and customize

Useful Jess commands include:

```clojure
(facts)
(agenda)
(watch rules)
(watch facts)
(run 1)
```

Inspect facts before and after a single rule firing to understand state transitions. Tracing is verbose; enable it for a small scenario first.

To create a scenario, copy one cave file, keep coordinates inside its world size, and set hunter, exit, gold, hazards, and blocked cells. To change behavior, inspect desire strengths, goal-selection rules, and safety inference in `ww.jess`.

## Validation and limitations

Run each bundled scenario from a clean session, inspect hunter location/alive/gold fields, and compare the trace when changing one rule or hazard. No automated expected-outcome suite is included, so the presence of a scenario does not guarantee the agent succeeds in it.

The project bundles runtime documentation, examples, and compiled files that are not specific to the simulation. A cleaner distribution would separate original simulation source from externally obtained runtime dependencies while preserving notices. The runtime's rights and legacy compatibility should be resolved before using this as a publicly redistributed starter project.
