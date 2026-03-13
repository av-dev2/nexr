# Copyright (c) 2024, elius mgani and contributors
# For license information, please see license.txt

"""
Nexr MCP Server - AI-Assisted Frappe Development Tools

This module implements a comprehensive Model Context Protocol (MCP) server
that extends frappe/mcp with development-focused tools for creating DocTypes,
managing documents, and introspecting schemas across all Frappe apps.

Compatible with Frappe v14, v15, v16+
"""

import frappe
import frappe_mcp
import json
import os
from pathlib import Path
from typing import List, Dict, Any, Optional

# Initialize MCP server instance
mcp = frappe_mcp.MCP("nexr-dev-assistant")


# ============================================================================
# DOCTYPE CREATION & FILE GENERATION
# ============================================================================

@mcp.tool()
def create_doctype(
	app_name: str,
	doctype_name: str,
	module: str,
	fields: List[Dict[str, Any]],
	is_submittable: bool = False,
	is_child: bool = False,
	track_changes: bool = False,
	naming_rule: str = "autoname",
	autoname: Optional[str] = None,
	title_field: Optional[str] = None,
	description: Optional[str] = None
) -> Dict[str, Any]:
	"""Create a new DocType with complete file structure.
	
	This tool creates a DocType in any Frappe app and generates all required files:
	- JSON definition file
	- Python controller
	- JavaScript client controller
	- Unit test file
	
	All files are placed in the correct module directory structure and the DocType
	is inserted into the database.
	
	Args:
		app_name: Name of the Frappe app (e.g., 'hrms', 'erpnext', 'healthcare')
		doctype_name: Name of the DocType (e.g., 'Employee Skill', 'Sales Order')
		module: Module name where DocType belongs (e.g., 'HR', 'Stock', 'Accounts')
		fields: List of field definitions. Each field should be a dict with:
			- fieldname: Field name (snake_case)
			- label: Display label
			- fieldtype: Field type (Data, Link, Select, etc.)
			- options: Options for Link/Select fields
			- reqd: Required field (0 or 1)
			- read_only: Read-only field (0 or 1)
			- hidden: Hidden field (0 or 1)
			- default: Default value
		is_submittable: Whether the DocType is submittable (workflow support)
		is_child: Whether this is a child DocType (table field)
		track_changes: Whether to track document changes in Version log
		naming_rule: Naming strategy ('autoname', 'field', 'prompt', 'expression', 'random')
		autoname: Autoname pattern (e.g., 'EMP-.####', 'field:employee_name')
		title_field: Field to use as document title in listings
		description: DocType description for documentation
	
	Returns:
		dict: Status, created file paths, and any errors
	"""
	try:
		# Validate app exists
		try:
			app_path = frappe.get_app_path(app_name)
		except Exception:
			return {
				"success": False,
				"error": f"App '{app_name}' not found. Available apps: {', '.join(frappe.get_installed_apps())}"
			}
		
		# Format names for file system
		doctype_folder = frappe.scrub(doctype_name)
		module_folder = frappe.scrub(module)
		class_name = doctype_name.replace(" ", "")
		
		# Create doctype directory
		doctype_path = os.path.join(app_path, module_folder, "doctype", doctype_folder)
		os.makedirs(doctype_path, exist_ok=True)
		
		# 1. CREATE JSON DEFINITION FILE
		json_data = {
			"actions": [],
			"allow_rename": 1,
			"autoname": autoname or "hash" if naming_rule == "autoname" else None,
			"creation": frappe.utils.now(),
			"description": description or f"{doctype_name} DocType",
			"doctype": "DocType",
			"editable_grid": 1,
			"engine": "InnoDB",
			"fields": fields,
			"is_submittable": 1 if is_submittable else 0,
			"istable": 1 if is_child else 0,
			"links": [],
			"modified": frappe.utils.now(),
			"modified_by": frappe.session.user,
			"module": module,
			"name": doctype_name,
			"naming_rule": naming_rule,
			"owner": frappe.session.user,
			"permissions": [
				{
					"create": 1,
					"delete": 1,
					"email": 1,
					"export": 1,
					"print": 1,
					"read": 1,
					"report": 1,
					"role": "System Manager",
					"share": 1,
					"write": 1
				}
			],
			"quick_entry": 1,
			"sort_field": "modified",
			"sort_order": "DESC",
			"states": [],
			"title_field": title_field,
			"track_changes": 1 if track_changes else 0,
			"track_seen": 1,
			"track_views": 0
		}
		
		json_file = os.path.join(doctype_path, f"{doctype_folder}.json")
		with open(json_file, "w") as f:
			json.dump(json_data, f, indent=1)
		
		# 2. CREATE PYTHON CONTROLLER FILE
		py_content = f'''# Copyright (c) {frappe.utils.now()[:4]}, {frappe.db.get_value("User", frappe.session.user, "full_name")} and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class {class_name}(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		# TODO: Add type hints for fields here
		pass
	# end: auto-generated types

	def validate(self):
		"""Validate document before saving."""
		pass
	
	def before_save(self):
		"""Called before document is saved."""
		pass
	
	def on_update(self):
		"""Called after document is saved."""
		pass
	
	def on_submit(self):
		"""Called when document is submitted."""
		pass
	
	def on_cancel(self):
		"""Called when document is cancelled."""
		pass
	
	def on_trash(self):
		"""Called before document is deleted."""
		pass
'''
		
		py_file = os.path.join(doctype_path, f"{doctype_folder}.py")
		with open(py_file, "w") as f:
			f.write(py_content)
		
		# 3. CREATE JAVASCRIPT CONTROLLER FILE
		js_content = f'''// Copyright (c) {frappe.utils.now()[:4]}, {frappe.db.get_value("User", frappe.session.user, "full_name")} and contributors
// For license information, please see license.txt

frappe.ui.form.on("{doctype_name}", {{
	refresh(frm) {{
		// Called when form is refreshed
		if (frm.doc.__islocal) {{
			// Document is new
		}} else {{
			// Document exists
		}}
	}},
	
	validate(frm) {{
		// Called before document is saved (client-side validation)
	}},
	
	onload(frm) {{
		// Called when form is loaded
	}},
	
	// Field-specific events
	// Example: fieldname: function(frm) {{ }}
}});
'''
		
		js_file = os.path.join(doctype_path, f"{doctype_folder}.js")
		with open(js_file, "w") as f:
			f.write(js_content)
		
		# 4. CREATE __init__.py
		init_file = os.path.join(doctype_path, "__init__.py")
		with open(init_file, "w") as f:
			f.write("")
		
		# 5. CREATE TEST FILE
		test_content = f'''# Copyright (c) {frappe.utils.now()[:4]}, {frappe.db.get_value("User", frappe.session.user, "full_name")} and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTest{class_name}(UnitTestCase):
	"""
	Unit tests for {doctype_name}.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTest{class_name}(IntegrationTestCase):
	"""
	Integration tests for {doctype_name}.
	Use this class for testing interactions with the database.
	"""

	def setUp(self):
		"""Set up test data before each test."""
		pass
	
	def tearDown(self):
		"""Clean up test data after each test."""
		pass
	
	def test_{frappe.scrub(doctype_name)}_creation(self):
		"""Test creating a new {doctype_name}."""
		# Create test document
		doc = frappe.get_doc({{
			"doctype": "{doctype_name}",
			# Add required fields here
		}})
		doc.insert()
		
		# Assertions
		self.assertEqual(doc.doctype, "{doctype_name}")
		self.assertIsNotNone(doc.name)
		
		# Clean up
		doc.delete()
'''
		
		test_file = os.path.join(doctype_path, f"test_{doctype_folder}.py")
		with open(test_file, "w") as f:
			f.write(test_content)
		
		# 6. INSERT DOCTYPE INTO DATABASE
		# Check if DocType already exists
		if frappe.db.exists("DocType", doctype_name):
			return {
				"success": False,
				"error": f"DocType '{doctype_name}' already exists. Use update or choose a different name."
			}
		
		doc = frappe.get_doc(json_data)
		doc.insert(ignore_permissions=True)
		
		# Clear cache to ensure new DocType is recognized
		frappe.clear_cache(doctype=doctype_name)
		frappe.db.commit()
		
		return {
			"success": True,
			"message": f"DocType '{doctype_name}' created successfully in {app_name}",
			"doctype": doctype_name,
			"app": app_name,
			"module": module,
			"files_created": {
				"json": json_file,
				"python": py_file,
				"javascript": js_file,
				"test": test_file,
				"init": init_file
			},
			"doctype_path": doctype_path,
			"next_steps": [
				f"Restart bench to load the new DocType",
				f"Navigate to {doctype_name} list to start using it",
				f"Customize fields and add business logic in {py_file}",
				f"Add client-side interactions in {js_file}",
				f"Write tests in {test_file}"
			]
		}
		
	except Exception as e:
		frappe.log_error(f"DocType Creation Error: {str(e)}", "Nexr MCP - create_doctype")
		frappe.db.rollback()
		return {
			"success": False,
			"error": str(e),
			"traceback": frappe.get_traceback()
		}


