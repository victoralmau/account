# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Account Invoice Shipping Expedition TXT",
    "version": "12.0.1.0.0",
    "author": "Odoo Nodriza Tech (ONT), "
              "Odoo Community Association (OCA)",
    "website": "https://nodrizatech.com/",
    "category": "Tools",
    "license": "AGPL-3",
    "depends": [
        "base",
        "account_invoice_shipping_expedition",
        "shipping_expedition_txt"  # https://github.com/OdooNodrizaTech/stock
    ],
    "external_dependencies": {
        "python": ["xlrd"],
    },
    "data": [],
    "installable": True
}
