import json
from agents.data_parser_agent import DataParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.content_logic_agent import ContentLogicAgent
from agents.template_agent import TemplateAgent
from agents.comparison_agent import ComparisonAgent

class Orchestrator:

    def run(self, raw_data):
        product = DataParserAgent().parse(raw_data)
        questions = QuestionGeneratorAgent().generate(product)
        blocks = ContentLogicAgent().build(product)

        faq = TemplateAgent().build_faq(questions, product)
        product_page = TemplateAgent().build_product_page(product, blocks)
        comparison = ComparisonAgent().compare(product)

        self.save("outputs/faq.json", faq)
        self.save("outputs/product_page.json", product_page)
        self.save("outputs/comparison_page.json", comparison)
        print("All pages generated successfully.")
        print("Check outputs/ folder")


    def save(self, path, data):
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