# ============================================================================
# DOCUMENT CRUD OPERATIONS
# ============================================================================

@mcp.tool()
def create_document(doctype: str, data: Dict[str, Any]) -> Dict[str, Any]:
	"""Create a new document in any DocType.
	
	Works across all installed Frappe apps (frappe, erpnext, hrms, healthcare, etc.).
	Respects user permissions and validates data according to DocType rules.
	
	Args:
		doctype: Name of the DocType (e.g., 'Employee', 'Sales Order', 'Patient')
		data: Dictionary of field values. Must include all required fields.
	
	Returns:
		dict: Created document data with name and success status
	"""
	try:
		# Validate DocType exists
		if not frappe.db.exists("DocType", doctype):
			return {
				"success": False,
				"error": f"DocType '{doctype}' does not exist"
			}
		
		# Create document
		doc = frappe.get_doc({
			"doctype": doctype,
			**data
		})
		
		# Insert with validation
		doc.insert()
		frappe.db.commit()
		
		return {
			"success": True,
			"message": f"{doctype} '{doc.name}' created successfully",
			"name": doc.name,
			"data": doc.as_dict()
		}
		
	except frappe.exceptions.DuplicateEntryError as e:
		frappe.db.rollback()
		return {
			"success": False,
			"error": f"Duplicate entry: {str(e)}"
		}
	except frappe.exceptions.MandatoryError as e:
		frappe.db.rollback()
		return {
			"success": False,
			"error": f"Missing required fields: {str(e)}"
		}
	except Exception as e:
		frappe.db.rollback()
		frappe.log_error(f"Document Creation Error: {str(e)}", "Nexr MCP - create_document")
		return {
			"success": False,
			"error": str(e)
		}


