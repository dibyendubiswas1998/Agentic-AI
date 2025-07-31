# Model Context Protocol (MCP)

MCP (Model Context Protocol) is an open protocol that standardizes how applications provide and interact with context for Large Language Models (LLMs). Think of MCP like a USB-C port for AI applications: just as USB-C provides a universal connection for hardware, MCP enables AI apps to connect with tools, APIs, databases, and files in a structured, modular, and scalable way.

---

## 🚀 Why MCP?

Modern LLM-based applications need to dynamically access and interact with diverse tools and data sources. Traditional RESTful APIs fall short because they:

- Require custom integration for every tool
- Lack persistent context and memory
- Don’t support dynamic tool discovery or bi-directional communication

**MCP solves this by offering:**

- 📦 Dynamic, pluggable tools with self-describing schemas  
- 🧠 Context sharing across tools and sessions  
- 🔁 Asynchronous interactions (e.g., background jobs, notifications)  
- 📉 Reduced N×M complexity in multi-tool integrations

---

## 🧩 Key Terminologies

### 1. MCP Host
- The LLM-powered application (e.g., a chat UI, IDE, or LangChain agent)
- Orchestrates interactions with tools but doesn’t connect directly to them
- Uses MCP Clients internally to make tool requests  
> _Example: Claude Desktop querying a Postgres database_

---

### 2. MCP Client
- The connector inside the Host
- Translates LLM requests to MCP messages using JSON-RPC
- Maintains 1:1 connection with MCP Servers  
> _Analogy: like a “waiter” taking orders from the LLM “chef”_

---

### 3. MCP Server
- Lightweight service exposing one or more tools
- Self-describes its capabilities, inputs/outputs, and schemas
- Can wrap local or remote tools and data  
> _Example: A `Quiz Generator` server that takes topics and returns MCQs_

---

### 4. MCP Protocol
- Standard that defines how MCP Clients and Servers communicate
- Uses **JSON-RPC 2.0** over **stdio** or **HTTP + SSE**
- Enables:
  - Tool discovery
  - Structured inputs/outputs
  - Persistent memory
  - Bi-directional communication

---

## 🔄 Communication Between Components
![MCP](Img/Communication%20Between%20MCP%20Components.png)
### 🔑 **Step-by-Step Flow**

1️⃣ **User Input**
A user provides input (e.g., a question or command) to the system.

2️⃣ **MCP Client requests tool list**
The MCP Client (inside the MCP Host / Application) queries available MCP Servers to **find the list of tools** they provide.

3️⃣ **MCP Client collects tool descriptions**
The MCP Client **retrieves metadata** about the available tools from all MCP Servers (e.g., what methods they support, input/output schemas).

4️⃣ **LLM receives question + tool list**
The MCP Client gives the LLM the user’s question and the list of available tools for reasoning.

5️⃣ **LLM selects a specific tool for the task**
The LLM decides which tool(s) to call based on the user input and tool capabilities, then forms a tool request.

6️⃣ **MCP Client sends tool call**
The MCP Client forwards the LLM’s tool request (via JSON-RPC) to the **specific MCP Server** that hosts the tool.

7️⃣ **MCP Server processes and extracts context**
The MCP Server performs the requested operation (e.g., DB query, file processing, API call) and generates output.

8️⃣ **MCP Client returns tool response to LLM**
The result from the tool is passed back to the LLM for integration into its reasoning.

9️⃣ **LLM generates contextualized response**
The LLM uses the tool output as part of its overall response formulation.

🔟 **Final output to user**
The user receives a rich, contextualized answer that combines the LLM’s reasoning and the tool’s output.

---

## 🧪 Real-World Example: K12 Chatbot with Agentic Capabilities

**Scenario**: You're building an AI chatbot for students that can:

- Answer subject questions (Math, Science)
- Generate MCQs or quizzes
- Summarize textbooks
- Solve equations and generate charts

### Architecture

| Component      | Description |
|----------------|-------------|
| **MCP Host**   | LLM-powered chatbot interface with memory and tool orchestration |
| **MCP Client** | Connector inside the host that discovers tools and invokes servers |
| **MCP Servers**| Tool providers (e.g., `quiz_generator`, `math_solver`, `textbook_reader`) |
| **MCP Protocol**| JSON-RPC-based protocol enabling real-time, contextual communication |

> Example Tools as MCP Servers:
> - `textbook_reader` (markdown/PDF parser)
> - `quiz_generator` (returns topic-based MCQs)
> - `math_solver` (evaluates and graphs equations)
> - `video_explainer` (calls APIs for animated tutorials)

---

## 🛡️ Security, Scalability & Design Considerations

### ✅ Security & Isolation
- Each MCP Server runs in isolation (process/container)
- Prevents unauthorized access between tools
- Enables sandboxing for untrusted tools (e.g., code executors)

### 🔄 Scalability & Modularity
- Scale tools independently (e.g., deploy quiz and video servers separately)
- Tools can be developed, tested, and deployed independently
- Ideal for microservices or function-as-a-service platforms

---

## ⚖️ APIs vs. MCP — A Comparison

| Criteria            | Traditional APIs           | Model Context Protocol (MCP)         |
|---------------------|----------------------------|---------------------------------------|
| Designed For        | Frontend/human clients     | LLMs and autonomous agents            |
| Interface Type      | RESTful (HTTP endpoints)   | JSON-RPC (`run_tool`, `generate_quiz`) |
| Tool Discovery      | Manual/OpenAPI             | Automatic/self-describing             |
| Context Awareness   | Stateless                  | Contextual (session-aware)            |
| Dynamic Tool Calls  | Not native                 | Built-in, real-time                   |
| Communication       | Synchronous                | Supports async & notifications        |
| Scalability Model   | Per-function microservices | Modular MCP Servers per tool/group    |
| Use Case Fit        | CRUD apps, APIs            | LLM agents, AI orchestration          |

---

## 📚 Example Tool Definitions

Each MCP Server provides a schema describing the tools it offers:

```json
{
  "tool": "generate_quiz",
  "description": "Generate 5 MCQs on a given topic",
  "input_schema": {
    "type": "object",
    "properties": {
      "topic": { "type": "string" },
      "difficulty": { "type": "string" }
    }
  },
  "output_schema": {
    "type": "array",
    "items": { "type": "object" }
  }
}
```

---

## 📌 Conclusion
MCP is purpose-built for LLM-first architectures. It abstracts away the complexity of integrating and orchestrating tools, allowing AI agents to discover, invoke, and interact with them in real-time, with full context and modularity.