# import frappe
# import asyncio
# from hrms.hr.doctype.expense_claim.expense_claim import ExpenseClaim
# from telegram_productivity.telegram_productivity.utils.telegram_bot import send_notification


# class Notification(ExpenseClaim):
# 	def validate(self):
# 		super().validate()
# 		if self.approval_status == 'Draft':
# 			print("=======================================================")
# 			employee_id = self.employee
# 			expense_approver = self.expense_approver
# 			from_user = frappe.db.get_value("Telegram Employee ID", {"company_email":employee_id}, ["telegram_username"])
# 			user_id, username = frappe.db.get_value("Telegram Employee ID", {"company_email":expense_approver}, ["telegram_user_id", "telegram_username"])

# 			doc_name =self.name
# 			try:
# 				asyncio.run(send_notification(user_id=user_id,username=username,doc_name=doc_name,from_user = from_user))
# 				frappe.msgprint("telegram notification sent successfully")
# 			except Exception as e:
# 				frappe.throw(e)
# 			# else:
# 			# 	frappe.db.commit()
# 		else:
# 			print("else block ========== elseblock")