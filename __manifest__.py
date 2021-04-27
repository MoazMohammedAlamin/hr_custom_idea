
{
    "name": "Idea HR Employee",
    "version": "13.0.1.0.0",
    "category": "Human Resources",
    "website": "",
    "author": "(IDEA)",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "sequence":-8,
    "summary": "VIEW CUSTOMIZE WORK",
    "depends": ["hr"],
    "external_dependencies": {"python": ["dateutil"]},
    "data": [
        "security/idea_secuirty.xml",
        "security/ir.model.access.csv",
        "views/hr_employee.xml",
        "reports/report.xml"
    ],
}
