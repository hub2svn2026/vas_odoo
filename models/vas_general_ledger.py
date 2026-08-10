# -*- coding: utf-8 -*-
from odoo import models

class VasGeneralLedger(models.AbstractModel):
    _name = 'report.vas_accounting.vas_general_ledger_pdf'
    _description = 'VAS General Ledger Report'

    def _get_report_values(self, docids, data=None):
        return {}
