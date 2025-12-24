class TemplateAgent:

    def build_faq(self, questions, product):
        faqs = []

        faqs.append({
            "question": questions["Informational"][0],
            "answer": f"{product['product_name']} contains {product['concentration']}."
        })

        faqs.append({
            "question": questions["Usage"][0],
            "answer": product["usage"]
        })

        faqs.append({
            "question": questions["Safety"][0],
            "answer": product["side_effects"]
        })

        return {
            "page_type": "FAQ",
            "faqs": faqs
        }

    def build_product_page(self, product, blocks):
        return {
            "product_name": product["product_name"],
            "overview": {
                "concentration": product["concentration"],
                "skin_type": product["skin_type"]
            },
            "ingredients": product["key_ingredients"],
            "benefits": blocks["benefits"]["benefits"],
            "usage": product["usage"],
            "safety": product["side_effects"],
            "price": product["price"]
        }
