class QuestionGeneratorAgent:
    def generate(self, product):
        return {
            "Informational": [
                f"What is {product['product_name']}?",
                "What is the concentration of Vitamin C?"
            ],
            "Usage": [
                "How should I apply this serum?",
                "When should I use this product?"
            ],
            "Safety": [
                "Are there any side effects?",
                "Is it suitable for sensitive skin?"
            ],
            "Purchase": [
                "What is the price of this serum?",
                "Which skin types is this suitable for?"
            ],
            "Comparison": [
                "How is this different from other Vitamin C serums?"
            ]
        }
