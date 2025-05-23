![pix2grasshopper header](https://github.com/thomknoe/pix2grasshopper/blob/main/github-cover.png)

# pix2grasshopper

pix2grasshopper is an OpenAI-integrated Grasshopper component set that processes digital images, with a particular emphasis on patterns found in nature, using CLIP to classify images, JSON to store descriptions, and ChatGPT to generate functional GhPython scripts with generating slider parameters and optional error handling methods. It helps designers bypass any linguistic limitations and creates a workflow where their inspiration—often rooted in visual and spatial understanding—directly informs the design process without needing to translate into code-specific language. The primary users for this component set are students, bio-inspired designers, parametric designers, and 3D artists.

# Quick Start

_To use pix2grasshopper with success, please use the `pix2grasshopper_main_demo_example.gh` file for code generation. While there exists a component plugin `pix2grasshopper.gha`, which can be installed by placing it in your Grasshopper special components folder, it is currently experiencing errors in the geometry output._

_You will also need your own OpenAI API key to use this workflow._

1. Clone this repsoitory `git clone https://github.com/thomknoe/pix2grasshopper.git`
2. Open the file `pix2grasshopper_main_demo_example.gh` and ensure you also have `descriptions.json`
3. Either load up your image or use one of the example images in the `Examples` folder
4. Follow the instructions in the large text panel in the pix2grasshopper workspace

# Detailed Guide

The pix2grasshopper component set consists of three different components that combine to create a system for inputting images and generating code. They are `pix2grasshopper`, `Code Checker`, and `Code Executable`. Each component has different communications with OpenAI API and have different outputs for both the Grasshopper and Rhino environment.

## pix2grasshopper Component

Processes an input image to generate a caption using the CLIP model and creates Python code for nature-inspired geometry in Grasshopper using OpenAI's GPT API. Outputs include the generated code, parameter ranges, and image description.

### Inputs:

- `my_key (str)`: OpenAI API key
- `img_path (str)`: Path to the input image
- `json_path (str)`: Path to the token JSON
- `on_off (bool)`: Trigger to run the script

### Outputs:

- `code (str)`: Generated Python code for Grasshopper
- `params (str)`: JSON string of parameter names and ranges
- `desc (str)`: Image description from CLIP

## Code Checker Component

Processes an input Python code string, parses dynamic inputs from a dictionary, executes the code, and handles errors by fetching code suggestions from OpenAI to fix the issues.

### Inputs:

- `my_key (str)`: OpenAI API key
- `params (str)`: Dictionary string representing dynamic slider inputs, parsed into a Python dictionary
- `code (str)`: Python code string to be executed with dynamic inputs

### Outputs:

- `feedback (str)`: The original or corrected Python code after execution, including suggestions for errors
- `exec_results (dict)`: The results from executing the Python code

## Code Executable Component

Manages input sliders in Grasshopper, parses dictionary strings into Python dictionaries, executes
provided code with dynamically generated inputs, and manages sliders based on parsed input values.
It can also clear dynamic inputs and associated sliders, and it handles errors during execution.

### Inputs:

- `params (str)`: A string representing a dictionary of dynamic input ranges
- `code (str)`: The Python code string to be executed with dynamic inputs
- `reset (bool)`: Flag to clear dynamic inputs and sliders

### Outputs:

- `geometry`: The processed results (geometry) after code execution

# Files

- `pix2grasshopper.rhproj`: pix2grasshopper plugin project file
- `pix2grasshopper.gha`: pix2grasshopper plugin for the packaged components
- `pix2grasshopper_main_demo_example.gh`: The main pix2grasshopper workspace file
- `pix2grasshopper_unpackaged_components.gh`: The unpacked components with descriptions
- `descriptions.json`: Synthetically generated database of naturalistic descriptions
