G21          ; Set units to millimeters
G90          ; Set to absolute positioning
G28          ; Home all axes (X, Y, and Z)

G1 Z5 F300   ; Lift tool to 5mm above the bed at 300mm/min speed
G1 X0 Y0     ; Move to the starting corner (0,0)

G1 Z0 F150   ; Lower tool to touch the bed surface
G1 X100 F1200; Cut/move right 100mm
G1 Y100      ; Cut/move up 100mm
G1 X0        ; Cut/move left 100mm
G1 Y0        ; Cut/move down 100mm (back to start)

G1 Z10 F300  ; Lift tool 10mm to clear the workspace
M30          ; End of program
