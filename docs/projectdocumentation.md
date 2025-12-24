1. Problem Statement
    Design a modular multi-agent system that converts structured product data into machine-readable content pages (FAQ, Product, Comparison) using automation and templates.

2. Solution Overview
    The system uses multiple specialized agents coordinated by an orchestrator. Each agent performs one task, reusable logic blocks transform data, and templates assemble final JSON outputs.

3. Scope & Assumptions
    One product per run
    JSON output only
    No external APIs or data
    Fictional product allowed for comparison

4. System Design (Important)
    DataParserAgent → normalize input
    QuestionGeneratorAgent → generate questions
    ContentLogicAgent → apply reusable blocks
    TemplateAgent → assemble pages
    ComparisonAgent → compare products
    OrchestratorAgent → control flow

5. Output
    Generates:
        faq.json
        product_page.json
        comparison_page.json