@mcp.tool()
def get_document(doctype: str, name: str) -> Dict[str, Any]:
	"""Get a single document by name.
	
	Retrieves complete document data including child tables and linked documents.
	
	Args:
		doctype: Name of the DocType
		name: Document name/ID
	
	Returns:
		dict: Complete document data
	"""
	try:
		# Check if document exists
		if not frappe.db.exists(doctype, name):
			return {
				"success": False,
				"error": f"{doctype} '{name}' does not exist"
			}
		
		# Get document
		doc = frappe.get_doc(doctype, name)
		
		return {
			"success": True,
			"doctype": doctype,
			"name": name,
			"data": doc.as_dict()
		}
		
	except frappe.exceptions.PermissionError:
		return {
			"success": False,
			"error": f"No permission to read {doctype} '{name}'"
		}
	except Exception as e:
		frappe.log_error(f"Get Document Error: {str(e)}", "Nexr MCP - get_document")
		return {
			"success": False,
			"error": str(e)
		}


@mcp.tool()
def get_documents(
	doctype: str,
	filters: Optional[Dict[str, Any]] = None,
	fields: Optional[List[str]] = None,
	limit: int = 20,
	order_by: str = "modified desc",
	start: int = 0
) -> Dict[str, Any]:
	"""Get list of documents with filtering, sorting, and pagination.
	
	Supports complex filtering with operators like >, <, >=, <=, !=, like, in, not in.
	
	Args:
		doctype: Name of the DocType
		filters: Dictionary of filters
		fields: List of fields to fetch. Use ["*"] or None for all fields
		limit: Maximum number of records to return (default: 20, max: 500)
		order_by: Sort order (e.g., "modified desc", "name asc")
		start: Starting index for pagination (default: 0)
	
	Returns:
		dict: List of documents matching the criteria
	"""
	try:
		# Validate limit
		if limit > 500:
			limit = 500
		
		# Default fields
		if not fields or fields == ["*"]:
			fields = ["*"]
		
		# Get documents
		docs = frappe.get_all(
			doctype,
			filters=filters or {},
			fields=fields,
			limit_page_length=limit,
			limit_start=start,
			order_by=order_by
		)
		
		# Get total count
		total_count = frappe.db.count(doctype, filters=filters or {})
		
		return {
			"success": True,
			"doctype": doctype,
			"count": len(docs),
			"total": total_count,
			"has_more": (start + len(docs)) < total_count,
			"data": docs
		}
		
	except Exception as e:
		frappe.log_error(f"Get Documents Error: {str(e)}", "Nexr MCP - get_documents")
		return {
			"success": False,
			"error": str(e)
		}


