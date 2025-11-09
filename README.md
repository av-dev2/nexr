# Nexr - Frappe MCP Development Assistant

**Nexr** is a comprehensive Model Context Protocol (MCP) server that extends [frappe/mcp](https://github.com/frappe/mcp) functionality to provide powerful AI-assisted development tools for Frappe Framework applications.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![Frappe](https://img.shields.io/badge/frappe-v14%2B%20|%20v15%2B%20|%20v16%2B-orange)](https://github.com/frappe/frappe)

## 🚀 Quick Start

**New to Nexr?** Check out our [Quick Start Guide](QUICKSTART.md) to get up and running in 5 minutes!

## 🎯 Overview

Nexr enables AI assistants (like GitHub Copilot, Claude, etc.) to interact with your Frappe/ERPNext environment through standardized MCP tools. It provides complete development capabilities including DocType creation, CRUD operations, schema introspection, and more - all accessible through natural language interactions with your AI assistant.

**Compatible with Frappe v14, v15, v16+**

## ✨ Features

### 1. **DocType Creation & File Generation**
- Create DocTypes for any Frappe app (frappe, erpnext, hrms, healthcare, helpdesk, etc.)
- Automatically generates all required files:
  - `.json` - DocType definition
  - `.py` - Python controller
  - `.js` - JavaScript client-side controller
  - `test_*.py` - Unit test file
- Places files in the correct module directory structure
- Inserts DocType into database and clears cache

### 2. **Universal Document Operations**
- **Create** documents in any DocType across all installed apps
- **Read** single documents or lists with advanced filtering
- **Update** existing documents with partial or complete data
- **Delete** documents with proper error handling
- Works seamlessly across frappe, erpnext, hrms, healthcare, and all custom apps

### 3. **Schema Introspection**
- Retrieve complete DocType metadata and field definitions
- Get field options for Link and Select fields
- List all available DocTypes filtered by app
- View permissions, child tables, and relationships
- Analyze app structures and dependencies

### 4. **Development Tools**
- Execute bench commands remotely
- List installed apps and versions
- Run database migrations
- Clear cache and rebuild assets
- Health checks and version information

## 📦 Installation

### Prerequisites
- Frappe Framework (v14, v15, v16, or higher)
- Python 3.10+
- Access to a Frappe bench

### Install via Bench

```bash
cd /path/to/your/bench
bench get-app https://github.com/av-dev2/nexr
bench --site your-site.local install-app nexr
```

**Note:** The `frappe-mcp` dependency is automatically installed when you install the app - no manual pip installation needed!

### Verify Installation

```bash
# Check if nexr is installed
bench --site your-site.local list-apps

# You should see nexr in the list
```

## 🚀 Configuration

### 1. Generate API Credentials

Create API credentials in your Frappe site:

**Option A: Via Web UI**
1. Go to User profile (top right)
2. Click on "API Access"
3. Click "Generate Keys"
4. Save the API Key and API Secret

**Option B: Via Bench Console**
```bash
bench --site your-site.local console

# In the Python console:
user = frappe.get_doc("User", "your-email@example.com")
user.generate_keys()
frappe.db.commit()

# Get the credentials
api_key = user.api_key
api_secret = frappe.utils.password.get_decrypted_password("User", user.name, "api_secret")
print(f"API Key: {api_key}")
print(f"API Secret: {api_secret}")
```

### 2. Configure VS Code (GitHub Copilot)

Add to your VS Code `settings.json`:

**File Location:**
- **User Settings**: `~/.config/Code/User/settings.json` (Linux) or `~/Library/Application Support/Code/User/settings.json` (macOS)
- **Workspace Settings**: `.vscode/settings.json` (in your project)

**Configuration:**
```json
{
  "github.copilot.chat.mcpServers": {
    "nexr-dev": {
      "type": "http",
      "url": "http://localhost:8000/api/method/nexr.mcp.handle_mcp",
      "headers": {
        "Authorization": "token YOUR_API_KEY:YOUR_API_SECRET"
      }
    }
  }
}
```

**Replace:**
- `localhost:8000` with your site's URL and port
- `YOUR_API_KEY` with your actual API key
- `YOUR_API_SECRET` with your actual API secret

### 3. Configure for Multiple Benches

```json
{
  "github.copilot.chat.mcpServers": {
    "nexr-prod": {
      "type": "http",
      "url": "http://localhost:8000/api/method/nexr.mcp.handle_mcp",
      "headers": {
        "Authorization": "token KEY1:SECRET1"
      }
    },
    "nexr-dev": {
      "type": "http",
      "url": "http://localhost:8001/api/method/nexr.mcp.handle_mcp",
      "headers": {
        "Authorization": "token KEY2:SECRET2"
      }
    },
    "nexr-staging": {
      "type": "http",
      "url": "http://localhost:8002/api/method/nexr.mcp.handle_mcp",
      "headers": {
        "Authorization": "token KEY3:SECRET3"
      }
    }
  }
}
```

### 4. Configure for Docker Containers

```json
{
  "github.copilot.chat.mcpServers": {
    "nexr-docker": {
      "type": "http",
      "url": "http://localhost:8080/api/method/nexr.mcp.handle_mcp",
      "headers": {
        "Authorization": "token YOUR_API_KEY:YOUR_API_SECRET"
      }
    }
  }
}
```

### 5. Configure for Claude Desktop

Add to:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "nexr": {
      "type": "http",
      "url": "http://localhost:8000/api/method/nexr.mcp.handle_mcp",
      "headers": {
        "Authorization": "token YOUR_API_KEY:YOUR_API_SECRET"
      }
    }
  }
}
```

## 🔧 Available MCP Tools

### DocType Management

#### `create_doctype`
Create a new DocType with complete file structure.

**Parameters:**
- `app_name`: Target app (e.g., 'hrms', 'erpnext')
- `doctype_name`: Name of the DocType
- `module`: Module name (e.g., 'HR', 'Stock')
- `fields`: List of field definitions
- `is_submittable`: Make DocType submittable (default: False)
- `is_child`: Create as child table (default: False)
- `track_changes`: Enable change tracking (default: False)
- `naming_rule`: Naming strategy (default: 'autoname')

#### `get_doctype_schema`
Get complete schema and metadata for any DocType.

#### `get_all_doctypes`
List all DocTypes, optionally filtered by app.

### Document Operations

#### `create_document`
Create a new document in any DocType.

#### `get_document`
Retrieve a single document by name.

#### `get_documents`
Get list of documents with filtering and sorting.

#### `update_document`
Update an existing document.

#### `delete_document`
Delete a document.

### Schema Tools

#### `get_field_options`
Get options for Link or Select fields.

### Utility Tools

#### `get_installed_apps`
List all installed apps with versions.

#### `run_bench_command`
Execute bench commands (migrate, clear-cache, build, etc.).

#### `health_check`
Check server and site health status.

## 💡 Usage Examples

### Creating a Custom DocType

```
@copilot Using nexr-dev, create a "Project Task" DocType in the erpnext app, 
Projects module. It should have:
- project (Link to Project, required)
- task_name (Data, required)
- assigned_to (Link to User)
- start_date (Date)
- end_date (Date)
- status (Select: Open, In Progress, Completed, Cancelled)
- priority (Select: Low, Medium, High)
- description (Text Editor)

