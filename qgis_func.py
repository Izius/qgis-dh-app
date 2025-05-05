import pandas as pd
import geopandas as gpd
from qgis.core import (
    QgsApplication, QgsProject, QgsVectorLayer, QgsRasterLayer,
    QgsCoordinateReferenceSystem, QgsSymbol, QgsRendererCategory,
    QgsCategorizedSymbolRenderer
)
from PyQt5.QtGui import QColor
import subprocess
from qgis.utils import *
from qgis.gui import QgsMapCanvas
from typing import List


def data_processing(data_path: str, columns_drop: List[str], columns_dropna: List[str], shp_path: str) -> None:
    """
    Process the data from an Excel file and save it as a shapefile.
    :param data_path:
    :param columns_drop:
    :param columns_dropna:
    :param shp_path:
    :return:
    """

    df = pd.read_excel(data_path) # Read the Excel file
    df = df.drop(columns_drop, axis=1) # Drop specified columns
    df = df.dropna(subset=columns_dropna) # Drop rows with NaN values in specified columns

    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df["Longitude"], df["Latitude"]),
        crs="EPSG:4326"
    ) # Create a GeoDataFrame with the geometry column
    gdf.to_file(shp_path) # Save the GeoDataFrame as a shapefile

    print(f"Shapefile saved: {shp_path}")

def qgis_app(program_path: str, shp_path: str, colors: List[str], project_path: str, bat_path: str) -> None:
    """
    Create a QGIS application, load a shapefile, create colored points based on shapefile and save the project.
    Colored points reperesent either LCOHdh > LCOHindivid or LCOHdh < LCOHindivid for each location.
    :param program_path:
    :param shp_path:
    :param colors:
    :param project_path:
    :param bat_path:
    :return:
    """

    QgsApplication.setPrefixPath(program_path, True)
    qgs = QgsApplication([], False)
    qgs.initQgis()

    project = QgsProject.instance()
    canvas = QgsMapCanvas()

    point_layer = QgsVectorLayer(shp_path, "Points", "ogr")
    if not point_layer.isValid():
        raise Exception("Failed to load shapefile.")

    symbol1 = QgsSymbol.defaultSymbol(point_layer.geometryType())
    symbol1.setColor(QColor(colors[0]))
    symbol1.setSize(4)

    symbol2 = QgsSymbol.defaultSymbol(point_layer.geometryType())
    symbol2.setColor(QColor(colors[1]))
    symbol2.setSize(4)

    categories = [
        QgsRendererCategory(1, symbol1, "Category 1"),
        QgsRendererCategory(2, symbol2, "Category 2")
    ]

    renderer = QgsCategorizedSymbolRenderer("Category", categories)
    point_layer.setRenderer(renderer)

    project.addMapLayer(point_layer)

    uri = "type=xyz&url=https://mt1.google.com/vt/lyrs%3Ds%26x%3D%7Bx%7D%26y%3D%7By%7D%26z%3D%7Bz%7D&zmax=19&zmin=0"
    satellite = QgsRasterLayer(uri, "Google Satellite", "wms")
    project.addMapLayer(satellite)

    root = project.layerTreeRoot()
    root.insertChildNode(0, root.findLayer(point_layer.id()))

    project.setCrs(QgsCoordinateReferenceSystem("EPSG:4326"))

    canvas.waitWhileRendering()
    extent = point_layer.extent()
    canvas.setExtent(extent)
    canvas.refresh()

    project_path = os.path.abspath(project_path)
    project.write(project_path)

    print(f"Project saved: {project_path}")

    subprocess.Popen([bat_path, project_path])

    qgs.exitQgis()