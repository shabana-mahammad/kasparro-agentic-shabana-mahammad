# Agentic Content System – Architecture

## Overview
This system is an agent-based content generation pipeline that transforms
structured product data into multiple content pages using reusable logic blocks
and templates.

The design prioritizes modularity, clarity, and deterministic outputs.

## High-Level Flow

product_data
 → DataParserAgent
 → ContentLogicAgent
 → Domain Agents (FAQ / Product / Comparison)
 → TemplateAgent
 → JSON Outputs

## Core Components

### Agents
- Each agent has a single responsibility
- Agents are stateless and operate only on input data
- Orchestration is controlled centrally

### Blocks
- Blocks contain reusable domain logic (benefits, usage, safety)
- Blocks can be reused across multiple agents

### Templates
- Templates define output structure
- Agents only fill data, not formatting

### Orchestrator
- Coordinates agent execution
- Ensures predictable execution order

## Design Principles
- Separation of concerns
- Reusable logic blocks
- Template-driven structured output
- Easy to extend with new agents or pages

## Future Improvements
- JSON schema validation for outputs
- CLI-based execution
- Agent interface standardization
