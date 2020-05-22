# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from odoo import api, models, fields
from odoo.exceptions import Warning

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    inv_vat = fields.Char(
        string='VAT',
        related='partner_id.vat'
    )
    partner_bank_name = fields.Char(
        compute='_partner_bank_name',
        string='Banco'
    )
    date_paid_status = fields.Datetime(
        string='Fecha fin pago',
        readonly=True
    )

    @api.multi
    def action_invoice_open(self):
        allow_confirm = True
        #check
        for obj in self:
            if obj.partner_id.vat==False:
                allow_confirm = False
                raise Warning("Es necesario definir un CIF/NIF para el cliente de la factura.\n")
            elif obj.type=="in_invoice" and obj.reference==False:
                allow_confirm = False
                raise Warning("Es necesario definir una referencia de proveedor para validar la factura de compra.\n")
        #allow_confirm
        if allow_confirm==True:
            return super(AccountInvoice, self).action_invoice_open()

    @api.one
    def write(self, vals):
        # stage date_paid_status
        if vals.get('state') == 'paid' and self.date_paid_status == False:
            vals['date_paid_status'] = fields.datetime.now()
        #return
        return super(AccountInvoice, self).write(vals)
    
    @api.multi        
    def _partner_bank_name(self):
        for obj in self:
            obj.partner_bank_name = ''
            if obj.partner_bank_id.id>0:
                if obj.partner_bank_id.bank_id.id>0:
                    obj.partner_bank_name = obj.partner_bank_id.bank_id.name + ' ' + obj.partner_bank_id.acc_number[-4:]
                else:
                    obj.partner_bank_name = obj.partner_bank_id.acc_number                                                                                                                                                                                                          