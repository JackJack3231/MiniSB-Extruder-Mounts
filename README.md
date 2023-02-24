# MiniSB-Extruder-Mounts
Remix of the Mini-Stealthburner to run other Extruders

![Lineup of Extruder-Mounts](./_MiniSB-Lineup-Combined.png)

This repo includes reworked Files of the Mini-Stealthburner to allow you to use diferent Extruders, namely:
- [Mellow Libra Mini](https://www.aliexpress.com/item/1005003506182112.html)
- [Annex Engineering Sherpa Micro](https://github.com/Annex-Engineering/Sherpa_Micro-Extruder)
- [Annex Engineering Sherpa Mini](https://github.com/Annex-Engineering/Sherpa_Mini-Extruder)
- [LDO Orbiter v2.0](https://orbiterprojects.com/orbiter-v2-0/)
- Trianglelab TBG-Lite ([Left](https://www.aliexpress.com/item/1005004186141062.html)- and [Right](https://www.aliexpress.com/item/1005003908281100.html)-Version)
- [Vz-Hextrudort Low](https://github.com/VzBoT3D/Vz-HextrudORT)

The only parts that have changed are the Cowling, Strain-Relief and the Spacers. Everything else is Stock(Hotend-Mount, X-Carriage) so this is a drop-in-replacement for Printers with the V0.2-Style X-Carriage.

## Versions
There are two Versions, a "Standard" and a "Minified" Version. The Standard-Version has the upper Logo-Part of the MiniStealthburner in front of the Extruder (like [Mavericks LGX-Lite Mod](https://mods.vorondesign.com/detail/nJmiEHmmiI9woW4PqjQ2dA)). The Minified Version doesn't have this cover and is more in line with the Bowden-Toolhead or [Mini-AfterSherpa](https://github.com/PrintersForAnts/Mini-AfterSherpa).

## Strain-Relief and Spacers
Also included are Strain-Reliefs (quickly and crappily thrown together) and Mounting Plates for the [Umbilical-PCB by Timmit](https://github.com/VoronDesign/Voron-Hardware/tree/master/V0-Umbilical).

The needed Spacers (Size according to CAD) are also included, both in the standard round shape and a octagon version inspired by [KayosMaker](https://github.com/KayosMaker/CANboard_Mounts). The Octagon Spacers are the preferred version, because these don't rely on layer-adhesion for their strength and can be printed lying down instead. Also note that depending on which motor you have on your extruder the Spacer-Length can change because Moons-Motors have a thicker Mounting-Flange (2.5mm) compared to LDO (2mm). Keep in mind, when installing the Heatsets into the spacers they can get squished, so the alignment is not 100% correct anymore. If you have issues with this try using longer spacers.

## Print-Instructions
Standard Voron Print-Settings (0.2mm Layer Height, 4 Perimeters, 40% Infill, 5 Top- and Bottom-Layers). No Supports are needed and all STLs are oriented the correct way and ready to import and print. 

## Credits
The files have been remixed from [Mavericks LGX-Lite Mod](https://mods.vorondesign.com/detail/nJmiEHmmiI9woW4PqjQ2dA). CAD-Files are included as well as Base-CAD-Files so you can easily create a Version for your Extruder.
