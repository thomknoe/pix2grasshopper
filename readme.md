# Overview

pix2grasshopper is an OpenAI-integrated Grasshopper component set that processes digital images, with a particular emphasis on patterns found in nature, using CLIP to classify images, JSON to store descriptions, and ChatGPT to generate functional GhPython scripts with generating slider parameters and optional error handling methods. It helps designers bypass any linguistic limitations and create a workflow where their inspiration—often rooted in visual and spatial understanding—directly informs the design process without the need for translation into code-specific language. The primary users for this component set are students, bio-inspired designers, parametric designers, and 3D artists.

# Quick start

_To use pix2grasshopper with success, please download this repository and use the pix2grasshopper_main_demo_example.gh file for code generation. While there exists a component plugin, pix2grasshopper.gha which can be installed by placing it in your Grasshopper special components folder, it is currently experiencing errors in the geometry output._

_You will also need your own OpenAI API key to use this workflow_

1. Clone this repsoitory `git clone https://github.com/thomknoe/pix2grasshopper.git`
2. Open the file `pix2grasshopper_main_demo_example.gh` and ensure you also have `descriptions.json`
3. Follow the instructions in the large text panel in the pix2grasshopper workspace, and enjoy!

# Detailed Guide

The pix2grasshopper component set consists of three different components that combine to create a system for inputting images and generating code. They are pix2grasshopper, Code Checker, and Code Executable. Each component has different communications with OpenAI API and have different outputs for both the Grasshopper and Rhino environment.

## pix2grasshopper Component

Processes an input image to generate a caption using the CLIP model and creates Python code for nature-inspired geometry
in Grasshopper using OpenAI's GPT API. Outputs include the generated code, parameter ranges, and image description.

### Inputs:

- my_key (str): OpenAI API key.
- img_path (str): Path to the input image.
- json_path (str): Path to the token JSON.
- on_off (bool): Trigger to run the script.

### Outputs:

- code (str): Generated Python code for Grasshopper.
- params (str): JSON string of parameter names and ranges.
- desc (str): Image description from CLIP.

## Code Checker Component

Processes an input Python code string, parses dynamic inputs from a dictionary, executes
the code, and handles errors by fetching code suggestions from OpenAI to fix the issues.

### Inputs:

- my_key (str): OpenAI API key.
- params (str): Dictionary string representing dynamic slider inputs, parsed into a Python dictionary.
- code (str): Python code string to be executed with dynamic inputs.

### Outputs:

- feedback (str): The original or corrected Python code after execution, including suggestions for errors.
- exec_results (dict): The results from executing the Python code.

## Code Executable Component

Manages input sliders in Grasshopper, parses dictionary strings into Python dictionaries, executes
provided code with dynamically generated inputs, and manages sliders based on parsed input values.
It can also clear dynamic inputs and associated sliders, and it handles errors during execution.

### Inputs:

- params (str): A string representing a dictionary of dynamic input ranges.
- code (str): The Python code string to be executed with dynamic inputs.
- reset (bool): Flag to clear dynamic inputs and sliders.

### Outputs:

- geometry: The processed results (geometry) after code execution.

# Main Workspace

The main pix2grasshopper workspace is the primary hub for generating geometry, and having an overview over all all of the inputs and outputs going into the pix2grasshopper system. The main workspace is divided into three sections: a section where all the file paths and API keys reside, a section where all the python components operate, and a section where all the outputs from the system can be seen via text panels.

# Results

### Image 1

### Image 2

# Current Limitations/Bugs

- Process errors occur when the reset button is pressed if there is not a one-to-one correspondence between dynamically generated sliders and inputs
- Sliders do not update the geometry upon generationa nd require a manual componenent reset in order to manipulate the geometry in real time
- Not all geometries are valid and sometimes fail to render, which can be due to item type (i.e. producing Goo objects istead of Geometry objects)
