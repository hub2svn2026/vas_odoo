# -*- coding: utf-8 -*-
from odoo import models

class VasRecomputeWizard(models.TransientModel):
    _name = 'vas.recompute.wizard'
    _description = 'Tính lại toàn bộ đối ứng'