# Overview

pix2grasshopper is an OpenAI-integrated Grasshopper component set that processes digital images, with a particular emphasis on patterns found in nature, using CLIP to classify images, JSON to store descriptions, and ChatGPT to generate functional GhPython scripts with generating slider parameters and optional error handling methods. It helps designers bypass any linguistic limitations and create a workflow where their inspiration—often rooted in visual and spatial understanding—directly informs the design process without the need for translation into code-specific language. The primary users for this component set are students, bio-inspired designers, parametric designers, and 3D artists.

# Get Started

<mark>_To use pix2grasshopper with higher success, please download this repository and use the pix2grasshopper_main_demo_example.gh file for code generation. While there exists a component plugin, pix2grasshopper.gha which can be installed by placing it in your Grasshopper special components folder, it is currently experiencing errors in its geometry output. you will also need your own OpenAI API key to use this workflow._</mark>

Welcome to pix2grasshopper. To begin using this workflow, start by entering the full path to the JSON file called "descriptions.json" included in the file setup. The full path should begin at the top of your users directory (i.e. /Users) Then, enter the path of the image you would like to convert into Python code, again starting from the users directory. Finally, enter your OpenAI API key. Once you are done, you may now set the "Generate Code" toggle switch to True. You may have to wait a moment for the code to run and the geometry to appear. Longer wait times usually mean that the "Code Checker" component is making API requests to fix faulty code. However you should not have to wait longer than a minute. Otherwise restart Rhino and try again.

Once loaded, the geometry should appear in the Rhino viewport and the "Code Executable" component should generate sliders that correspond to parameters. Currently, these sliders cannot manipulate the geometry on generation. In order to do this, you can do two things. Either enter into the "Code Executable" component and manually run it, which will update the component to now be able to read the sliders. Or, you can delete one of the sliders, that same slider will be regenerated. You can now manipulate the sliders and the geometry will update.

This system is a work in progress and will often not generate geometry or not return code or parameters when needed. If you attempt to run the workflow and the "Code Executable" component generates sliders, but you do not see a geometry in the Rhino viewport, you may need to run it a few times until you receive a valid geometry or try a different picture. To run the workflow again after an unsuccessful attempt you need to start by setting the "Generate Code" toggle back to False, this is necessary to pause the code transfer process. Then, click the "Clear Input" button to clear out the existing inputs on the "Code Executable" component, you might see an empty error popup, ignore it and set it to not show all future popups. If Grasshopper becomes unresponsive after the first reset, click the reset button again and it will become responsive.

**WARNING: ONLY PRESS THE CLEAR INPUTS BUTTON WHEN THE "CODE EXECUTABLE" COMPONENT HAS AN EQUAL NUMBER OF INPUTS AND SLIDERS CONNECTED TO THEM, NO MORE NO LESS. OTHERWISE, THE COMPONENT WILL TIME OUT IN A PROCESS ERROR. IF THIS HAPPENS YOU NEED TO CREATE A NEW "CODE EXECUTABLE" COMPONENT BY COPYING AND PASTING A NEW ONE AND DELETING THE OLD ONE. YOU WILL NEED TO REWIRE THE GEOMETRY OUTPUT TO THE PANEL.**

Once you have no inputs in the "Code Executable" component, you can now set the "Generate Code" toggle to True once again, and repeat until you receive a valid geometry in the viewport. Continue to find different images that correspond to tokenized descriptions in the JSON file to find out what other geometries can be made.

# Detailed Guide

## System Diagram

## Description

# Main Example Workspace

# Results

### Image 1

### Image 2

# Current Limitations/Bugs
