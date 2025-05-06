# DisCoNetHeat

This app has been developed within 3DIVERSE (Decentralisation, Diversity and Dynamic Load Regulation – Novel Approaches to Tangible Energy Transition with Diversification of Production Sources) project, funded by the European Union's LIFE Programme (Grant Agreement No. 101077343).

![eu](eu.png)

Views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or CINEA. Neither the European Union nor the granting authority can be held responsible for them.

## Description
This app serves for identification of potential disconnections form district heating networks. This app generates a QGIS map based on coordinate and category data provided in an Excel file. The categories represent different Levelized Cost of Heat (LCOH) values, which are, in this example, assigned to either individual heating systems or district heating consumers. The purpose of this tool is to provide a clear, graphical representation of LCOH variations across a district heating network.

By visualizing this data spatially, the tool allows users to easily identify areas where the LCOH for district heating is higher than for individual heating. In such cases, the affected consumers or entire zones are more likely to disconnect from the district heating network, which can help stakeholders or network operators anticipate potential risks to network viability or plan future interventions. Different scenarios can be evaluated based on the different LCOH values.

The application package includes:

- run.bat: a batch file used to launch the application,
- program.py: the main Python script executed by the batch file,
- qgis_func.py: a script containing the key functions used for processing data and creating the QGIS project environment,
- example.xlsx: exemplary excel file with input data.

This setup facilitates the integration of spatial and economic data into decision-making processes for energy network planning and management.

## Requirements and how to use
1. Install QGIS 3.42.1 (Python is included in the installation) and have excel data ready with calculated LCOH values for systems that you want to compare
2. Change the path to the QGIS installation in the run.bat file if necessary
3. Change paths, column names (Longitude, Latitude and Category must always be named that way) and category colors variables in the program.py file if necessary
4. Run the run.bat file. After that you will have the .qgz file in the same directory as the program.py file and from
    there you can open the project in QGIS.
