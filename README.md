# MiniSB-Extruder-Mounts
Remix of the Mini-Stealthburner to run other Extruders

![Lineup of Extruder-Mounts](images/_MiniSB-Lineup-Combined_v3.png)

This repo includes reworked Files of the Mini-Stealthburner to allow you to use diferent Extruders, namely:
- [Mellow Libra Mini](https://www.aliexpress.com/item/1005003506182112.html)
- [Annex Engineering Sherpa Micro](https://github.com/Annex-Engineering/Sherpa_Micro-Extruder)
- [Annex Engineering Sherpa Mini](https://github.com/Annex-Engineering/Sherpa_Mini-Extruder)
- [LDO Orbiter v2.0](https://orbiterprojects.com/orbiter-v2-0/)
- Trianglelab TBG-Lite ([Left](https://www.aliexpress.com/item/1005004186141062.html)- and [Right](https://www.aliexpress.com/item/1005003908281100.html)-Version)
- [Vz-Hextrudort Low CNC](https://github.com/VzBoT3D/Vz-HextrudORT)

The only parts that have changed are the Cowling, Strain-Relief and the Spacers. Everything else is Stock(Hotend-Mount, X-Carriage) so this is a drop-in-replacement for Printers with the V0.2-Style X-Carriage.

As I don't have all of the extruders some are untested, however if the CAD-Files are accurate they should work fine. This table shows the versions i have verified to work (green checkmark):
| Extruder | Standard | Minified |
| -------- | -------- | -------- |
| Libra Mini | :grey_question: | :grey_question: |
| Sherpa Micro | :heavy_check_mark: | :heavy_check_mark: |
| Sherpa Mini | :heavy_check_mark: | :heavy_check_mark: |
| Orbiter v2.0 | :heavy_check_mark: | :heavy_check_mark: |
| TBG-Lite Left | :heavy_check_mark: | :heavy_check_mark: |
| TBG-Lite Right | :grey_question: | :grey_question: |
| Vz-Hextrudort Low CNC | :heavy_check_mark: | :heavy_check_mark: |

## Versions
There are two Versions, a "Standard" and a "Minified" Version. The Standard-Version has the upper Logo-Part of the MiniStealthburner in front of the Extruder (like [Mavericks LGX-Lite Mod](https://mods.vorondesign.com/detail/nJmiEHmmiI9woW4PqjQ2dA)). The Minified Version doesn't have this cover and is more in line with the Bowden-Toolhead or [Mini-AfterSherpa](https://github.com/PrintersForAnts/Mini-AfterSherpa).

## Strain-Relief and Spacers
Also included are Strain-Reliefs (quickly and crappily thrown together) and Mounting Plates for the [Umbilical-PCB by Timmit](https://github.com/VoronDesign/Voron-Hardware/tree/master/V0-Umbilical).

The needed Spacers (Size according to CAD) are also included, both in the standard round shape and a octagon version inspired by [KayosMaker](https://github.com/KayosMaker/CANboard_Mounts). The Octagon Spacers are the preferred version, because these don't rely on layer-adhesion for their strength and can be printed lying down instead. Also note that depending on which motor you have on your extruder the Spacer-Length can change because Moons-Motors have a thicker Mounting-Flange (2.5mm) compared to LDO (2mm). Keep in mind, when installing the Heatsets into the spacers they can get squished, so the alignment is not 100% correct anymore. If you have issues with this try using longer spacers.

## General BOM
Needed for all mounts unless otherwise specified in specific mount instructions
| Part                             | Quantity | Usage                       |
| -------------------------------- | -------- | --------------------------- |
| M3x35 BHCS                       | 2        | Front Cowling Screws (same as stock MiniSB)             |
| M3x22 BHCS            | 1        | Rear X-Carriage Screw, M3x25 + a Washer also works                     |

## Print-Instructions
Standard Voron Print-Settings (0.2mm Layer Height, 4 Perimeters, 40% Infill, 5 Top- and Bottom-Layers). No Supports are needed and all STLs are oriented the correct way and ready to import and print. 

## Assembly
Pretty much all of the mounts get assembled the same way, important differences get called out in the mount-specific Readme:
1. Install Heatset-Inserts into Spacers, if your Extruder gets screwed down from the top also install Heatsets into the Cowling
2. Install Fans according to [V0.2 Assembly Manual](https://github.com/VoronDesign/Voron-0/blob/Voron0.2/Manuals/VORON_V0.2_Assembly_Manual.pdf) (page 165-167)
3. Secure Extruder to the Cowling with hardware mentioned in the mount-specific BOM
4. Install Hotend, make sure to cut the PTFE-Tube to the correct length.
5. Install everything to the X-Carriage, secure with 2 M3x35 BHCS from the front and 1 M3x22 BHCS from the rear
6. Add Spacers for strain-relief/umbilical plate, you may need to replace some screws to have enough thread to engage with the spacers
7. Add strain-relief/umbilical plate, secure to spacers and X-Carriage
## Credits
The files have been remixed from [Mavericks LGX-Lite Mod](https://mods.vorondesign.com/detail/nJmiEHmmiI9woW4PqjQ2dA). CAD-Files are included as well as Base-CAD-Files so you can easily create a Version for your Extruder.

## Extras
There are Toolhead-Pictures for the Mainsail sidebar included in the Extras Folder.

![Mainsail Sidebar](images/mainsail-sidebar-example.png)
