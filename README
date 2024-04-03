# A Wumpus World Simulation in Jess

## Overview

WW.Jess is a rule-based simulation of the Wumpus World, a classic problem in artificial intelligence. The simulation is built using Jess, a rule engine for the Java platform that provides fully developed scripting language. WW.Jess allows users to explore decision-making and planning in an environment filled with hazards. The simulation features a hunter navigating through a grid of caves in search of gold while avoiding pits and a deadly wumpus.

## Getting Started

### Prerequisites
- Java Runtime Environment (JRE)
- Jess rule engine (You can obtain Jess from Sandia National Laboratories)
### Installation
- Ensure Java is installed on your system.
- Install Jess according to the instructions provided with your Jess distribution.
- Download the WW.Jess files to a directory of your choice.
### Running the Simulation
To run the WW.Jess simulation, use the Jess command-line tool and specify the main Jess file:

```bash
java -jar path/to/jess.jar -f ww.jess
(batch ww.jess)
(batch cave0.jess)
(reset)
(run)
```
Replace path/to/jess.jar with the actual path to your Jess jar file and ww.jess with the path to the WW.Jess script if necessary.

## Features

- Dynamic World Generation: The simulation constructs a world based on predefined dimensions, placing the wumpus, gold, and pits in various locations.
- Hunter Agent: A hunter navigates the world, making decisions based on perceptions (stench, breeze, glitter) in search of gold.
- Rule-Based Logic: The hunter's behavior is driven by a set of Jess rules, simulating decision-making processes.
- Safe Navigation: The hunter evaluates the safety of adjacent caves to make informed decisions about where to move next.
- Goal-Oriented Actions: The hunter's actions are driven by goals such as finding gold, shooting the wumpus, or leaving the cave system.
## Customizing the Simulation

WW.Jess allows for customization of the world size, the number of hazards, and the starting location of the hunter. These parameters can be adjusted within the Jess script to create varying levels of difficulty and to explore different strategies for navigation and survival.

## Contributing

Contributions to WW.Jess are welcome. If you have ideas for improvements or bug fixes, please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open source and available under the MIT License. Please see the LICENSE file for more details.
