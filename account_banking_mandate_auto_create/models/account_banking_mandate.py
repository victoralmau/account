# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields
from datetime import datetime


class AccountBankingMandate(models.Model):
    _inherit = 'account.banking.mandate'
    
    auto_create = fields.Boolean(
        string="Auto create"
    )        
    
    @api.model    
    def cron_fix_auto_create_banking_mandate(self):
        current_date = datetime.today()
        
        account_banking_mandate_ids = self.env['account.banking.mandate'].search(
            [
                ('state', '!=', 'cancel')
            ]
        )
        if account_banking_mandate_ids:
            partner_bank_ids = account_banking_mandate_ids.mapped('partner_bank_id')
            res_partner_bank_ids = self.env['res.partner.bank'].search(
                [
                    ('id', 'in', partner_bank_ids.ids)
                ]
            )
            if res_partner_bank_ids:
                partner_ids = res_partner_bank_ids.mapped('partner_id')
                # buscamos cuentas bancarias de los contactos que NO son estos
                res_partner_bank_ids = self.env['res.partner.bank'].search(
                    [
                        ('partner_id', 'not in', partner_ids.ids)
                    ]
                )
                if res_partner_bank_ids:
                    for res_partner_bank_id in res_partner_bank_ids:
                        vals = {
                            'auto_create': True,
                            'format': 'sepa',
                            'scheme': 'CORE',
                            'type': 'recurrent',
                            'recurrent_sequence_type': 'recurring',
                            'partner_bank_id': res_partner_bank_id.id,
                            'partner_id': res_partner_bank_id.partner_id.id,
                            'signature_date': current_date.strftime("%Y-%m-%d"),                                                             
                        }
                        account_banking_mandate_obj = self.env['account.banking.mandate'].sudo().create(vals)
                        account_banking_mandate_obj.validate()                                                    