# ZeroClick for Mini-Stealthburner

**All of these parts are currently untested, use at your own risk!**

This is a custom implementation of ZeroClick. The only unchanged part is the probe.
This was done to achieve the following goals:

- Clearance of the mount to avoid collisions
- Allow the use of 2 Sequins LEDs

This resulted in a custom Mount that gets attached to the cowling, an adjusted Dock and slim rail stoppers for the z-axis.

## Printed Parts

To use the ZeroClick Probe you will need to print:

- 1x [ZeroClick_Probe](https://github.com/zruncho3d/ZeroClick/blob/main/STLs/ZeroClick_Probe.stl) from the original repo. Consider printing 1 or 2 extra in case they break during assembly.
- 1x [ZeroClick_Mount](STL/ZeroClick_Mount_x1.stl). Consider printing 1 or 2 extra in case they break during assembly.
- 1x [ZeroClick_Dock_Center](STL/ZeroClick_Dock_Center.stl). The Docking position of the probe was adjusted 1.65 mm forward, so the original dock is most likely incompatible.
- 1x [Z_RailStopper_Slim_SingleSided](STL/[a]_Z_RailStopper_Slim_SingleSided.stl) and 1x [Z_RailStopper_Slim_SingleSided_Mirror](STL/[a]_Z_RailStopper_Slim_SingleSided_Mirror.stl).
- 1x Cowling for your Extruder. See the Extruder specific folders for the STL files.

## BOM

The required parts are the same as for standard ZeroClick:

| Part                     | Quantity |
| ------------------------ | -------- |
| M2x10 self-tapping screw | 2        |
| 6x3 mm magnet            | 5        |
| Omron D2F microswitch    | 1        |
| M3x6 BHCS                | 3        |
| M3 Nut                   | 2        |
| Solder wick, wire        |          |

Additionally, if you want to use the slim rail stoppers you will need a M3x8 BHCS and a M3 Nut, however these can be reused from the stock rail stoppers.

## Assembly

The assembly process is basically the same as for the original Mod, so follow the [original instructions](https://github.com/zruncho3d/ZeroClick/tree/main?tab=readme-ov-file#instructions). 

## Pictures

### Rail Stoppers:
![Rail Stoppers](images/RailStoppers.png)

### Mount:
![Mount](images/Mount.png)