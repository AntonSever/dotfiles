#!/bin/bash

xinput --set-prop $(xinput list --id-only 'DLL075B:01 06CB:76AF Touchpad') 'libinput Tapping Enabled' 1
xinput --set-prop $(xinput list --id-only 'DLL075B:01 06CB:76AF Touchpad') 'libinput Middle Emulation Enabled' 1
