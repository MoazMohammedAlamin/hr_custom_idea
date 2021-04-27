# Copyright (C) 2018 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api
from  odoo.exceptions import  UserError


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirmed'),
        ('approve','Approved'),
    ], string='Status', readonly=True, default='draft')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_approve(self):
        for rec in self:
            rec.state = 'approve'

    # def action_draft(self):
    #     for rec in self:
    #         rec.state = 'draft'

 # overread unlink function
    def unlink(self):
        print("self statement", self)
        for rec in self:
             if rec.state == 'approve' or 'confirm':
               raise UserError('Sorry, You can not deleted')
        # rtn = super(department, self).unlink()
        rtn = super(HrEmployee, self).unlink()
        print("Return statement", rtn)
        return rtn
# not Duplicate name function
    @api.constrains('name')
    def check_name(self):
        for rec in self:
            if self.search([('name', '=', rec.name),
                            ('id', '!=', rec.id)]):
                raise UserError('Sorry, This Employee name is already Found !')

    children_ids = fields.One2many(
        string="Children Info",
        comodel_name="hr.employee.children",
        inverse_name="employee_id",
    )


class ChildrenInformation(models.Model):
    _name = "hr.employee.children"
    _description = "Children Information"
    child_name = fields.Char(string='Name')
    type = fields.Selection(
        string="Type",
        selection=[("son", "Son"), ("daughter", "Daughter")])
    education_level = fields.Selection(
        string="Education Level",
        selection=[("preschool", "PreSchool"), ("peramiryschool", "Peramiryschool"),("secandaryschool", "Secandaryschool"),("university", "University")])

    employee_id = fields.Many2one(string="Employee", comodel_name="hr.employee")


# Department Tables
class department(models.Model):
    _inherit = "hr.department"

    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirmed'),
        ('approve','Approved')
    ], string='Status', readonly=True, default='draft')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_approve(self):
        for rec in self:
            rec.state = 'approve'

    # def action_draft(self):
    #     for rec in self:
    #         rec.state = 'draft'
# Not Duplicate name function
    @api.constrains('name')
    def check_name(self):
        for rec in self:
            if self.search([('name', '=', rec.name),
                            ('id', '!=', rec.id)]):
                raise UserError('Sorry, This Department name is already Found !')

# overread unlink function
    def unlink(self):
        print("self statement", self)
        for rec in self:
             if rec.state == 'approve' or 'confirm':
               raise UserError('Sorry, You can not deleted')
        rtn = super(department, self).unlink()
        print("Return statement", rtn)
        return rtn
# Job Position Tables
class job_position(models.Model):
    _inherit = "hr.job"

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('approve', 'Approved')
    ], string='Status', readonly=True, default='draft')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_approve(self):
        for rec in self:
            rec.state = 'approve'

    # def action_draft(self):
    #     for rec in self:
    #         rec.state = 'draft'
    
# overread unlink function
    def unlink(self):
        print("self statement", self)
        for rec in self:
             if rec.state == 'approve' or 'confirm':
               raise UserError('Sorry, You can not deleted')
        # rtn = super(department, self).unlink()
        rtn = super(job_position, self).unlink()
        print("Return statement", rtn)
        return rtn
# Not Duplicate Function
    @api.constrains('name')
    def check_name(self):
        for rec in self:
            if self.search([('name', '=', rec.name),
                            ('id', '!=', rec.id)]):
                raise UserError('Sorry, This Job Position name is already Found !')


# Contract Table
class contrcat(models.Model):
    _inherit = "hr.contract"

# Training Table
class training(models.Model):
    _name = "human.training"
    image = fields.Image()
    name = fields.Char(required=True)
    phone = fields.Char(string="Work Phone", required=True)
    mobile = fields.Char(string="Work Mobile", required=True)
    location = fields.Char(string="Work Location", required=True)
    email = fields.Char(string="Work Email", required=True)
    department_id = fields.Many2one("hr.department", string="Department")
    employee_id = fields.Many2one("hr.employee", string="Employee Responsible")
    manager_id = fields.Many2one("hr.employee", string="Manager")
    date_today = fields.Date(string="Date", readonly=True, default=fields.Date.today())
    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirm'),
        ('approve','Approve'),
        ('cancel','Cancel')
    ], string="Status", readonly=True, default='draft')
    certificates = fields.Selection([
        ('diploma','Diploma'),
        ('bachelor','Bachelor'),
        ('master','Master'),
        ('phd','PhD')
    ], string="Certificates", default="diploma", required=True)
    university = fields.Char(string="University Name", required=True)
    faculty = fields.Char(string="Faculty Name", required=True)
    date_graduation = fields.Date(string="Graduation Date", required=True)
    address = fields.Char(string="Address")
    facebook = fields.Char(string="FaceBook Name")
    k_m_home = fields.Integer(string="Km Home Work")
    identification_no = fields.Char(string="Identification_No")
    passport_no = fields.Char(string="PassPort_No")
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ], string="Gender",  default="male")
    date_of_birth = fields.Date(string="Date of Birth")
    place_of_birth = fields.Char(string="Plac of Birth")
    parent_name = fields.Char(string="Parent Name")
    parent_type = fields.Selection([
        ('father','Father'),
        ('mother','Mother'),
        ('brother','Brother'),
        ('sister','Sister'),
        ('husband','Husband'),
        ('wife','Wife')
    ], string="Parent Type", default="father")
    company = fields.Char(string="Company Name")
    company_address = fields.Char(string="Company Address")
    job = fields.Char(string="Job Position")
    work_phone = fields.Char(string="Work Phone")
    work_email = fields.Char(string="Work Email")
    work_address = fields.Char(string="Address")
    date = fields.Date(string="Data of Birth")
    place = fields.Char(string="Place of Birth")
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    calendar = fields.Many2one("resource.calendar", required=True, string="Working Schedule")
    salary = fields.Float(string="Training Salary")

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_approve(self):
        for rec in self:
            rec.state = 'approve'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            if self.search([('name', '=', rec.name),
                            ('id', '!=', rec.id)]):
                raise UserError('Sorry, This Trainer name is already Found !')

    def unlink(self):
        print("self statement", self)
        for rec in self:
            if rec.state == 'approve' or 'confirm':
                raise UserError('Sorry, You can not deleted')
        # rtn = super(department, self).unlink()
        # rtn = super(job_position, self).unlink()
        rtn = super(training, self).unlink()
        print("Return statement", rtn)
        return rtn

    # @api.model
    # def _default_image(self):
    #     image_path = get_module_resource('hr', 'static/src/img', 'default_image.png')
    #     return base64.b64encode(open(image_path, 'rb').read())



