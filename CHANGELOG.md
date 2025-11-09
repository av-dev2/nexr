# Changelog

All notable changes to Nexr will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Enhanced error reporting with suggested fixes
- Batch operations for bulk document creation
- Custom script execution support
- Report generation tools
- Database query builder
- Webhook management
- Email template tools

## [1.0.0] - 2025-01-XX

### Added
- Initial release of Nexr
- Complete MCP server implementation using frappe-mcp
- 12 comprehensive MCP tools for Frappe development
- DocType creation with automatic file generation (.json, .py, .js, test)
- Full CRUD operations for all DocTypes across all apps
- Schema introspection and metadata retrieval
- Support for Frappe v14, v15, v16+
- Streamable HTTP transport over MCP protocol
- API key/secret authentication via Frappe's built-in system
- Multi-bench and Docker container support
- Comprehensive documentation and examples
- Quick start guide for 5-minute setup
- Pre-commit hooks for code quality

#### MCP Tools Included

**DocType Management:**
- `create_doctype` - Create DocTypes with complete file structure
- `get_doctype_schema` - Retrieve DocType metadata and fields
- `get_all_doctypes` - List all DocTypes filtered by app

**Document Operations:**
- `create_document` - Create new documents
- `get_document` - Retrieve single document
- `get_documents` - Query multiple documents with filters
- `update_document` - Update existing documents
- `delete_document` - Delete documents

**Schema Tools:**
- `get_field_options` - Get Link/Select field options

**Utilities:**
- `get_installed_apps` - List installed apps and versions
- `run_bench_command` - Execute bench commands
- `health_check` - Server and site status

### Technical Details
- Built on frappe-mcp >= 0.1.0
- Python 3.10+ compatibility
- Modern packaging with pyproject.toml
- Automatic dependency installation
- Whitelist-based security for bench commands
- Comprehensive error handling
- Permission-aware operations

### Documentation
- README.md with complete setup guide
- QUICKSTART.md for rapid onboarding
- EXAMPLES.md with practical use cases
- Inline code documentation
- Configuration examples for VS Code and Claude Desktop

## Version Support Matrix

| Nexr Version | Frappe v14 | Frappe v15 | Frappe v16 | Python | frappe-mcp |
|--------------|------------|------------|------------|--------|------------|
| 1.0.0        | ✅         | ✅         | ✅         | 3.10+  | 0.1.0+     |

## Migration Guide

### From Manual frappe-mcp Installation

If you were previously using frappe-mcp with manual installation:

1. **Before**: Manual pip install in each bench
   ```bash
   bench pip install frappe-mcp
   ```

2. **After**: Automatic with Nexr installation
   ```bash
   bench get-app https://github.com/av-dev2/nexr
   bench --site your-site.local install-app nexr
   # frappe-mcp is automatically installed!
   ```

3. **Update Configuration**: Change endpoint in your MCP client
   ```json
   // Before
   "url": "http://localhost:8000/api/method/frappe_mcp.handle_request"
   
   // After
   "url": "http://localhost:8000/api/method/nexr.mcp.handle_mcp"
   ```

## Breaking Changes

None in v1.0.0 (initial release)

## Security Updates

None in v1.0.0 (initial release)

## Known Issues

None reported yet. Please [report issues](https://github.com/av-dev2/nexr/issues) if you find any.

## Upgrade Instructions

### To 1.0.0 (Initial Installation)

```bash
# Get the app
cd /path/to/your/bench
bench get-app https://github.com/av-dev2/nexr

# Install on your site
bench --site your-site.local install-app nexr

# Restart bench
bench restart

# migrate site
bench --site your-site.local migrate
```

## Deprecation Notices

None in v1.0.0

## Contributors

- Initial development and design
- Built on frappe-mcp by the Frappe team
- Inspired by the Frappe/ERPNext community

## Links

- [GitHub Repository](https://github.com/av-dev2/nexr)
- [Issue Tracker](https://github.com/av-dev2/nexr/issues)
- [Documentation](README.md)
- [frappe-mcp](https://github.com/frappe/mcp)

---

**Format Note**: We follow [Keep a Changelog](https://keepachangelog.com/) format:
- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for bug fixes
- **Security** for vulnerability fixes
