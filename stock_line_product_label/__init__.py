from odoo import models


class StockLinePrintBarcode(models.Model):
    _inherit = "stock.move"

    def action_open_label_layout(self):
        action = self.env['ir.actions.act_window']._for_xml_id(
            'product.action_open_label_layout')
        action['context'] = {
            'default_product_ids': [self.product_id.id],
            'default_custom_quantity': self.quantity_done or 1,
        }
        return action
