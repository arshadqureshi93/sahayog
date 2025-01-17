from __future__ import unicode_literals
import frappe
from frappe import _

def emp_enable_disable(doc, method):
    status = doc.status
    user = doc.user_id

    current_status = frappe.db.get_value('User', user, 'enabled')

    if status == "Active":
        # If the user is not already enabled, set the 'enabled' field to 1
        if current_status != 1:
            frappe.db.set_value('User', user, 'enabled', 1, update_modified=False)
            frappe.msgprint(f"User {user} is now enabled.")
        

    elif status == "Inactive":
        # If the user is not already disabled, set the 'enabled' field to 0
        if current_status != 0:
            frappe.db.set_value('User', user, 'enabled', 0, update_modified=False)
            frappe.msgprint(f"User {user} is now disabled.")
