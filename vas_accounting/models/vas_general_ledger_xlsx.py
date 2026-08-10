# -*- coding: utf-8 -*-
from odoo import models

class VasGeneralLedgerXlsx(models.AbstractModel):
    _name = 'report.vas_accounting.vas_general_ledger_xlsx'
    _description = 'Sổ Cái S03b-DN XLSX'

    def _get_report_values(self, docids, data=None):
        return {'doc_ids': docids, 'doc_model': '', 'docs': [], 'data': data}