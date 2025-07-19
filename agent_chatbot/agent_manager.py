from langchain_core.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor

class AgentManager:
    def __init__(self, models, tools):
        self.models = models
        self.tools = tools
        self.prompt = self._create_prompt_template()
        self.agent = self._create_agent()
        self.agent_executor = self._create_agent_executor()
    
    def _create_prompt_template(self):
        """Create prompt template for the agent"""
        template = '''
                  Answer the following questions as best you can. You have access to the following tools:

                  {tools}

                  Use the following format:

                  Question: the input question you must answer
                  Thought: you should always think about what to do
                  Action: the action to take, should be one of [{tool_names}]. Always look first in Vector Store
                  Action Input: the input to the action
                  Observation: the result of the action
                  ... (this Thought/Action/Action Input/Observation can repeat 2 times)
                  Thought: I now know the final answer
                  Final Answer: the final answer to the original input question

                  Begin!

                  Question: {input}
                  Thought:{agent_scratchpad}
                  '''
        return PromptTemplate.from_template(template)
    
    def _create_agent(self):
        """Create the agent using the LLM and the prompt template"""
        agent = create_react_agent(
            tools=self.tools, 
            llm=self.models.llm, 
            prompt=self.prompt
        )
        return agent
    
    def _create_agent_executor(self):
        """Initialize the agent executor with the created agent and tools"""
        agent_executor = AgentExecutor(
            tools=self.tools, 
            agent=self.agent, 
            handle_parsing_errors=True, 
            verbose=False
        )
        return agent_executor
    
    def query(self, user_input):
        """Execute a query using the agent"""
        response = self.agent_executor.invoke({"input": user_input})
        return response['output']