@mcp.tool()
def update_document(doctype: str, name: str, data: Dict[str, Any]) -> Dict[str, Any]:
	"""Update an existing document.
	
	Can update partial or complete document data. Validates changes and runs
	document hooks (validate, before_save, on_update).
	
	Args:
		doctype: Name of the DocType
		name: Document name/ID
		data: Dictionary of fields to update
	
	Returns:
		dict: Updated document data
	"""
	try:
		# Check if document exists
		if not frappe.db.exists(doctype, name):
			return {
				"success": False,
				"error": f"{doctype} '{name}' does not exist"
			}
		
		# Get and update document
		doc = frappe.get_doc(doctype, name)
		doc.update(data)
		doc.save()
		frappe.db.commit()
		
		return {
			"success": True,
			"message": f"{doctype} '{name}' updated successfully",
			"name": doc.name,
			"data": doc.as_dict()
		}
		
	except frappe.exceptions.PermissionError:
		frappe.db.rollback()
		return {
			"success": False,
			"error": f"No permission to update {doctype} '{name}'"
		}
	except Exception as e:
		frappe.db.rollback()
		frappe.log_error(f"Update Document Error: {str(e)}", "Nexr MCP - update_document")
		return {
			"success": False,
			"error": str(e)
		}


@mcp.tool()
def delete_document(doctype: str, name: str, force: bool = False) -> Dict[str, Any]:
	"""Delete a document.
	
	Runs document hooks (on_trash) and validates dependencies before deletion.
	
	Args:
		doctype: Name of the DocType
		name: Document name/ID
		force: Force delete even if there are linked documents (use with caution)
	
	Returns:
		dict: Deletion status
	"""
	try:
		# Check if document exists
		if not frappe.db.exists(doctype, name):
			return {
				"success": False,
				"error": f"{doctype} '{name}' does not exist"
			}
		
		# Delete document
		frappe.delete_doc(doctype, name, force=force)
		frappe.db.commit()
		
		return {
			"success": True,
			"message": f"{doctype} '{name}' deleted successfully"
		}
		
	except frappe.exceptions.LinkExistsError as e:
		frappe.db.rollback()
		return {
			"success": False,
			"error": f"Cannot delete: {str(e)}. Use force=True to override (use with caution)"
		}
	except frappe.exceptions.PermissionError:
		frappe.db.rollback()
		return {
			"success": False,
			"error": f"No permission to delete {doctype} '{name}'"
		}
	except Exception as e:
		frappe.db.rollback()
		frappe.log_error(f"Delete Document Error: {str(e)}", "Nexr MCP - delete_document")
		return {
			"success": False,
			"error": str(e)
		}


# ============================================================================
# SCHEMA INTROSPECTION
# ============================================================================

@mcp.tool()
def get_doctype_schema(doctype: str, with_permissions: bool = True) -> Dict[str, Any]:
	"""Get complete schema/meta information for a DocType.
	
	Retrieves all metadata including fields, permissions, links, and properties.
	
	Args:
		doctype: Name of the DocType
		with_permissions: Include permission details (default: True)
	
	Returns:
		dict: Complete DocType metadata
	"""
	try:
		# Get meta
		meta = frappe.get_meta(doctype)
		
		# Build field information
		fields = []
		for f in meta.fields:
			field_info = {
				"fieldname": f.fieldname,
				"label": f.label,
				"fieldtype": f.fieldtype,
				"options": f.options,
				"reqd": bool(f.reqd),
				"read_only": bool(f.read_only),
				"hidden": bool(f.hidden),
				"default": f.default,
				"description": f.description,
				"in_list_view": bool(f.in_list_view),
				"in_standard_filter": bool(f.in_standard_filter),
				"length": f.length
			}
			fields.append(field_info)
		
		# Build schema
		schema = {
			"success": True,
			"doctype": doctype,
			"data": {
				"name": meta.name,
				"module": meta.module,
				"app": frappe.local.module_app.get(frappe.scrub(meta.module)),
				"is_submittable": bool(meta.is_submittable),
				"is_child": bool(meta.istable),
				"track_changes": bool(meta.track_changes),
				"editable_grid": bool(meta.editable_grid),
				"title_field": meta.title_field,
				"naming_rule": meta.naming_rule,
				"autoname": meta.autoname,
				"description": meta.description,
				"fields": fields,
				"links": [
					{
						"link_doctype": link.options,
						"link_fieldname": link.fieldname,
						"label": link.label,
						"fieldtype": link.fieldtype,
						"reqd": bool(link.reqd),
						"read_only": bool(link.read_only),
						"hidden": bool(link.hidden),
						"description": link.description,
						"search_indexed": bool(link.search_indexed),
						"in_list_view": bool(link.in_list_view),
						"in_standard_filter": bool(link.in_standard_filter),
						"fetch_from": link.fetch_from
					}
					for link in meta.get_link_fields()
				]
			}
		}
		
		# Add permissions if requested
		if with_permissions:
			schema["data"]["permissions"] = [
				{
					"role": p.role,
					"read": bool(p.read),
					"write": bool(p.write),
					"create": bool(p.create),
					"delete": bool(p.delete),
					"submit": bool(p.submit),
					"cancel": bool(p.cancel),
					"amend": bool(p.amend)
				}
				for p in meta.permissions
			]
		
		return schema
		
	except Exception as e:
		frappe.log_error(f"Get Schema Error: {str(e)}", "Nexr MCP - get_doctype_schema")
		return {
			"success": False,
			"error": str(e)
		}


