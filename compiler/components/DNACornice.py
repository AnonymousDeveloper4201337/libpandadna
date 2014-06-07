import DNAGroup
from DNAPacker import *


class DNACornice(DNAGroup.DNAGroup):
    COMPONENT_CODE = 12

    def __init__(self, name):
        DNAGroup.DNAGroup.__init__(self, name)

        self.code = ''
        self.color = (1, 1, 1, 1)

    def setCode(self, code):
        self.code = code

    def setColor(self, color):
        self.color = color

    def traverse(self, recursive=True, verbose=False):
        packer = DNAGroup.DNAGroup.traverse(self, recursive=False, verbose=verbose)
        packer.name = 'DNACornice'  # Override the name for debugging.

        packer.pack('code', self.code, SHORT_STRING)

        for component in self.color:
            packer.pack('color', int(component * 255), UINT16)
        return packer
