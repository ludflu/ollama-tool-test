from llama_index.core.tools import FunctionTool
from llama_index.llms.ollama import Ollama
from llama_index.core.agent import ReActAgent

llm = Ollama(model="llama3", request_timeout=60.0)

def multiply_numbers(x:int, y:int) -> int:
    """useful for getting the product of two numbers."""
    return x * y

def get_weather(location: str) -> str:
    """Usfeful for getting the weather for a given location."""
    return f"its raining in {location} "

def list_family_members(last_name: str) -> list[dict]:
    """Useful for listing the family members of a given name."""
    return [{"name":"Jim", "relation":"Father"},
            {"name":"Jaime", "relation":"Mother"},
            {"name":"Maggie", "relation":"Son"},
            {"name":"Graham", "relation":"Son"}]

weather = FunctionTool.from_defaults(get_weather,
                                  name="get_weather",
                                  description="a tool for getting the weather report")

mult = FunctionTool.from_defaults(multiply_numbers,
                                  name="multiply_numbers",
                                  description="returns the product of two numbers")

fam = FunctionTool.from_defaults(list_family_members,
                                  name="list_family_members",
                                  description="returns a list of family members")

tools = [weather, mult, fam]

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)

agent.chat("what is the name of Maggie's father?")

