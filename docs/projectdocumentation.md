## 1. Problem Statement
Design a modular, multi-agent system that converts structured product data into
machine-readable content pages (FAQ, Product Page, and Comparison Page) using
automation and template-driven generation.

## 2. Solution Overview
The system is built using multiple specialized agents coordinated by a central
orchestrator. Each agent performs a single responsibility. Reusable logic blocks
handle data transformation, and templates are used to assemble consistent JSON
outputs.

## 3. Scope & Assumptions
- One product is processed per execution
- Output is generated strictly in JSON format
- No external APIs or external data sources are used
- Comparison pages may use fictional products for demonstration purposes

## 4. System Design
The system follows a sequential, deterministic flow:

- **DataParserAgent**: Normalizes and prepares input product data
- **QuestionGeneratorAgent**: Generates structured FAQ questions
- **ContentLogicAgent**: Applies reusable domain logic blocks
- **TemplateAgent**: Renders structured content using templates
- **ComparisonAgent**: Generates product comparison content
- **OrchestratorAgent**: Controls execution order and data flow

## 5. Outputs
The system generates the following machine-readable files:
- `faq.json`
- `product_page.json`
- `comparison_page.json`
