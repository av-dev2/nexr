app_name = "nexr"
app_title = "Nexr"
app_publisher = "elius mgani"
app_description = "MCP Development and Assistant Tool for Frappe based apps"
app_email = "eliasmgani@gmail.com"
app_license = "mit"
app_version = "1.0.0"

# MCP Server Configuration
# -------------------------
# Nexr provides a Model Context Protocol (MCP) server for AI-assisted development.
# 
# Endpoint: /api/method/nexr.mcp.handle_mcp
# 
# Available MCP Tools:
# - create_doctype: Create DocTypes with file generation for any app
# - get_doctype_schema: Retrieve DocType metadata and fields
# - get_all_doctypes: List all DocTypes filtered by app
# - create_document: Create documents in any DocType
# - get_document: Retrieve single document by name
# - get_documents: Query documents with filtering and sorting
# - update_document: Update existing documents
# - delete_document: Delete documents
# - get_field_options: Get options for Link/Select fields
# - get_installed_apps: List installed apps with versions
# - run_bench_command: Execute whitelisted bench commands
# - health_check: Check server and site status
# 
# Authentication: Frappe API Key/Secret
# Transport: Streamable HTTP (MCP over HTTP)
# Version Support: Frappe v14, v15, v16+
# 
# For setup instructions, see: https://github.com/av-dev2/nexr

# Apps
# ------------------

# Frappe is required and will be automatically installed if not present on the site
required_apps = ["frappe"]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "nexr",
# 		"logo": "/assets/nexr/logo.png",
# 		"title": "Nexr",
# 		"route": "/nexr",
# 		"has_permission": "nexr.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nexr/css/nexr.css"
# app_include_js = "/assets/nexr/js/nexr.js"

# include js, css files in header of web template
# web_include_css = "/assets/nexr/css/nexr.css"
# web_include_js = "/assets/nexr/js/nexr.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "nexr/public/scss/website"

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
# app_include_icons = "nexr/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "nexr.utils.jinja_methods",
# 	"filters": "nexr.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "nexr.install.before_install"
# after_install = "nexr.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "nexr.uninstall.before_uninstall"
# after_uninstall = "nexr.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "nexr.utils.before_app_install"
# after_app_install = "nexr.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "nexr.utils.before_app_uninstall"
# after_app_uninstall = "nexr.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nexr.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nexr.tasks.all"
# 	],
# 	"daily": [
# 		"nexr.tasks.daily"
# 	],
# 	"hourly": [
# 		"nexr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nexr.tasks.weekly"
# 	],
# 	"monthly": [
# 		"nexr.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "nexr.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nexr.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "nexr.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["nexr.utils.before_request"]
# after_request = ["nexr.utils.after_request"]

# Job Events
# ----------
# before_job = ["nexr.utils.before_job"]
# after_job = ["nexr.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"nexr.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

