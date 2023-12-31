# MiniSB-Extruder-Mounts

Remix of the Mini-Stealthburner to run other Extruders.

![Lineup of Standard Extruder-Mounts](images/Standard_Lineup.png)
![Lineup of Minified Extruder-Mounts](images/Minified_Lineup.png)

This repo includes reworked Files of the Mini-Stealthburner to allow you to use different, namely:

- [Phaetus Apus](https://www.phaetus.com/apus/)
- [Mellow Libra Mini](https://www.aliexpress.com/item/1005003506182112.html)
- [Annex Engineering Sherpa Micro](https://github.com/Annex-Engineering/Sherpa_Micro-Extruder)
- [Annex Engineering Sherpa Mini](https://github.com/Annex-Engineering/Sherpa_Mini-Extruder)
- [Orbiter v1.5](https://orbiterprojects.com/orbiter-1-5/)
- [LDO Orbiter v2.0](https://orbiterprojects.com/orbiter-v2-0/)
- TriangleLab TBG-Lite ([Left](https://www.aliexpress.com/item/1005004186141062.html)- and [Right](https://www.aliexpress.com/item/1005003908281100.html)-Version)
- [Vz-Hextrudort Low CNC](https://github.com/VzBoT3D/Vz-HextrudORT)
- [Bondtech LGX-Lite](https://www.bondtech.se/product/lgx-lite-large-gears-extruder/)

The only parts that have changed are the Cowling, Strain-Relief and the Spacers. Everything else is Stock(Hotend Mount, X-Carriage) so this is a drop-in-replacement for Printers with the V0.2-Style X-Carriage.

As I don't have all the extruders some are untested, however if the CAD-Files are accurate they should work fine. This table shows the versions I have verified to work (green checkmark):
| Extruder | Standard | Minified |
| -------- | -------- | -------- |
| Phaetus Apus | N/A | :grey_question: |
| Libra Mini | :grey_question: | :grey_question: |
| Sherpa Micro | :heavy_check_mark: | :heavy_check_mark: |
| Sherpa Mini | :heavy_check_mark: | :heavy_check_mark: |
| Orbiter v1.5 | :grey_question: | :grey_question: |
| Orbiter v2.0 | :heavy_check_mark: | :heavy_check_mark: |
| TBG-Lite Left | :heavy_check_mark: | :heavy_check_mark: |
| TBG-Lite Right | :heavy_check_mark: | :heavy_check_mark: |
| Vz-Hextrudort Low CNC | :heavy_check_mark: | :heavy_check_mark: |
| LGX-Lite | :grey_question: | :grey_question: |

## Versions

There are two visual Versions, a "Standard" and a "Minified" Version. The Standard-Version has the upper Logo-Part of the Mini-Stealthburner in front of the Extruder (like [Mavericks LGX-Lite Mod](https://mods.vorondesign.com/detail/nJmiEHmmiI9woW4PqjQ2dA)). The Minified Version doesn't have this cover and is more in line with the Bowden Toolhead or [Mini-AfterSherpa](https://github.com/PrintersForAnts/Mini-AfterSherpa).

### Rapido HF, Dragon UHF and TriangleLab Dragon Ace

Additionally, there are longer cowlings and Hotend mounts to allow you to use a Rapido HF or a Dragon UHF. These versions can be found in the "High_Flow"-Folders of each extruder. **Remember that this will reduce a bit of the usable z height, so update your firmware configuration.**

Also, there is a mount for the [Dragon Ace Hotend](https://www.trianglelab.net/products/dragon-ace%E2%84%A2-hotend) (the mount is exactly the same as the Dragon UHF). With this mount you can use the Dragon Ace with the "Standard Flow" cowlings as it is 3 mm shorter than the Rapido HF or Dragon UHF. Alternatively you can use the spacer that is included with the Dragon ace and use it with the "High Flow" cowlings.

### Klicky and KlickyNG

Also, for Klicky Users there are cowlings with the probe carrier part for both "normal" [Klicky and KlickyNG](https://github.com/jlas1/Klicky-Probe).

### One Fits Most Version a.k.a. Swiss Cheese

There is a [Version](/Extruder_Mounts/_OneFitsMost/) that aims to support as many extruders as possible, while needing as few printed parts as possible. Dubbed Swiss cheese.

### ZeroClick

**Currently untested**

Support for the [ZeroClick Probe by zruncho3d](https://github.com/zruncho3d/ZeroClick) is available.
To make space and reduce the chance of collisions, the Dock and Mount have been remade, and special Cowlings are necessary. Also, unlike other remixes of the MiniSB for ZeroClick, this implementation should (barely) allow the use of both Sequin LEDs. More information can be found in the [ZeroClick Common Folder](/Extruder_Mounts/_ZeroClick-Common/).

### Boop

The non Klicky Cowlings have a cutout for [Boop](https://github.com/PrintersForAnts/Boop).
This is currently untested. The current strain-reliefs and PCB-plates are incompatible,
I recommend using [KayosMakers CANboard Mounts](https://github.com/KayosMaker/CANboard_Mounts).

## Strain-Relief and Spacers

Also included are Strain-Reliefs (quickly and crappily thrown together), Mounting Plates for the [Umbilical-PCB by Timmit](https://github.com/VoronDesign/Voron-Hardware/tree/master/V0-Umbilical) and mounting plates for CAN Toolhead boards based on [@KayosMaker/CANboard_Mounts](https://github.com/KayosMaker/CANboard_Mounts). **If you use a PCB Toolhead board please double-check, that the screws on the mounting plate don't short anything!**

The needed Spacers (Size according to CAD) are also included, both in the standard round shape and an octagon version inspired by [KayosMaker](https://github.com/KayosMaker/CANboard_Mounts). The Octagon Spacers are the preferred version, because these don't rely on layer-adhesion for their strength and can be printed lying down instead. Also note that depending on which motor you have on your extruder the Spacer-Length can change because Moons-Motors have a thicker Mounting-Flange (2.5 mm) compared to LDO (2 mm). Keep in mind, when installing the Heatsets into the spacers they can get squished, so the alignment is not 100% correct anymore. If you have issues with this try using longer spacers.

## Print-Instructions

Standard Voron Print-Settings (0.2 mm Layer Height, 4 Perimeters, 40% Infill, 5 Top- and Bottom-Layers). No Supports are needed and all STLs are oriented the correct way and ready to import and print.

## Assembly

Pretty much all the mounts get assembled the same way, important differences get called out in the mount-specific Assembly Manual:

1. Install Heatset-Inserts into Spacers, if your Extruder gets screwed down from the top also install Heatsets into the Cowling
2. Install Fans according to [V0.2 Assembly Manual](https://github.com/VoronDesign/Voron-0/blob/Voron0.2/Manuals/VORON_V0.2_Assembly_Manual.pdf) (page 165-167)
3. Insert the M3 Hex-Nut into the slot on the top of the cowling
4. Secure Extruder to the Cowling with hardware mentioned in the mount-specific BOM
5. Install Hotend, make sure to cut the PTFE-Tube to the correct length.
6. Install everything to the X-Carriage, secure with 2 M3x35 BHCS from the front and 1 M3x20 BHCS from the rear
7. Add Spacers for strain-relief/umbilical plate, you may need to replace some screws to have enough thread to engage with the spacers
8. Add strain-relief/umbilical plate, secure to spacers and X-Carriage

## Credits

The cowling files have been remixed from [Mavericks LGX-Lite Mod](https://mods.vorondesign.com/detail/nJmiEHmmiI9woW4PqjQ2dA). CAD-Files are included as well as Base-CAD-Files, so you can easily create a Version for your Extruder.

For the umbilical plates [Timmit's PCB CAD](https://github.com/VoronDesign/Voron-Hardware/tree/master/V0-Umbilical) was used.

The CAN-board mounts are remixed from [KayosMakers CANboard Mounts](https://github.com/KayosMaker/CANboard_Mounts)

The Klicky Parts were directly taken from [JosAr's CAD-Files](https://github.com/jlas1/Klicky-Probe) on the Klicky-Probe GitHub.

ZeroClick Parts are based on [zruncho3d's original mod](https://github.com/zruncho3d/ZeroClick).

## Extras

There are Toolhead Pictures for the Mainsail sidebar included in the Extras Folder.

![Mainsail Sidebar](images/mainsail-sidebar-example.png)

# Changelog

## 2023-12-26

- Added experimental ZeroClick support. Progresses [#4](https://github.com/JackJack3231/MiniSB-Extruder-Mounts/issues/4)
- Added Dragon Ace Mount
- Spelling and grammar fixes in the repo

## 2023-11-15

- Added experimental Boop Support
- Fixed STL names of OneFitsMost, Sherpa Micro and TBG-Lite Left
- (Re-) Added a small gap to the hexagonal contact between x-carriage and cowling, like in the original Mini-Stealthburner

## 2023-08-29 Late August Update

- Remade all the CAD-Files. This was mainly to make updating in the future easier and faster. This resulted in cosmetic changes to all the cowlings and the umbilical plates. Strain relief plates have been altered in their height to be more consistent, the old STLs are still available in the Legacy folders.
- Changed naming scheme of most STLs to make files easier to identify
- Promoted HF-Cowlings from experimental to full release.
- Updated Dragon UHF and Rapido Mount to use Holes for M2.5 instead of M3 screws.
- Added Klicky and KlickyNG Cowlings (untested).
- Added CAN-Board mounts (untested).
- Orbiter v2.0: Dropped the "Offset"-Versions for now, unless someone wants them back.
- Apus: Removed the "printed Adapter"-Cowling, as there is now enough space for the Heatsets with the default adapter in the cowling because the Hex-nut was moved back a bit in the last update. There still is a printable adapter for people that don't have the default adapter anymore.

## 2023-08-17

- Added LGX-Lite Mounts. As Maverick hasn't updated the original Mod to the R1 ducts, I decided to add updated LGX-Lite Mounts to this repo. This includes Strain Relief, Umbilical Plate and a Minified Version.
- Added small hexagonal shape to the rear of the cowling. This makes it slot into the X-Carriage even more, thanks [@probably-Erwins-Cat](https://github.com/probably-Erwins-Cat) for pointing that out. Closes [#3](https://github.com/JackJack3231/MiniSB-Extruder-Mounts/issues/3)
- Moved Hex nut in the cowling back 2 mm so now a M3x20 BHCS can be used to secure the cowling from the back instead of a M3x22.

## 2023-07-29:

- Update Rapido Cowlings to use R1-style part-cooling-ducts (a bit ugly but should work pretty well)
- Add Dragon UHF Mount, as it should work just like the Rapido HF
- Update One Fits Most Version to use R1 part-cooling-ducts (missed that last time)

## 2023-06-13:

- Update Cowling ducts to the improved ones from the [V0.2r1 Release](https://github.com/VoronDesign/Voron-0#v02r1-2023-june). Rapido Cowlings are using the old ducts for now.

## 2023-06-06:

- Add Experimental Rapido HF Cowlings based on [Mavericks mod](https://mods.vorondesign.com/detail/dWZjGJ83RbTpRTdYYRwng).
