#!/usr/bin/python3

import SharedLibrary

parseline=SharedLibrary.ParseLine()

port=parseline.get_accessport()

print(port)
