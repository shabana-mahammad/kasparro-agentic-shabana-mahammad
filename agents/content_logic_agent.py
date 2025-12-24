from blocks.benefits import benefits_block
from blocks.usage import usage_block
from blocks.safety import safety_block

class ContentLogicAgent:
    def build(self, product):
        return {
            "benefits": benefits_block(product),
            "usage": usage_block(product),
            "safety": safety_block(product)
        }
