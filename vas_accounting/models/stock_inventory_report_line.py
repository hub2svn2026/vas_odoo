# -*- coding: utf-8 -*-
from odoo import models

class StockInventoryReportLine(models.Model):
    _name = 'stock.inventory.report.line'
    _description = 'Kết quả báo cáo nhập xuất tồn theo kỳ'