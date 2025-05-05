from qgis_func import data_processing, qgis_app

if __name__ == "__main__":
    data_path = "data.xlsx" # Path to your Excel file, must be .xlsx
    columns_drop = ["LCOH DH (EUR/MWh)", "LCOH individual (EUR/MWh)"] # Columns to drop
    columns_dropna = ["Longitude", "Latitude", "Category"] # Columns to drop if they contain NaN values,
    shp_path = "data.shp"

    data_processing(data_path, columns_drop, columns_dropna, shp_path)

    program_path = "C:/Program Files/QGIS 3.42.1/apps/qgis" # Path to QGIS installation
    colors = ["blue", "red"] # Colors for the points
    project_path = "project.qgz" # Path to save the QGIS project
    bat_path = "C:\Program Files\QGIS 3.42.1\bin\qgis.bat" # Path to QGIS batch file

    qgis_app(program_path, shp_path, colors, project_path, bat_path)



