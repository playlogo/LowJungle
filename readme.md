# LowJungle

![Layout](assets/layout.png)
![PCB](assets/pcb_components.png)
![PCB](assets/pcb_routing.png)
![Case](assets/case.png)

A low profile, ~65% keyboard, with:

- Hot swappable sockets
- Per key RGB backlight
- Wifi & BLE (but no battery)
- Integrated 3 port USB Hub

Links:

- [Onshape: Case](https://cad.onshape.com/documents/196ae99135554e28081e9cd8/w/09114671e2d692aadc408c6f/e/86be969bd7a114ceaf756b4a?renderMode=0&uiState=67d72bd2d4975832f10ffe5c)
- [Keyboard Layout Editor: Layout](https://www.keyboard-layout-editor.com/#/gists/81105ca4efea79bf3cdf03d682872e17)

## Firmware

For testing: KMK  
For production: QMK

> Circuitpython is soooo much nicer for finding errors in the hardware  
> Status KMK: Pins are correct, keymap is WIP

## PCB

- [Schematic](assets/schematic.pdf)
- No relevant ERC & DRC errors
- Size: 371.48mm x 133.35mm
- VCC for backlight LEDs can be controlled by the ESP32 using 2 mosfets
- Used libraries:
  - [Marbastlib, needs to be installed as plugin](https://github.com/ebastler/marbastlib/tree/main)
  - [easyeda2kicad, needs to be installed separately, used for downloading LCSC schematics & footprints](https://github.com/uPesy/easyeda2kicad.py)
    - Download `C2913204, C192893, C2891732, C778164, C2988369, C8547, C503996, C82942` using `easyeda2kicad --full --lcsc_id=<id>` (one-by-one, yes...)
  - `0_Custom`, included in the `libraries` folder, should load automatically

## Fabrication

> I'm print all parts myself using [the large scale 3D printer (Billig)](https://github.com/playlogo/billig) I'm build for [infill](https://github.com/hackclub/infill).

> Download the latest revision from [Onshape](https://cad.onshape.com/documents/196ae99135554e28081e9cd8/w/09114671e2d692aadc408c6f/e/86be969bd7a114ceaf756b4a?renderMode=0&uiState=67d72bd2d4975832f10ffe5c). STLs included with this repo are only meant as a backup if the onshape link ever stops working.

- Largest part: 380mmx145mm
- Recommended settings:
  - 6 wall loops
  - 6 solid top & bottom layers
  - 40% infill
- Notes:
  - `LowJungle-Backplate-V2.stl`: Should be solid
  - `LowJungle-Bumper-Bottom-V2.stl`: Print with TPU, 3x
  - `LowJungle-Bumper-Top-V2.stl`: 4x
  - `LowJungle-Frame-V2.stl`: Manually place tree supports for the USB connector cutouts

## BOM

**PCB:** [$36.34 at JLCPCB](assets/jlcpcb.png)

**Switches:** [Aliexpress: Gateron KS33 low-profile red, 90 for $38.63 => 0.43 per switch](https://de.aliexpress.com/item/1005007794069535.html)

**Keycaps:** [Aliexpress: Low profile set, 143 lily version, $21.61](https://de.aliexpress.com/item/1005004882406296.html)

**Stabilizers:** [Aliexpress: Gateron low-profile stabilizer set, 4x 2u 1x 6.25u, $13.79](https://de.aliexpress.com/item/1005005296240590.html)

**Fasteners:**

| Name | Price | Link |
|------|-------|------|
| 30x M2.5x3x3.5mm Heat insert | $1.83 | [Aliexpress](https://de.aliexpress.com/item/1005003582355741.html) |
| 14x M2.5x6mm Hex socket screw (for feet) | $1.41 | [Aliexpress](https://de.aliexpress.com/item/32810872544.html)|
| 16x M2.5x8mm Hex socket screw (for mounting frame) | $1.64 | [Aliexpress](https://de.aliexpress.com/item/32810872544.html) |
| 9x M3x10mm Hex socket screw | $1.79 | [Aliexpress](https://de.aliexpress.com/item/32810872544.html) |

Total: $6,67

**MCU:**

> Note: The ESP32S3 implementation is the same as in my [Hackpad](https://github.com/hackclub/hackpad/pull/570). Thus the cost can be drastically reduced when combining both LCSC orders:
>
> - -$3: Removed handling fee
> - -$6: Random shipping coupon
> - and often times the MOQ from hackpad also covers this project

|Name|Price|Link| Needed if combined order ? |
|----|-----|----|----------------------------|
|Espressif Systems ESP32-S3-WROOM-1-N8R2| $4.41| [LCSC](https://www.lcsc.com/product-detail/WiFi-Modules_Espressif-Systems-ESP32-S3-WROOM-1-N8R2_C2913204.html)| Yes|
| N-Channel mosfet | $0.6 for MOQ | [LCSC](https://www.lcsc.com/product-detail/MOSFETs_YONGYUTAI-SI2302_C2891732.html)| Yes |
|3.3V LDO | $0.48 for MOQ| [LCSC](https://www.lcsc.com/product-detail/Voltage-Regulators-Linear-Low-Drop-Out-LDO-Regulators_MICRONE-Nanjing-Micro-One-Elec-ME6211C33M5G-N_C82942.html?s_z=n_ME6211C33M5G-N)| No |
| USB-A female| $0.42 for MOQ | [LCSC](https://www.lcsc.com/product-detail/USB-Connectors_Shenzhen-Kinghelm-Elec-KH-AF90DIP-112_C503996.html?s_z=n_usb%20a)|No |
| USB-C female| $0.4 for MOQ | [LCSC](https://www.lcsc.com/product-detail/USB-Connectors_G-Switch-GT-USB-7010ASV_C2988369.html?s_z=n_G-Switch%20GT-USB-7010asv)|No |
| P-Channel mosfet | $0.49 for MOQ | [LCSC](https://www.lcsc.com/product-detail/MOSFETs_Jiangsu-Changjing-Electronics-Technology-Co-Ltd-CJ2301-S1_C8547.html)|No |
| Mini push button | $0.47 for MOQ | [LCSC](https://www.lcsc.com/product-detail/Tactile-Switches_G-Switch-GT-TC029A-H020-L1N_C778164.html?s_z=n_SKRKAEE020)|No |
| CoreChips SL2.1A USB Hub driver | $1.32 for MOQ | [LCSC](https://www.lcsc.com/product-detail/USB-HUB-Controllers_CoreChips-SL2-1A_C192893.html?s_z=n_C192893)|No |
|---|----|---|---|
| 1N4148 Diodes | $1.04 for 100 | [LCSC](https://www.lcsc.com/product-detail/Switching-Diodes_LangJie-1N4148_C18195411.html?s_z=n_1N4148%2520Diodes) | Yes |
|10uF 0805 Capacitor | $0.16 for MOQ| [LCSC](https://www.lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_Samsung-Electro-Mechanics-CL21A106KOQNNNE_C1713.html)| No|
| 100nF * | $0.3 for MOQ | [LCSC](https://www.lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_FH-Guangdong-Fenghua-Advanced-Tech-0805B104J500NT_C29926.html)|No|
| 1uF * | $1 for MOQ | [LCSC](https://www.lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_YAGEO-CC0805JKX7R9BB105_C541528.html) | No |
|10k 0805 Resistor | $0.13 for MOQ | [LCSC](https://www.lcsc.com/product-detail/Chip-Resistor-Surface-Mount_VO-SCR0805J10K_C5140188.html?s_z=n_resistor)| No|
| 5.1k * | $0.15 for MOQ | [LCSC](https://www.lcsc.com/product-detail/Chip-Resistor-Surface-Mount_UNI-ROYAL-Uniroyal-Elec-0805W8J0512T5E_C26023.html?s_z=n_resistor) | No |
| 100k * |  $0.13 for MOQ | [LCSC](https://www.lcsc.com/product-detail/Chip-Resistor-Surface-Mount_VO-SCR0805J100K_C3017875.html?s_z=n_resistor) | No |

Total (without combined order): $11.46  
Total (with combined order): $6.01

>Note: Combined LCSC order will be around ~$28 (including shipping) for both hackpad and hackboard

**Misc Electronics:**

|Name|Price|Link|
| ----- | ---- | ---- |
| SK6812 MINI-E | $2.85 for 100 | [Aliexpress](https://de.aliexpress.com/item/1005002782417198.html) |
| Gateron Low-profile hot-swap socket | $9.03 for 100 => $0.1 per socket | [Aliexpress](https://de.aliexpress.com/item/1005008078611488.html?spm=a2g0o.productlist.main.1.3d3470f0o9Li2s&algo_pvid=ef243bac-f923-4f5b-85e0-b6818cdc378c&pdp_ext_f=%7B%22order%22%3A%2223%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A) |
| Rotary-encoder | in stock | - |

Total: $11.88

**Other parts:**

|Name|Reason|Price|Link|
|----|------|-----|----|
| Poron foam, Bottom case <-> PCB, 2.5mm 15x35cm | Sound damping | $6.10 | [Aliexpress](https://de.aliexpress.com/item/1005007442653383.html)|
| EVA foam, PCB <-> Top plate , 1mm 35x50cm | Stability of top plate |  $2.05 | [Aliexpress](https://de.aliexpress.com/item/1005002856054113.html)|
|EVA foam, PCB <-> Keyswitch  | Sound damping | $3.42 | [Aliexpress](https://de.aliexpress.com/item/1005005556269716.html)|
|PE foam, Top plate <-> Keyswitch | Water spill protection (has happened before) | $2.19 | [Aliexpress](https://de.aliexpress.com/item/1005004804230184.html)|

Total: $13,76

### BOM total

**Fasteners:** $6,67
**PCB:** $36.34  
**Switches:** $38.63  
**Keycaps:** $21.61  
**Stabilizers:** $13.79  
**MCU:** $6.01  
**Misc Electronics:** $11.88  
**Other parts:** $13,76

**Total:** $148,69

> Note: Aliexpress prices are only valid until 26. March (15. anniversary sale)
> => If the grant is issued after 24. March, it would be awesome to have ~$15 buffer for changed prices. The unused amount would be returned to HackClub.
