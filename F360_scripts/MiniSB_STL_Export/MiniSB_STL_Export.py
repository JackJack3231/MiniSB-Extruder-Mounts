# Author - JackJack3231
# Description
# Exports most of the printed Files for the MiniSB mod as STL and presorts them into correct folders so they can be moved over to the main folder easily.

import adsk.core, adsk.fusion, adsk.cam, traceback
import os.path, sys
from .src import pathvalidate


def doExport(geometry, exportMgr, exportDir, filename):
    subDir = ""
    if "HF" in geometry.name:
        subDir = "High_Flow (Rapido HF or Dragon UHF)"
    elif "SF" in geometry.name:
        subDir = "Standard_Flow"
    elif any(
        x in geometry.name
        for x in ["CAN_Plate", "Strain_Relief_Plate", "Umbilical_Plate", "Spacer"]
    ):
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

    # Create required folders, Fusion will not create the directories and instead throw an error
    os.makedirs(exportDir, exist_ok=True)

    fullPath = os.path.join(exportDir, filename + ".stl")

    stlExportOptions = exportMgr.createSTLExportOptions(geometry, fullPath)
    stlExportOptions.sendToPrintUtility = False
    stlExportOptions.meshRefinement = (
        adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
    )
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
            ui.messageBox("No active Fusion design", "No Design")
            return

        rootComp = design.rootComponent

        (extruderName, cancelled) = ui.inputBox(
            "Enter Extruder Name",
            "Export STLs",
            rootComp.name.replace("MiniSB-", "").split(" ")[0],
        )

        if cancelled:
            return

        if not pathvalidate.is_valid_filename(extruderName + ".stl"):
            ui.messageBox("Invalid Filename!")
            return

        exportDir = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), ".export", extruderName, "STL"
        )

        exportMgr = design.exportManager

        # Search through design for things to export
        exportItems = []
        for occ in rootComp.allOccurrences:
            if "XXX" in occ.name and occ.isVisible:
                exportItems.append(occ)

            for body in occ.bRepBodies:
                if "XXX" in body.name and body.isVisible:
                    exportItems.append(body)

        # Remove duplicates from found items
        prunedItems = []
        for item in exportItems:
            unique = True
            for comp in prunedItems:
                if item.name.split(":")[0] == comp.name.split(":")[0]:
                    unique = False
                    break
            if unique:
                prunedItems.append(item)

        del exportItems

        progressDialog = ui.createProgressDialog()
        progressMsg = "Exporting STL %v of %m\n"
        progressDialog.isCancelButtonShown = False
        progressDialog.show("Exporting STLs", progressMsg, 0, len(prunedItems), 0)

        for item in prunedItems:
            progressDialog.progressValue += 1
            filename = item.name.replace("XXX", extruderName).split(":")[0]
            progressDialog.message = progressMsg + filename
            doExport(item, exportMgr, exportDir, filename)

        progressDialog.hide()

        if sys.platform.startswith("win"):
            os.startfile(exportDir)
        ui.messageBox(
            "Successfully exported " + str(len(prunedItems)) + " STLs to:\n" + exportDir
        )
    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))
