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
import frappe
from telegram_productivity.telegram_productivity.utils.telegram_bot import main
from telegram import Bot
import asyncio
from frappe import request
import json

@frappe.whitelist(allow_guest=True)
def telegram_webhook():
    # Get the bot instance
    application = frappe.local.telegram_application

    # Process the update
    if request.method == "POST":
        update = json.loads(frappe.request.data)
        application.update_queue.put(update)
    
    return "OK"

def get_application():
    return asyncio.run(main())

def after_migrate():
    print("Telegram bot installed - Migrate")
    print("Telegram bot installed - Install")
    # Replace 'YOUR TOKEN' and 'YOUR WEBHOOK URL' with your actual bot token and webhook URL
    bot = Bot("7177299800:AAHVyt9iDJGukGdHaVKXJojKStEgQyxG0tI")
    webhook_url = "https://ffd4-2401-4900-1ce0-3808-4d7b-4338-b0b6-24a2.ngrok-free.app/api/method/telegram_productivity.telegram_productivity.utils.overrides.telegram_webhook"
    bot.set_webhook(url=webhook_url)
    frappe.local.telegram_application = get_application()
    
# def after_install():
#     print("Telegram bot installed - Install")
#     # Replace 'YOUR TOKEN' and 'YOUR WEBHOOK URL' with your actual bot token and webhook URL
#     bot = Bot("7177299800:AAHVyt9iDJGukGdHaVKXJojKStEgQyxG0tI")
#     webhook_url = "https://ffd4-2401-4900-1ce0-3808-4d7b-4338-b0b6-24a2.ngrok-free.app/api/method/telegram_productivity.telegram_productivity.utils.overrides.telegram_webhook"
#     bot.set_webhook(url=webhook_url)