# -*- coding: utf-8 -*-
"""
Created : 2025-10-29

@author: Marius K.
"""

from docxtpl import DocxTemplate

DEST_FILE = "output/embedded_chart.docx"

tpl = DocxTemplate("templates/embedded_chart.docx")

context = {"color1": "Series 1", "data1": 10.5, "data2": 20}

tpl.render(context)
tpl.save(DEST_FILE)
