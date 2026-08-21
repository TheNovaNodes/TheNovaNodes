# TheNovaNodes 🌌

## What is TheNovaNodes?
TheNovaNodes is a modular upgrade layer for AI agent systems. It provides independent capabilities through the Model Context Protocol (MCP), HTTP, CLI, and compatible APIs to augment your existing agentic workflows.

## What problem does the modular layer solve?
Instead of a monolithic, one-size-fits-all solution, TheNovaNodes allows developers to selectively integrate individual tools, gateways, and controls into their existing setups. It decouples the orchestrator, cloud workers, and tools so you can build exactly what you need without being locked into a single ecosystem.

## Which capabilities are available?
We offer modular capabilities across different domains:
- **Semantic Memory**: Hybrid search and knowledge retrieval.
- **Web Intelligence**: Privacy-focused meta-search access.
- **Enterprise CRM/Storage**: Access to cloud files, notes, and user data.
- **Orchestration & Workers**: Reference orchestrators and specific cloud agent workers.

## How can a user start with one module?
Through our **"Choose Your Upgrade"** onboarding, you can adopt just a single repository. For instance, if you only need web search for your AI, you can spin up the `searxng-mcp-gateway` and connect it to your preferred orchestrator without adopting the rest of the stack.

## What is verified today and what remains experimental?
- **Verified**: Individual MCP gateways (Data Plane) and Controls (Control Plane) are verified for use in local and tunneled environments.
- **Experimental**: Complex multi-agent orchestration, fully decoupled autonomous workflows, and multi-layered worker architectures remain in experimental stages.

---

## Architecture

TheNovaNodes uses a modular topology. The Antigravity Telegram Agent is provided as a reference orchestrator (not a mandatory core) and Google Jules as one worker integration (not the only possible worker).

```mermaid
flowchart TD
    Orch[Orchestrator\n(e.g., antigravity-telegram-agent, or custom)]
    Worker[Cloud Workers\n(e.g., google-jules-mcp, or others)]
    
    Orch <--> Worker
    Worker <--> MCP[MCP Matrix]
    Orch <--> MCP
    
    subgraph MCP Matrix
        subgraph Memory
            A_G[anythingllm-mcp-gateway]
            A_C[anythingllm-mcp-control]
        end
        subgraph Web
            S_G[searxng-mcp-gateway]
            S_C[searxng-mcp-control]
        end
        subgraph CRM
            N_G[nextcloud-mcp-gateway]
            N_C[nextcloud-mcp-control]
        end
        subgraph Security
            PR_R[mcp-gh-pr-reviewer]
        end
        Vault[agent-vault]
    end
```

---

## Capability Matrix

| Domain | Data Plane (Read/Gateway) | Control Plane (Write/Admin) |
|---|---|---|
| **Semantic Memory** | anythingllm-mcp-gateway | anythingllm-mcp-control |
| **Web Intelligence** | searxng-mcp-gateway | searxng-mcp-control |
| **CRM & Storage** | nextcloud-mcp-gateway | nextcloud-mcp-control |
| **Security & Auditing** | mcp-gh-pr-reviewer | *N/A* |

---

## Choose Your Upgrade (Onboarding)

You don't need to adopt the entire suite. Choose what fits your needs:
1. **Need an Orchestrator?** Try our reference implementation: [antigravity-telegram-agent](https://github.com/TheNovaNodes/antigravity-telegram-agent)
2. **Need a Cloud Worker?** Integrate: [google-jules-mcp](https://github.com/TheNovaNodes/google-jules-mcp)
3. **Need Tools/Storage?** Spin up one of our MCP gateways or controls (see Repository Groups below) or securely manage credentials with [agent-vault](https://github.com/TheNovaNodes/agent-vault).

---

## Security Model

TheNovaNodes prioritizes secure access models. Our MCP gateways are designed to be run locally and can be securely tunneled with strict API headers for authentication. This ensures that sensitive internal data planes (such as Nextcloud or AnythingLLM) are not broadly exposed to the public internet, requiring explicit authentication from your agent workers.

---

## Repository Groups

### Orchestration & Workers
- **[antigravity-telegram-agent](https://github.com/TheNovaNodes/antigravity-telegram-agent)**: A reference orchestrator providing a Telegram interface for agent management.
- **[google-jules-mcp](https://github.com/TheNovaNodes/google-jules-mcp)**: An integration module for Google Jules cloud workers.
- **[agent-vault](https://github.com/TheNovaNodes/agent-vault)**: Secure credential and secrets management for your agents.

### Semantic Memory
- **[anythingllm-mcp-gateway](https://github.com/TheNovaNodes/anythingllm-mcp-gateway)**: Connects LLMs to internal knowledge bases.
- **[anythingllm-mcp-control](https://github.com/TheNovaNodes/anythingllm-mcp-control)**: Manages AnythingLLM workspaces and threads.

### Web Intelligence
- **[searxng-mcp-gateway](https://github.com/TheNovaNodes/searxng-mcp-gateway)**: Privacy-focused web search for real-time agent research.
- **[searxng-mcp-control](https://github.com/TheNovaNodes/searxng-mcp-control)**: Administers SearXNG settings.

### Enterprise CRM
- **[nextcloud-mcp-gateway](https://github.com/TheNovaNodes/nextcloud-mcp-gateway)**: Allows agents to read WebDAV, files, and notes.
- **[nextcloud-mcp-control](https://github.com/TheNovaNodes/nextcloud-mcp-control)**: Manages Nextcloud users and permissions.

### Security & Auditing
- **[mcp-gh-pr-reviewer](https://github.com/TheNovaNodes/mcp-gh-pr-reviewer)**: Universal Fallback MCP Server for automated GitHub Pull Request security reviews.

---

## Status & Limitations
- **Modularity:** High. You can use any module independently.
- **Maturity:** The data plane MCP gateways are verified for production usage; complex orchestrated workflows are experimental.
- **Limitations:** Certain control plane modules require elevated privileges to the underlying services (e.g., Nextcloud admin credentials), so careful deployment is required.

---

## Support TheNovaNodes

If this modular agent infrastructure is useful to you, you can support its open-source development.

**USDT (TRC20):** `TQvw8MJMdSBFXu5G74JsZm1gzg7cuXBZ2o`
