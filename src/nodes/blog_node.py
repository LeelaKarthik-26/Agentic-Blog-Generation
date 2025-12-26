from src.states.blogstate import BlogState
from langchain.prompts import PromptTemplate

class BlogNode:
    """
    Base class for all blog nodes
    """

    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state:BlogState):
        """
        Generate a title for the blog post
        """
        if "topic" in state and state["topic"]:
            prompt = PromptTemplate.from_template(
            """
            \r\n You are an expert blog content writer. Use Markdown formating.
            Generate a blog title for {topic}. This title should be creative 
            and SEO friendly. \r\n
            """
            )
            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke([system_message])
            return {"blog": {'title': response.content}}

    def content_generation(self, state:BlogState):
        """
        Generate the content for the blog post based on the title
        """
        if "topic" in state and state["topic"]:
            prompt = PromptTemplate.from_template(
            """
            \r\n You are an expert blog content writer. Use Markdown formating.
            Generate a blog content for {topic} with detailed breakdown 
            of the content \r\n
            """
            )
            system_message = prompt.format(topic=state['topic'])
            response = self.llm.invoke([system_message])
            return {"blog": {'title': state['blog']['title'], 'content': response.content}}