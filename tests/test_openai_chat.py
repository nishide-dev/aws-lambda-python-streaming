# external imports
import pytest
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# internal imports
from config.env import OPENAI_API_KEY, OPENAI_CHAT_MODEL

# define the test
class TestOpenAIChat:
    @pytest.fixture
    def init_llm(self):
        return ChatOpenAI(
            model=OPENAI_CHAT_MODEL,
            api_key=OPENAI_API_KEY,
        )
    
    def test_stream(self, init_llm: ChatOpenAI):
        prompt = "自己紹介をしてください"
        chain = init_llm | StrOutputParser()
        for chunk in chain.stream(prompt):
            assert isinstance(chunk, str)
            print(chunk, end="", flush=True)

