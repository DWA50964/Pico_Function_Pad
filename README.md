# Pico_Function_Pad
A Raspberry Pi Pico powered macro/function pad that is fully programmable for multiple applications and uses.

The main aim of this project is to create a cheap and extremely flexible function pad that can quickly and easily jump between its different uses. There are many devices on the market that achieve similar goals, although many are flawed by lack of functionality, being too application specific or too expensive. 

### Project Goals:
-	Cheap (Less than £25).
-	Minimal knowledge required to build.
-	Minimal Components and Assembly.
-	Easy to program and customise.
-	Can adapt to current use case.

# What does this look like?

![(Picture of Version 1 Unit) ](res/finalV1Case.jpeg?raw=true)

Above you can see the Version 1. Contained in a fully 3D printed enclosure there are 11 x Kailh Gold mechanical keyboard switches (with keycaps), 6 x 5mm LEDs (and resistors) and at its heart a Raspberry Pi Pico running Circuit Python.

Depending on where you buy the parts and assuming you have a 3D printer this can all be had for less than £15. This makes it cheap enough.

In regard to how adaptable it is, I’m barely scratching the surface of what this device is capable of, with the Circuit Python at your disposal, you can achieve quite a bit. In my initial testing I have been working mainly with the USB_HID Library turning it into a number pad and mouse mover to name a few. I plan to expand greatly on my devices capabilities as I continue with the project. 

So far I believe that I am on track to achieving my goals. In the short term I will primarily be working on the software side of things and expanding the capabilities and functionality of my device. In the long term I plan to design a Version 2 to fix any flaws with my current unit and make it much easier to build, replicate, modify and customise.

**Current Feature List:**
- Number Pad
- Extended Function Keys (F13-F22)
- LED Test Mode

**Upcoming Features:**
- MIDI note outputs
- MIDI note inputs (Changing LEDs and modes)
- Integration with broadcast software (VMix)
- Program launching 

## Further Information
This repository and project as a whole is still very work in progress. I have plans to make this project extremly accessable and include everything that would be needed to replicate and/or expand upon my project, including but not limited too, detailed documentation, CAD/STL files, assembly instructions and most importantly, robust and well documented code.
Please be patient and keep checking back for updates and improvements. 
