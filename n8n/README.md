# n8n - Open-Source Workflow Automation Tool

**n8n** is an open-source workflow automation platform that empowers users to automate repetitive tasks and integrate various applications, services, and APIs without writing complex code. With its visual interface, users can create workflows by simply dragging and dropping pre-built connectors, known as "nodes," to define automation logic.

**n8n** can be self-hosted on your own server, giving you full control over your data, privacy, and workflows. The platform supports integrations with hundreds of applications, such as Slack, Google Sheets, Trello, and more, allowing you to automate a wide variety of tasks.

## Key Features

### Empowering Non-Developers with AI Automation
- No need for coding knowledge—n8n’s visual interface makes automation accessible to everyone.

### Access to 400+ Built-in Integrations
- Integrate with popular apps like Google apps, Microsoft apps, Slack, X, and more.
- String together multiple integrations for endless possibilities.

### Connect to Almost Any Tool
- Extend n8n using APIs, Webhooks, and custom code to integrate with almost any external tool.

## Why Use n8n?

Manual, repetitive tasks can waste time and increase the likelihood of errors. n8n helps by automating processes, reducing human intervention, and streamlining workflows.

### Common Use Cases:
- **Automating Workflows:** For example, sending emails when a form is submitted.
- **Integrating Apps:** Sync data between tools like CRMs and spreadsheets.
- **Reducing Human Intervention:** Automate tasks like order processing from an e-commerce store.
- **Handling Complex Logic:** Use conditional triggers, data transformations, and more advanced workflows.

Unlike other paid automation tools (like Zapier or Make), n8n is free, self-hostable, and highly customizable, making it an ideal choice for developers and businesses that need flexibility.

## Example: Automating Lead Management

Imagine a company collects leads via a Google Form and wants to automate the following tasks:

1. Store form responses in Google Sheets.
2. Send a Slack notification to the sales team.
3. Add the lead to a CRM (like HubSpot).

### n8n Workflow Steps:
1. **Trigger:** Google Forms node (detects new form submissions).
2. **Action 1:** Google Sheets node (saves data to a spreadsheet).
3. **Action 2:** Slack node (sends a message to a channel).
4. **Action 3:** HubSpot node (creates a new contact in CRM).

**Visual Workflow:**  
Google Form → Google Sheets → Slack → HubSpot

## Key Benefits of n8n

- **No-Code/Low-Code:** User-friendly for non-developers.
- **Self-Hosted:** Full control over privacy, security, and customization.
- **Extensible:** Supports custom nodes using JavaScript or Python.
- **Cost-Effective:** Free & open-source (no recurring subscription fees like Zapier).

## Self-Host vs. Cloud (n8n.io)

**n8n** offers two main deployment options: Self-hosting or using the Cloud platform (n8n.io). Here's how to choose:

### Choose Self-Hosted If:
- You need complete control over your data and environment.
- You want to customize n8n (e.g., custom nodes or logic).
- You have the technical expertise or DevOps resources to manage servers.
- You want to avoid subscription fees, except for hosting costs.
- You have strict compliance requirements for data privacy.

### Choose Cloud (n8n.io) If:
- You want a quick and easy setup.
- You prefer not to manage infrastructure or updates.
- You need reliable uptime and dedicated support.
- You’re comfortable with storing your data on n8n.io's secure servers.
- You want a managed SaaS solution with auto-scaling capabilities.

### Example Scenario:
- **Solo Developer Building a Small App:** Cloud (n8n.io) is ideal for quick setup and minimal infrastructure management.
- **Mid-Sized Company with Sensitive User Data:** Self-hosting is recommended for full control over data security and customization.

## n8n Interface

The n8n interface is designed to be user-friendly while offering powerful automation capabilities. It consists of three main components: Workflows, Nodes, and Executions.

### 1. Workflow
A **workflow** is the complete automation logic that you build visually inside n8n. It connects various apps or services (via nodes) to perform tasks sequentially or conditionally.

#### Example Workflow:
- **Goal:** When a user fills out a contact form (via Typeform), automatically:
  - Save the data to Google Sheets.
  - Send a Slack alert to the team.
  - Email a thank-you message via Gmail.

This complete automation logic is one workflow in n8n.

### 2. Nodes
**Nodes** are the building blocks of workflows. Each node performs a specific task, such as triggering an event, processing data, or integrating with an external app.

#### Types of Nodes:
- **Trigger Node:** Starts the workflow (e.g., Webhook, Form, Cron).
- **Action Node:** Executes an action (e.g., Send Email, Add Row to Google Sheet).
- **Logic Node:** Adds decision-making (e.g., IF, Switch, Merge).

#### Example Workflow with Nodes:
- **Trigger:** Typeform node (starts when the form is submitted).
- **Action 1:** Google Sheets node (adds data to the spreadsheet).
- **Action 2:** Slack node (sends a message to a Slack channel).
- **Action 3:** Gmail node (sends a thank-you email).

### 3. Execution
An **execution** occurs when a workflow runs. Each time a trigger fires (e.g., a form submission), a new execution starts and moves through the workflow’s nodes.

#### Execution Details:
- You can view past executions to check the status of automation, the data passed, and whether any errors occurred.
- Execution logs are useful for debugging and monitoring workflow performance.

#### Example:
If 5 users submit a form today, there will be 5 separate executions, each logging the automation run for each user's data.

## Types of Nodes in n8n

n8n nodes can be broadly categorized into the following types, each with its specific role:

### 1. Trigger Nodes
Trigger nodes start the workflow based on events.
- **Examples:** Webhook, Schedule (Cron), Gmail Trigger, Typeform Trigger.
- **Use Case:** Start a workflow every day at 9 AM → Use a Cron Trigger.

### 2. Action Nodes
Action nodes perform specific tasks, such as sending messages or updating a database.
- **Examples:** Gmail, Slack, Google Sheets, HTTP Request.
- **Use Case:** After a form submission, send a thank-you email → Use the Gmail node.

### 3. Logic Nodes
Logic nodes help control decision-making and data flow within workflows.
- **Examples:** IF, Switch, Merge.
- **Use Case:** If the user's role is "admin," send an alert; otherwise, store the data → Use the IF node.

### 4. Function Nodes
Function nodes allow for custom data manipulation using JavaScript.
- **Examples:** Function, Function Item.
- **Use Case:** Capitalize a user's name before sending an email → Use a Function node.

### 5. Utility Nodes
Utility nodes manage timing, formatting, or simplifying data.
- **Examples:** Wait, Set, Date & Time.
- **Use Case:** After user registration, wait 5 minutes before sending a follow-up email → Use the Wait node.

## Example: Lead Capture Automation

**Goal:** A user fills out a Typeform, and based on their role, either send an email or store their data.

### Workflow with Node Types:
1. **Trigger Node:** Typeform node (detects form submission).
2. **Logic Node:** IF node (checks the role of the user).
3. **Action Node 1:** Gmail node (sends a thank-you email).
4. **Action Node 2:** Google Sheets node (stores the form data).

## Conclusion

**n8n** is a powerful, flexible, and open-source tool for automating tasks and integrating apps without extensive coding. Whether you are a developer or a non-technical user, n8n offers an easy-to-use visual interface that allows you to automate workflows, saving time and reducing errors.

For more information, explore the full documentation and community resources on the [n8n website](https://n8n.io).
