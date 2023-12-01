import frappe
import asyncio
from telegram_productivity.telegram_productivity.utils.telegram_bot import send_notification


async def send_telegram_msg(self, method):
	if self.approval_status == 'Draft':
		print("=======================================================")
		employee_id = self.employee
		expense_approver = self.expense_approver
		from_user = frappe.db.get_value("Telegram Employee ID", {"employee_id":employee_id}, ["telegram_username"])
		user_id, username = frappe.db.get_value("Telegram Employee ID", {"company_email":expense_approver}, ["telegram_user_id", "telegram_username"])
		doc_name =self.name
		try:
			await send_notification(user_id=user_id,username=username,doc_name=doc_name,from_user = from_user)
			frappe.msgprint("telegram notification sent successfully")
		except Exception as e:
			frappe.msgprint("Error: " + str(e))
			# else:
			# 	frappe.db.commit()
	else:
		print("else block ========== elseblock")