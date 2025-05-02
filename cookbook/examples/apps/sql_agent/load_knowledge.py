from agents import agent_knowledge
from agno.utils.log import logger
import os
from dotenv import load_dotenv

def load_knowledge(recreate: bool = True):
    logger.info("Loading SQL agent knowledge.")
    agent_knowledge.load(recreate=recreate)
    logger.info("SQL agent knowledge loaded.")

load_dotenv()
if __name__ == "__main__":
    load_knowledge()
