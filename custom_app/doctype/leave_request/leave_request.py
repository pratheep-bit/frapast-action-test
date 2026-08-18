import frappe
from frappe.model.document import Document

class LeaveRequest(Document):
    def on_submit(self):
        # Mutates employee status on submit but defines no on_cancel
        frappe.db.set_value("Employee", self.employee, "status", "On Leave")
