# QGIS app

This app creates QGIS map based on the coordinates and categories in an excel file.
Categories are based on levelized cost of heat for either individual users or district heating. App includes run.bat file to run an application, program.py script that runs behind the run.bat file and qgis_func.py that includes functions necessary for processing and creating the QGIS project. 

## Description
This run.bat executes program.py. This program takes as an input an Excel file with
coordinates and categories (1 for LCOHdh < LCOHindivid and 2 for LCOHdh > LCOHindivid). Program first creates shape file
and then uses it and creates a map with the coordinates and categories. The map is saved as .qgz project.

## Requirements and how to use
1. Install QGIS 3.42.1 (Python is included in the installation)
2. Change the path to the QGIS installation in the run.bat file if necessary
3. Change paths, column names (Longitude, Latitude and Category must always be named that way) and category colors variables in the program.py file if necessary
4. Run the run.bat file. After that you will have the .qgz file in the same directory as the program.py file and from
    there you can open the project in QGIS.
