# external imports
import os
import sys
from dotenv import load_dotenv

# internal imports
current_directory = os.path.dirname(os.path.abspath(__file__))
project_root_directory = os.path.dirname(current_directory)
sys.path.append(project_root_directory)

# load environment variables
load_dotenv()
# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_CHAT_MODEL = os.environ.get("OPENAI_CHAT_MODEL")
