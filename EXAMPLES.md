# Nexr Usage Examples

Comprehensive examples for using Nexr MCP tools with your AI assistant.

## Table of Contents

- [DocType Creation](#doctype-creation)
- [Document Operations](#document-operations)
- [Data Queries](#data-queries)
- [Schema Introspection](#schema-introspection)
- [Bulk Operations](#bulk-operations)
- [Development Tasks](#development-tasks)
- [Advanced Patterns](#advanced-patterns)

## DocType Creation

### Basic DocType

Create a simple DocType with basic fields:

```
@copilot Using nexr-dev, create a "Book" DocType in the library_management app, 
Library module with these fields:
- book_title (Data, required)
- author (Data, required)
- isbn (Data, unique)
- publication_year (Int)
- publisher (Data)
- description (Text)
```

### DocType with Link Fields

Create a DocType with relationships:

```
@copilot Using nexr-dev, create a "Project Assignment" DocType in erpnext, 
Projects module with:
- project (Link to Project, required)
- employee (Link to Employee, required)
- role (Select: Developer, Tester, Manager, Designer)
- start_date (Date, required)
- end_date (Date)
- allocation_percentage (Percent)
- status (Select: Active, Completed, On Hold)
```

### Submittable DocType

Create a DocType that requires submission workflow:

```
@copilot Using nexr-dev, create a "Leave Request" DocType in hrms, HR module.
Fields:
- employee (Link to Employee, required)
- leave_type (Link to Leave Type, required)
- from_date (Date, required)
- to_date (Date, required)
- total_days (Float, read-only)
- reason (Text)
- approver (Link to User)
- approval_status (Select: Pending, Approved, Rejected)

Make it submittable and track changes.
```

### Child Table DocType

Create a child table for use in other DocTypes:

```
@copilot Using nexr-dev, create a "Order Item" child DocType in erpnext, 
Selling module with:
- item_code (Link to Item, required)
- item_name (Data, read-only)
- quantity (Float, required)
- rate (Currency, required)
- amount (Currency, read-only)
- delivery_date (Date)

Make it a child table.
```

### DocType with Computed Fields

Create a DocType with calculated fields:

```
@copilot Using nexr-dev, create a "Time Log" DocType in projects app with:
- task (Link to Task, required)
- employee (Link to Employee, required)
- start_time (Datetime, required)
- end_time (Datetime, required)
- hours (Float, computed from start_time and end_time)
- hourly_rate (Currency)
- total_cost (Currency, computed)
- billable (Check)
```

## Document Operations

### Create Documents

#### Simple Document Creation

```
@copilot Using nexr-dev, create a new Customer:
- customer_name: "Acme Corporation"
- customer_group: "Commercial"
- territory: "United States"
- email_id: "contact@acme.com"
```

#### Document with Child Table

```
@copilot Using nexr-dev, create a new Sales Order with:
- customer: "CUST-00001"
- delivery_date: "2024-02-15"
- items:
  - item_code: "ITEM-001", qty: 5, rate: 100
  - item_code: "ITEM-002", qty: 3, rate: 250
```

### Read Documents

#### Get Single Document

```
@copilot Using nexr-dev, show me the details of Sales Invoice "SINV-2024-00123"
```

#### Get Multiple Documents

```
@copilot Using nexr-dev, get all active Employees in the Sales department
```

### Update Documents

#### Simple Update

```
@copilot Using nexr-dev, update Task "TASK-2024-001" to set status as "Completed"
```

#### Bulk Update

```
@copilot Using nexr-dev, update all pending Purchase Orders from supplier 
"SUP-00123" to add a note "Delivery delayed by 1 week"
```

### Delete Documents

```
@copilot Using nexr-dev, delete the draft Sales Order "SO-2024-00456"
```

## Data Queries

### Filtering

#### Simple Filter

```
@copilot Using nexr-dev, get all Sales Orders with status "To Deliver"
```

#### Date Range Filter

```
@copilot Using nexr-dev, show me all Invoices created in January 2024
```

#### Multiple Filters

```
@copilot Using nexr-dev, get all Items where:
- item_group is "Electronics"
- stock_qty is greater than 100
- disabled is 0
```

### Sorting and Limiting

```
@copilot Using nexr-dev, get the top 10 Customers by outstanding amount, 
sorted descending
```

### Field Selection

```
@copilot Using nexr-dev, list all Employees showing only: name, employee_name, 
department, and designation
```

### Aggregations

```
@copilot Using nexr-dev, calculate total revenue from Sales Orders this month
```

```
@copilot Using nexr-dev, count how many open Issues are assigned to each user
```

## Schema Introspection

### Get DocType Schema

```
@copilot Using nexr-dev, show me the complete schema for Sales Invoice doctype
```

### List All DocTypes

```
@copilot Using nexr-dev, list all DocTypes in the healthcare app
```

### Get Field Options

```
@copilot Using nexr-dev, what are the available options for the "status" field 
in the Lead doctype?
```

### Analyze Relationships

```
@copilot Using nexr-dev, show me all child tables for the Purchase Order doctype
```

## Bulk Operations

### Mass Creation

```
@copilot Using nexr-dev, create 5 test Employees with the naming pattern:
- employee_name: "Test Employee 1" through "Test Employee 5"
- department: "Operations"
- designation: "Software Developer"
- status: "Active"
```

### Conditional Updates

```
@copilot Using nexr-dev, for all Tasks in Project "PRO-2024-001":
- If status is "Open" and expected_end_date is before today, set priority to "High"
- Add a comment "Priority escalated due to overdue status"
```

### Data Migration

```
@copilot Using nexr-dev, copy all Customers from customer_group "Retail" 
and create corresponding Leads for follow-up
```

## Development Tasks

### Run Migrations

```
@copilot Using nexr-dev, run database migrations
```

### Clear Cache

```
@copilot Using nexr-dev, clear the cache and rebuild
```

### Get Installed Apps

```
@copilot Using nexr-dev, list all installed apps with their versions
```

### Build Assets

```
@copilot Using nexr-dev, run bench build
```

## Advanced Patterns

### Multi-App DocType Creation

Create related DocTypes across different apps:

```
@copilot Using nexr-dev, I need to set up a training management system:

1. Create "Training Course" in hrms, HR module:
   - course_name (Data, required)
   - duration_hours (Float)
   - trainer (Link to Employee)
   - max_participants (Int)
   - description (Text Editor)

2. Create "Training Session" in hrms, HR module:
   - course (Link to Training Course, required)
   - session_date (Date, required)
   - start_time (Time)
   - end_time (Time)
   - venue (Data)
   - participants (Table with Child DocType)
   
3. Create "Training Participant" child table in hrms:
   - employee (Link to Employee, required)
   - attendance (Select: Present, Absent, Partial)
   - feedback_score (Int)
   - certificate_issued (Check)
```

### Complex Data Analysis

```
@copilot Using nexr-dev, analyze sales performance:

1. Get all Sales Invoices from last quarter
2. Group by customer
3. Calculate total revenue, average order value, and order count
4. Show top 20 customers
5. Include their outstanding amount
```

### Workflow Automation

```
@copilot Using nexr-dev, automate the invoice approval workflow:

1. Get all draft Sales Invoices where grand_total > 10000
2. For each invoice:
   - Add a comment requesting approval
   - Send email to finance manager
   - Update custom field "approval_requested" to today's date
```

### Data Validation

```
@copilot Using nexr-dev, validate data integrity:

1. Check all Sales Orders for:
   - Missing delivery dates
   - Items with zero rate
   - Orders older than 30 days still in draft
   
2. Create a report of issues found
3. Update problematic orders with a warning comment
```

### Custom Reporting

```
@copilot Using nexr-dev, create a monthly sales summary:

1. Get all submitted Sales Orders from current month
2. Group by territory and customer_group
3. Calculate:
   - Total orders
   - Total revenue
   - Average order value
   - Top 5 items by quantity
4. Format as a readable report
```

### Integration Testing

```
@copilot Using nexr-dev, test the order-to-invoice workflow:

1. Create a test Customer "Test Co"
2. Create a test Item "Test Product"
3. Create a Sales Order
4. Submit the Sales Order
5. Create a Delivery Note from the Sales Order
6. Submit the Delivery Note
7. Create a Sales Invoice from the Delivery Note
8. Verify all documents are linked correctly
```

## Real-World Scenarios

### Scenario 1: New Feature Development

**Goal**: Add a customer feedback system

```
@copilot Using nexr-dev, help me build a customer feedback system:

1. Create "Customer Feedback" DocType in erpnext, CRM module:
   - customer (Link to Customer, required)
   - feedback_date (Date, default: today)
   - interaction_type (Select: Sales Call, Support Ticket, Product Review)
   - rating (Select: 1-Poor, 2-Fair, 3-Good, 4-Very Good, 5-Excellent)
   - comments (Text Editor)
   - follow_up_required (Check)
   - assigned_to (Link to User)
   - is_submittable: Yes

2. Create 5 sample feedback entries for testing

3. Query all feedback with rating < 3 for follow-up
```

### Scenario 2: Data Cleanup

**Goal**: Clean up duplicate and invalid data

```
@copilot Using nexr-dev, help me clean up customer data:

1. Find all Customers with duplicate email addresses
2. Find Customers with invalid phone number formats
3. Find Customers with no territory assigned
4. Generate a report of issues
5. For Customers with no territory, assign default territory "Rest of World"
```

### Scenario 3: Migration from Spreadsheet

**Goal**: Import data from external source

```
@copilot Using nexr-dev, I have product data to import:

For each of these items, create an Item in ERPNext:
1. "Laptop Dell XPS 13" - Electronics - $1200 - Stock: 50
2. "Mouse Logitech MX" - Accessories - $80 - Stock: 200
3. "Monitor LG 27inch" - Electronics - $350 - Stock: 75

Set appropriate item_code, item_name, item_group, standard_rate, and opening_stock
```

## Tips for Effective Usage

### 1. Be Specific
❌ "Create a DocType"
✅ "Create a 'Purchase Request' DocType in erpnext, Buying module with fields for item, quantity, and requested_by"

### 2. Use Context
❌ "Get documents"
✅ "Get all submitted Purchase Orders from last week that haven't been billed yet"

### 3. Chain Operations
✅ "Create a Customer 'ABC Inc', then create a Sales Order for them with item ITEM-001"

### 4. Request Validation
✅ "Create the DocType and then show me its schema to verify"

### 5. Ask for Explanations
✅ "Show me the Sales Invoice schema and explain what the posting_date field does"

## Need More Help?

- [Full Documentation](README.md)
- [Quick Start Guide](QUICKSTART.md)
- [GitHub Issues](https://github.com/av-dev2/nexr/issues)

---

**Happy Building with Nexr!** 🚀
