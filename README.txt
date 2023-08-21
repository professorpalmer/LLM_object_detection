===== Python Project: Airport Diagram Updater =====

This project aims to automate the process of extracting aeronautical information from loosely structured airport diagrams using machine learning and AI techniques.

== Structure ==
/airport-diagram-updater
|-- /data
|   |-- /old_diagrams : Contains previous versions of airport diagrams.
|   |-- /new_diagrams : Contains the most recent versions of airport diagrams.
|   |-- /annotated_data : For manually annotated data, if required for model training.
|-- /models : Storage for machine learning models, if any are developed or used.
|-- /results : Output after processing diagrams, such as detected changes or extracted information.
|-- /src
|   |-- __init__.py : Initialization file for Python modules.
|   |-- change_detection.py : Module for detecting changes between old and new diagrams.
|   |-- ocr_extraction.py : Module using Optical Character Recognition to extract text from diagrams.
|   |-- object_detection.py : Module for detecting specific objects or features within diagrams.
|   |-- helpers.py : Miscellaneous helper functions and utilities.
|-- main.py : Main executable script to run the project.
|-- requirements.txt : List of required Python packages.

== Getting Started ==
1. Clone the repository to your local machine.
2. Install the required packages using pip:
   `pip install -r requirements.txt`
3. Place your old diagrams in the /data/old_diagrams directory, and new diagrams in /data/new_diagrams.
4. Run the main.py script to initiate the processing:
   `python main.py`

== Contribution ==
Feel free to contribute to this project by creating pull requests or raising issues on GitHub.
