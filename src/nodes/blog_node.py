from src.states.blogstare import BlogState

class BlogNode:
    """
    A class to represent the blog node
    """
    
    def __init__(self, llm):
        self.llm = llm
        
    def title_creation(self, state:BlogState):
        """
        Create the title for the blog
    
        """
        
        if "topic" in state and state["topic"]:
            prompt="""
            You are an expert blog content writer. Use Markdown formatting.
            Generate a blog title for the {topic}. This title should be creative and SEO friendly.
            """
            
            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog":{"title":response.content}}
        
    def content_generation(self, state:BlogState):
        """
        generate content for the title
        """
        
        if "topic" in state and state["topic"]:
            prompt="""
            You are an expert blog content writer. Use Markdown formatting.
            Generate a detail blog content with detail breakdown for the {topic}.
            """
            
            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": {"title": state['blog']['title'], "content": response.content}}
        
    def translation(self, state:BlogState):
        """
        Translate the content to the specified language.
        """
        translation_prompt = """
        Translate the following content into {current_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.

        ORIGINAL CONTENT:
        {blog_content}
        """

        blog_content = state["blog"]["content"]
        message = translation_prompt.format(
            current_language=state["current_language"],
            blog_content=blog_content,
        )

        response = self.llm.invoke(message)
        return {
            "blog": {
                "title": state["blog"]["title"],
                "content": response.content,
            }
        }
    
    def route(self, state: BlogState):
        return {"current_language": state['current_language']}
    
    def route_decision(self, state:BlogState):
        """
        Route the content to the respective translation function.
        """
        if state["current_language"] == "hindi":
            return "hindi"
        elif state["current_language"] == "french":
            return "french"
        else:
            raise ValueError(f"Unsupported language: {state['current_language']}")
