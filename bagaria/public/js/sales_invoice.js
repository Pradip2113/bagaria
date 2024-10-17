



frappe.ui.form.on('Sales Invoice', {
    after_save:async function(frm) {
        if (frm.doc.status === "Overdue") {
            const duedate = frm.doc.due_date;
            const currentDate = frappe.datetime.now_date();
            const differenceInDays =await frappe.datetime.get_diff(currentDate, duedate);
            const aoutint =await (frm.doc.outstanding_amount * frm.doc.custom_interest_rate) / 100;
            const finalss =await (aoutint / 365) * differenceInDays;
            // frappe.throw(String(finalss))
            await frappe.db.set_value("Sales Invoice",frm.doc.name,"custom_interest_amount",finalss)
            await frappe.db.set_value("Sales Invoice",frm.doc.name,"custom_final_amount",finalss + frm.doc.outstanding_amount)
            console.log(`Difference in days: ${finalss}`);
        } else {
            console.log("Due date is not defined.");
        }
    } 
});
