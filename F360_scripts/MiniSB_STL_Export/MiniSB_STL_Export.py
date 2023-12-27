# Author - JackJack3231
# Description
# Exports most of the printed Files for the MiniSB mod as STL and presorts them into correct folders so they can be moved over to the main folder easily.

import adsk.core, adsk.fusion, adsk.cam, traceback
import os.path, sys
from .src import pathvalidate


def doExport(geometry, exportMgr, scriptDir, exName):
    exportDir = os.path.join(scriptDir, ".export", exName, "STL")

    subDir = ""

    if "HF" in geometry.name:
        subDir = "High_Flow (Rapido HF or Dragon UHF)"
    elif "SF" in geometry.name:
        subDir = "Standard_Flow"
    elif "CAN_Plate" or "Strain_Relief_Plate" or "Umbilical_Plate" in geometry.name:
        subDir = "Strain_Relief"

    if subDir != "":
        exportDir = os.path.join(exportDir, subDir)

    subsubDir = ""

    if "KlickyNG" in geometry.name:
        subsubDir = "KlickyNG"
    elif "Klicky" in geometry.name:
        subsubDir = "Klicky"
    elif "ZeroClick" in geometry.name:
        subsubDir = "ZeroClick"

    if subsubDir != "":
        exportDir = os.path.join(exportDir, subsubDir)
 
    os.makedirs(exportDir, exist_ok=True)

    filename = geometry.name.replace("XXX", exName).split(":")[0]

    fullPath = os.path.join(exportDir, filename + ".stl")

    stlExportOptions = exportMgr.createSTLExportOptions(geometry, fullPath)
    stlExportOptions.sendToPrintUtility = False
    stlExportOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
    stlExportOptions.isOneFilePerBody = False
    stlExportOptions.isBinaryFormat = True
                
    exportMgr.execute(stlExportOptions)
    

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        if not design:
            ui.messageBox('No active Fusion design', 'No Design')
            return
        
        rootComp = design.rootComponent

        defName = rootComp.name.replace("MiniSB-", "").split(" ")[0]

        (returnValue, cancelled) = ui.inputBox("Enter Extruder Name", "Export STLs", defName)

        if cancelled:
            return
        
        if not pathvalidate.is_valid_filename(returnValue + ".stl"):
            ui.messageBox("Invalid Filename!")
            return
        
        exName = returnValue

        scriptDir = os.path.dirname(os.path.realpath(__file__))

        exportMgr = design.exportManager

        allOccu = rootComp.allOccurrences

        for occ in allOccu:
            if "XXX" in occ.name:
                doExport(occ, exportMgr, scriptDir, exName)

            allBodies = occ.bRepBodies
            for body in allBodies:
                if "XXX" in body.name:
                    doExport(body, exportMgr, scriptDir, exName)

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))


