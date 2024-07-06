# Advanced Visualization for Deep Space Telemetry Applications

This is the project for my dissertation, "Advanced Visualization for Deep Space Telemetry Applications". This Python dashboard uses Dash to visualize Adaptive Optics Telemetry (AOT) data. The project leverages the `aotpy` Python package, along with Numpy and Plotly, and utilizes datasets from the European Southern Observatory (ESO).

## Datasets

You can test the dashboard using the following files from the [ESO Science Archive Facility](https://archive.eso.org/eso/eso_archive_main.html). Insert the program IDs `60.A-9278(#)`, with `#` as follows:
- B for GALACSI
- C for CIAO
- D for NAOMI
- E for ERIS

## Installation and Usage

### Windows Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/bea11/AOT-Dashboard.git bash'''

2. **Navigate to the Project Directory:**
   """cd AOT-Dashboard"""
3. **Run the application:**
  ''' python app.py'''
4.**Open the Dashboard:**
  After running the application, open your browser and go to the link provided (usually http://127.0.0.1:8050/).
   
### Linux Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/bea11/AOT-Dashboard.git '''

2. **Navigate to the Project Directory:**
   """cd AOT-Dashboard"""
3. **Run the application:**
  ''' python3 app.py'''
4.**Open the Dashboard:**
  After running the application, open your browser and go to the link provided (usually http://127.0.0.1:8050/).
   
### Notes:
Ensure you have Python and the necessary libraries (Dash, Numpy, Plotly, aotpy) installed. The complete versions are available on the requirements.txt of this git