Make it submittable and track changes.
```

### Querying Data

```
@copilot Using nexr-dev, get all Sales Orders from last month with status "To Deliver"
```

```
@copilot Using nexr-dev, show me the top 10 customers by total revenue
```

### Bulk Operations

```
@copilot Using nexr-dev, update all open Tasks in project "PRO-2024-001" 
to set priority as "High"
```

### Schema Analysis

```
@copilot Using nexr-dev, what fields are available in the Sales Invoice doctype?
```

```
@copilot Using nexr-dev, show me all doctypes in the healthcare app
```

## 🏗️ Architecture

Nexr is built on top of the official [frappe/mcp](https://github.com/frappe/mcp) library, which provides:
- Streamable HTTP transport for MCP
- Tool registration and management
- JSON-RPC request handling
- OAuth2 authentication support

Nexr adds:
- File system operations for DocType creation
- Advanced querying and filtering
- Bench command execution
- Comprehensive error handling
- Support for Frappe v14, v15, v16+

## 🔒 Security

- Uses Frappe's built-in API key authentication
- Respects user permissions and role-based access
- All operations are logged in Frappe's audit trail
- No direct database access - uses Frappe ORM
- Supports OAuth2 for enhanced security
- Whitelisted bench commands only

## 🧪 Testing

```bash
# Run unit tests
bench --site your-site.local run-tests --app nexr

# Run specific test
bench --site your-site.local run-tests --test nexr.tests.test_mcp_tools
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linters
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/nexr
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

## 📚 Documentation

- [Quick Start Guide](QUICKSTART.md) - Get started in 5 minutes
- [Usage Examples](EXAMPLES.md) - Practical examples and patterns
- [Changelog](CHANGELOG.md) - Version history and updates

## 🆚 Version Compatibility

| Nexr Version | Frappe v14 | Frappe v15 | Frappe v16 |
|--------------|------------|------------|------------|
| 1.0.0+       | ✅         | ✅         | ✅         |

## 🐛 Troubleshooting

### Issue: "Cannot connect to MCP server"

**Solution:**
1. Verify your bench is running: `bench start`
2. Check the URL and port in your config
3. Test with curl to verify the endpoint is accessible

### Issue: "Authentication failed"

**Solution:**
1. Regenerate API credentials
2. Verify you copied the full API key and secret
3. Check for extra spaces in the Authorization header

### Issue: "Tool not found"

**Solution:**
1. Verify Nexr app is installed: `bench list-apps`
2. Restart bench: `bench restart`
3. Check Nexr is installed on the site: `bench --site your-site.local list-apps`

### Issue: "frappe_mcp import error"

**Solution:**
The `frappe-mcp` package is automatically installed with Nexr. If you see this error:
```bash
bench --site your-site.local migrate
bench restart
```

## 🙏 Acknowledgments

- Built on top of [frappe/mcp](https://github.com/frappe/mcp)
- Inspired by the Frappe/ERPNext community
- Powered by the Model Context Protocol

## 📝 License

MIT License - see LICENSE file for details

## 🔗 Links

- [GitHub Repository](https://github.com/av-dev2/nexr)
- [Issue Tracker](https://github.com/av-dev2/nexr/issues)
- [Frappe Framework](https://github.com/frappe/frappe)
- [Model Context Protocol](https://modelcontextprotocol.io)

---

**Made with ❤️ for the Frappe community**