@mcp.tool()
def get_all_doctypes(app_name: Optional[str] = None, include_child: bool = False) -> Dict[str, Any]:
	"""Get list of all DocTypes, optionally filtered by app.
	
	Args:
		app_name: Optional app name to filter (e.g., 'hrms', 'erpnext', 'healthcare')
		include_child: Include child DocTypes (table fields) in results
	
	Returns:
		dict: List of DocTypes with metadata
	"""
	try:
		filters = {}
		
		# Filter by app
		if app_name:
			modules = frappe.get_all(
				"Module Def",
				filters={"app_name": app_name},
				pluck="name"
			)
			if not modules:
				return {
					"success": False,
					"error": f"No modules found for app '{app_name}'"
				}
			filters["module"] = ["in", modules]
		
		# Filter out child tables if requested
		if not include_child:
			filters["istable"] = 0
		
		# Get doctypes
		doctypes = frappe.get_all(
			"DocType",
			filters=filters,
			fields=["name", "module", "is_submittable", "istable", "track_changes"],
			order_by="name"
		)
		
		# Add app name to each doctype
		for dt in doctypes:
			dt["app"] = frappe.scrub(dt.get("module"))
			dt["is_child"] = bool(dt.get("istable"))
			dt.pop("istable", None)
		
		return {
			"success": True,
			"app_filter": app_name,
			"count": len(doctypes),
			"data": doctypes
		}
		
	except Exception as e:
		frappe.log_error(f"Get All DocTypes Error: {str(e)}", "Nexr MCP - get_all_doctypes")
		return {
			"success": False,
			"error": str(e)
		}


@mcp.tool()
def get_field_options(doctype: str, fieldname: str) -> Dict[str, Any]:
	"""Get options for Link or Select fields.
	
	For Link fields, returns list of available documents.
	For Select fields, returns list of valid options.
	
	Args:
		doctype: Name of the DocType
		fieldname: Name of the field
	
	Returns:
		dict: Field options
	"""
	try:
		meta = frappe.get_meta(doctype)
		field = meta.get_field(fieldname)
		
		if not field:
			return {
				"success": False,
				"error": f"Field '{fieldname}' not found in {doctype}"
			}
		
		result = {
			"success": True,
			"doctype": doctype,
			"fieldname": fieldname,
			"fieldtype": field.fieldtype,
			"label": field.label
		}
		
		if field.fieldtype == "Link":
			# Get linked documents
			link_doctype = field.options
			docs = frappe.get_all(
				link_doctype,
				fields=["name"],
				limit=100
			)
			result["options"] = [d.name for d in docs]
			result["link_doctype"] = link_doctype
			
		elif field.fieldtype == "Select":
			# Get select options
			options = field.options.split("\n") if field.options else []
			result["options"] = [opt.strip() for opt in options if opt.strip()]
		
		else:
			result["message"] = f"Field '{fieldname}' is type '{field.fieldtype}' which doesn't have predefined options"
		
		return result
		
	except Exception as e:
		frappe.log_error(f"Get Field Options Error: {str(e)}", "Nexr MCP - get_field_options")
		return {
			"success": False,
			"error": str(e)
		}


