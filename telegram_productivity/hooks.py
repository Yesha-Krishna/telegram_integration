app_name = "telegram_productivity"
app_title = "Telegram Productivity"
app_publisher = "krishna"
app_description = "to attain productivity using telegram"
app_email = "krishna@aerele.in"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/telegram_productivity/css/telegram_productivity.css"
# app_include_js = "/assets/telegram_productivity/js/telegram_productivity.js"

# include js, css files in header of web template
# web_include_css = "/assets/telegram_productivity/css/telegram_productivity.css"
# web_include_js = "/assets/telegram_productivity/js/telegram_productivity.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "telegram_productivity/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "telegram_productivity/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "telegram_productivity.utils.jinja_methods",
#	"filters": "telegram_productivity.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "telegram_productivity.install.before_install"
# after_install = "telegram_productivity.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "telegram_productivity.uninstall.before_uninstall"
# after_uninstall = "telegram_productivity.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "telegram_productivity.utils.before_app_install"
# after_app_install = "telegram_productivity.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "telegram_productivity.utils.before_app_uninstall"
# after_app_uninstall = "telegram_productivity.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "telegram_productivity.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	# "ToDo": "custom_app.overrides.CustomToDo"
    # "Expense Claim": "telegram_productivity.telegram_productivity.utils.overrides.Notification"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Expense Claim": {
		"validate": "telegram_productivity.api.send_telegram_msg",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"telegram_productivity.tasks.all"
#	],
#	"daily": [
#		"telegram_productivity.tasks.daily"
#	],
#	"hourly": [
#		"telegram_productivity.tasks.hourly"
#	],
#	"weekly": [
#		"telegram_productivity.tasks.weekly"
#	],
#	"monthly": [
#		"telegram_productivity.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "telegram_productivity.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "telegram_productivity.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "telegram_productivity.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["telegram_productivity.utils.before_request"]
# after_request = ["telegram_productivity.utils.after_request"]

# Job Events
# ----------
# before_job = ["telegram_productivity.utils.before_job"]
# after_job = ["telegram_productivity.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"telegram_productivity.auth.validate"
# ]
