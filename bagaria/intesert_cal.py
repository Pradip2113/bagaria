# import frappe
# from frappe.utils import nowdate, get_datetime
# @frappe.whitelist()
# def recalculate_interest():
#     frappe.msgprint("assssssssssssssss")
    # invoices = frappe.get_all("Sales Invoice", filters={"status": "Overdue"})
    # for invoice in invoices:
    #     doc = frappe.get_doc("Sales Invoice", invoice.name)
    #     if doc.due_date:
    #         current_date = nowdate()
    #         difference_in_days = (get_datetime(current_date) - get_datetime(doc.due_date)).days
            
    #         if difference_in_days > 0:
    #             aoutint = (doc.outstanding_amount * doc.custom_interest_rate) / 100
    #             final_interest = (aoutint / 365) * difference_in_days
                
    #             # Update the fields without violating submission rules
    #             doc.custom_interest_amount = final_interest
    #             doc.custom_final_amount = final_interest + doc.outstanding_amount
    #             doc.save(ignore_permissions=True)

    # To schedule this function, add it to your hooks.py
