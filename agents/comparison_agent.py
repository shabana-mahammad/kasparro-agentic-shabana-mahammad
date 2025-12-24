class ComparisonAgent:
    def compare(self, product):
        product_b = {
            "name": "RadiantC Serum",
            "ingredients": ["Vitamin C"],
            "benefits": ["Brightening"],
            "price": 799
        }

        return {
            "comparison": {
                "product_a": {
                    "name": product["product_name"],
                    "ingredients": product["key_ingredients"],
                    "benefits": product["benefits"],
                    "price": product["price"]
                },
                "product_b": product_b
            }
        }