# ============================================================================
# UTILITY TOOLS
# ============================================================================

@mcp.tool()
def get_installed_apps() -> Dict[str, Any]:
	"""Get list of all installed apps in the current site with versions.
	
	Returns:
		dict: List of installed apps with their versions
	"""
	try:
		apps = frappe.get_installed_apps()
		app_info = []
		
		for app in apps:
			try:
				version = frappe.get_attr(app + ".__version__")
			except:
				version = "Unknown"
			
			# Get app title
			try:
				hooks = frappe.get_hooks(app_name=app)
				title = hooks.get("app_title", [app])[0] if hooks.get("app_title") else app
			except:
				title = app
			
			app_info.append({
				"name": app,
				"title": title,
				"version": version
			})
		
		return {
			"success": True,
			"site": frappe.local.site,
			"count": len(app_info),
			"data": app_info
		}
		
	except Exception as e:
		frappe.log_error(f"Get Installed Apps Error: {str(e)}", "Nexr MCP - get_installed_apps")
		return {
			"success": False,
			"error": str(e)
		}


@mcp.tool()
def run_bench_command(command: str, cwd: Optional[str] = None, timeout: int = 300) -> Dict[str, Any]:
	"""Execute a bench command.
	
	Security note: Only whitelisted commands are allowed for safety.
	
	Args:
		command: Bench command to run (e.g., "migrate", "clear-cache", "build")
		cwd: Working directory (optional, defaults to bench path)
		timeout: Command timeout in seconds (default: 300)
	
	Returns:
		dict: Command output and status
	"""
	import subprocess
	
	# Whitelist of allowed commands for security
	allowed_commands = [
		"migrate",
		"clear-cache",
		"clear-website-cache",
		"build",
		"restart",
		"version",
		"--version"
	]
	
	try:
		# Validate command
		base_command = command.split()[0] if " " in command else command
		if base_command not in allowed_commands:
			return {
				"success": False,
				"error": f"Command '{base_command}' not allowed. Allowed commands: {', '.join(allowed_commands)}"
			}
		
		# Get bench path
		bench_path = frappe.utils.get_bench_path()
		if cwd is None:
			cwd = bench_path
		
		# Build full command
		full_command = f"bench {command}"
		
		# Execute
		result = subprocess.run(
			full_command,
			shell=True,
			cwd=cwd,
			capture_output=True,
			text=True,
			timeout=timeout
		)
		
		return {
			"success": result.returncode == 0,
			"command": full_command,
			"output": result.stdout,
			"error": result.stderr,
			"return_code": result.returncode
		}
		
	except subprocess.TimeoutExpired:
		return {
			"success": False,
			"error": f"Command timed out after {timeout} seconds"
		}
	except Exception as e:
		frappe.log_error(f"Bench Command Error: {str(e)}", "Nexr MCP - run_bench_command")
		return {
			"success": False,
			"error": str(e)
		}


@mcp.tool()
def health_check() -> Dict[str, Any]:
	"""Perform a health check of the MCP server and Frappe site.
	
	Returns system information, database status, and cache status.
	
	Returns:
		dict: Health check results
	"""
	try:
		# Get basic info
		result = {
			"success": True,
			"status": "healthy",
			"site": frappe.local.site,
			"frappe_version": frappe.__version__,
			"user": frappe.session.user,
			"timestamp": frappe.utils.now(),
			"database": {
				"connected": True,
				"type": frappe.conf.db_type or "mariadb"
			},
			"cache": {
				"enabled": bool(frappe.cache())
			},
			"installed_apps": len(frappe.get_installed_apps())
		}
		
		# Test database connection
		try:
			frappe.db.sql("SELECT 1")
		except:
			result["database"]["connected"] = False
			result["status"] = "unhealthy"
		
		return result
		
	except Exception as e:
		return {
			"success": False,
			"status": "unhealthy",
			"error": str(e)
		}


# ============================================================================
# MCP ENDPOINT REGISTRATION
# ============================================================================

@mcp.register()
def handle_mcp():
	"""Entry point for MCP requests.
	
	This function serves as the HTTP endpoint for all MCP tool calls.
	The endpoint is available at: /api/method/nexr.mcp.handle_mcp
	
	All registered tools are automatically available through this endpoint.
	"""
	# Import any additional tool modules here if they exist
	pass
