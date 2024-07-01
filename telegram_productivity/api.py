import frappe
import asyncio
from telegram_productivity.telegram_productivity.utils.telegram_bot import send_notification


def send_telegram_msg(self, method):
	try:
		if self.approval_status == 'Draft':
			# employee_id = self.employee
			expense_approver = self.expense_approver
			from_user = self.employee_name # frappe.db.get_value("Telegram User Details", {"user":employee_id}, ["telegram_username"])
			user_id, username = frappe.db.get_value("Telegram User Details", {"user":expense_approver}, ["telegram_user_id", "telegram_username"])
			doc_name =self.name
			asyncio.run(send_notification(user_id=user_id,username=username,doc_name=doc_name,status = self.approval_status,from_user = from_user))
			frappe.msgprint("telegram notification sent successfully")
		elif self.approval_status == 'Approved':
			user_id = frappe.db.get_value("Employee",filters = {"name":self.employee},fieldname = "user_id")
			from_user = self.expense_approver
			hr_names = frappe.db.get_list("User",filters= {"role_profile_name" : "HR Manager"}, fields = ["name"])
			for name in hr_names:
				user_id, username = frappe.db.get_value("Telegram User Details", {"user":name.get('name')}, ["telegram_user_id", "telegram_username"])
				doc_name =self.name
				loop = asyncio.get_event_loop()
				task = loop.create_task(send_notification(user_id=user_id,username=username,doc_name=doc_name,status = self.approval_status, from_user = from_user))
				loop.run_until_complete(task)
				#asyncio.run(send_notification(user_id=user_id,username=username,doc_name=doc_name,status = self.approval_status, from_user = from_user))
				frappe.msgprint("telegram notification sent to HR successfully")
		else:
			frappe.log_error(str(e))
	except Exception as e:
		frappe.log_error(str(e))
