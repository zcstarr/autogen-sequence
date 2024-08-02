# Autogen Sequence Generator

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Generate Only the PlantUML Script](#generate-only-the-plantuml-script)
  - [Generate PlantUML Script and Image Locally](#generate-plantuml-script-and-image-locally)
  - [Generate Sequence Image]
- [Caveats](#caveats)
- [Issues](#issues)

## Overview
This Python script processes log files to generate sequence diagrams. It can generate diagrams using a remote PlantUML server or locally if PlantUML is installed on your system. The script is designed to read log files where each line is a JSON object with specific attributes related to events in a system.

## Requirements
- Python 3.6 or higher
- `argparse` (standard Python library)
- `plantuml` Python module for remote diagram generation
- PlantUML software installed for local diagram generation

## Installation

### Python Dependencies
Install the necessary Python package using pip:
```bash
pip install plantuml
```
### Local PlantUML Setup
 -  For local diagram generation, install PlantUML:
 - Download PlantUML from http://plantuml.com/download.
 - Ensure you have Java installed, as PlantUML runs on Java.
 - Set up the PlantUML executable in your PATH or use it directly by specifying its location.


### Usage Section

```markdown
## Usage

### Command Line Arguments
- `filename`: Path to the log file to process.
- `--output-script`: Specifies the filename for saving the generated PlantUML script. Default is `sequence_diagram.puml`.
- `--output-image`: Specifies the filename for saving the diagram image. Default is `sequence_diagram.png`.
- `--no-image`: If set, no image will be generated, only the PlantUML script.
- `--local`: If set, the diagram will be generated locally. If not set, it uses a remote PlantUML server.
- `--help`: A quick help guide

### Examples

#### Generate Only the PlantUML Script
python autogen_sequence_diagram.py path/to/logfile.log --no-image

#### Generate Diagram Using Remote PlantUML Server
```bash
python autogen_sequence_diagram.py path/to/logfile.log
```

#### Generate Sequence Image
The easiest way to do this without installing plantuml is to use the online service hosted by plantuml. Simply copy paste your sequence diagram in. If messages are super long you may need to truncate them before they render.

https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000

### Local vs. Remote Generation Section

#### Local Generation
```
python autogen_sequence_diagram.py path/to/logfile.log --local
```


## Local vs. Remote Generation
- **Remote**: The script sends the generated PlantUML script to a remote server, which returns the diagram image. This method requires an active internet connection and availability of the remote server. Currently a bug with default server
- **Local**: The script uses the local PlantUML setup to generate the diagram. This method requires prior installation of PlantUML and is generally faster and more reliable than the remote method.

## Bugs 
File an issue if you see any any PRs are always greatly appreciated



