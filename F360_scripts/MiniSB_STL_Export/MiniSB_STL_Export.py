# Author - JackJack3231
# Description
# Exports most of the printed Files for the MiniSB mod as STL and presorts them into correct folders so they can be moved over to the main folder easily.

import adsk.core, adsk.fusion, adsk.cam, traceback
import os.path, sys


def doExport(occ, exportMgr, scriptDir, exName):
    exportDir = scriptDir + "\\" + ".export" + "\\" + exName + "\\" + "STL" + "\\"

    if "HF" in occ.name:
        exportDir += "High_Flow (Rapido HF or Dragon UHF)\\"
    elif "SF" in occ.name:
        exportDir += "Standard_Flow\\"
    elif "CAN_Plate" or "Strain_Relief_Plate" or "Umbilical_Plate" in occ.name:
        exportDir += "Strain_Relief\\"

    if "KlickyNG" in occ.name:
        exportDir += "KlickyNG\\"
    elif "Klicky" in occ.name:
        exportDir += "Klicky\\"
    elif "ZeroClick" in occ.name:
        exportDir += "ZeroClick\\"
 
    os.makedirs(exportDir, exist_ok=True)

    filename = occ.name.replace("XXX", exName).split(":")[0]

    fullPath = exportDir + filename + ".stl"

    stlExportOptions = exportMgr.createSTLExportOptions(occ, fullPath)
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


