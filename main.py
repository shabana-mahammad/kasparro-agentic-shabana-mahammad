from product_data import RAW_PRODUCT_DATA
from agents.orchestrator import Orchestrator

if __name__ == "__main__":
    Orchestrator().run(RAW_PRODUCT_DATA)
