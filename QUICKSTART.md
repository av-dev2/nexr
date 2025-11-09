# Nexr Quick Start Guide

Get up and running with Nexr in 5 minutes!

## Step 1: Install Nexr (1 min)

```bash
cd /path/to/your/bench
bench get-app https://github.com/av-dev2/nexr
bench --site your-site.local install-app nexr
```

**That's it!** The `frappe-mcp` dependency is automatically installed with the app.

## Step 2: Generate API Credentials (2 min)

### Using Bench Console (Recommended)

```bash
bench --site your-site.local console
```

In the Python console:
```python
user = frappe.get_doc("User", "your-email@example.com")
user.generate_keys()
frappe.db.commit()

# Display your credentials
api_key = user.api_key
api_secret = frappe.utils.password.get_decrypted_password("User", user.name, "api_secret")
print(f"\nAPI Key: {api_key}")
print(f"API Secret: {api_secret}")
```

**Save these credentials!** You'll need them in the next step.

### Alternative: Using Web UI

1. Login to your Frappe site
2. Click your profile (top right)
3. Select "API Access"
4. Click "Generate Keys"
5. Copy the API Key and API Secret

## Step 3: Configure VS Code (2 min)

### For GitHub Copilot

1. Open VS Code settings:
   - **Linux**: `~/.config/Code/User/settings.json`
   - **macOS**: `~/Library/Application Support/Code/User/settings.json`
   - **Windows**: `%APPDATA%\Code\User\settings.json`

2. Add this configuration:

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

3. **Replace:**
   - `localhost:8000` → Your site URL/port
   - `YOUR_API_KEY` → Your actual API key
   - `YOUR_API_SECRET` → Your actual API secret

4. Restart VS Code

### For Claude Desktop

1. Open config file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. Add configuration:

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

3. Restart Claude Desktop

## Step 4: Test It Out! (30 seconds)

Open GitHub Copilot Chat or Claude and try:

```
@copilot Using nexr-dev, run a health check
```

Expected response:
```
✓ Server is healthy
✓ Site: your-site.local
✓ Frappe version: vX.X.X
```

## 🎉 You're Ready!

Try these commands to explore Nexr:

### List Available Apps
```
@copilot Using nexr-dev, list all installed apps
```

### View DocTypes
```
@copilot Using nexr-dev, show me all DocTypes in the erpnext app
```

### Create a DocType
```
@copilot Using nexr-dev, create a "Meeting Notes" DocType in frappe, 
with fields: title (Data), date (Date), attendees (Small Text), notes (Text Editor)
```

### Query Data
```
@copilot Using nexr-dev, get the last 5 ToDo items
```

## 🚀 Next Steps

- Read the [Full Documentation](README.md)
- Explore [Usage Examples](EXAMPLES.md)
- Check the [Changelog](CHANGELOG.md)

## 🐛 Common Issues

### "Cannot connect to MCP server"

**Solution:**
```bash
# Make sure bench is running
bench start

# Check if your site is accessible
curl http://localhost:8000
```

### "Authentication failed"

**Solution:**
- Double-check your API key and secret
- Make sure there are no extra spaces in the config
- Regenerate credentials if needed

### "Tool not available"

**Solution:**
```bash
# Verify nexr is installed
bench --site your-site.local list-apps

# If not installed:
bench --site your-site.local install-app nexr
bench restart
```

## 💡 Tips

1. **Multiple Benches**: Give each configuration a unique name (`nexr-prod`, `nexr-dev`, etc.)
2. **Security**: Use different API keys for different environments
3. **Performance**: Keep your bench updated for best results
4. **Documentation**: Use natural language - Nexr understands context!

## 📚 Learn More

- [Complete Tool Reference](README.md#-available-mcp-tools)
- [Advanced Examples](EXAMPLES.md)
- [Architecture Details](README.md#-architecture)

---

**Need help?** [Open an issue](https://github.com/av-dev2/nexr/issues) on GitHub!
