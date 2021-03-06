# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Account Invoice Comission",
    "version": "12.0.1.0.0",
    "author": "Odoo Nodriza Tech (ONT), "
              "Odoo Community Association (OCA)",
    "website": "https://nodrizatech.com/",
    "category": "Tools",
    "license": "AGPL-3",
    "depends": [
        "base",
        "account",
        "sale",
        "account_invoice_date_paid_status"
    ],
    "external_dependencies": {
        "python": [
            "unidecode"
        ],
    },
    "data": [
        "views/account_invoice_view.xml",
        "views/product_template_view.xml",
        "views/res_users_view.xml",
        "wizard/account_invoice_line_commission.xml",
    ],
    "installable": True
}
