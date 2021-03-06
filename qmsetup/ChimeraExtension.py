#!/usr/bin/env python
# encoding: utf-8


from __future__ import print_function, division
import chimera.extension


class QMSetupExtension(chimera.extension.EMO):

    def name(self):
        return 'Tangram QMSetup'

    def description(self):
        return "Prepare input files for Gaussian jobs"

    def categories(self):
        return ['InsiliChem']

    def icon(self):
        return

    def activate(self):
        self.module('gui').showUI()


chimera.extension.manager.registerExtension(QMSetupExtension(__file__))
