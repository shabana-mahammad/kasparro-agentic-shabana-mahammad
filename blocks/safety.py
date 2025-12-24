def safety_block(product):
    return {
        "side_effects": product["side_effects"],
        "suitable_for": product["skin_type"]
    }
