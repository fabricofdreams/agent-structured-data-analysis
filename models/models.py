from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()


class LargeLanguageModel():
    """API LLMs services"""

    def chat_Openai(self, temp: float):
        """OpenAI llm"""
        return ChatOpenAI(
            model_name="gpt-3.5-turbo", temperature=temp)

    def gemini(self, temp: float):
        """Google llm"""
        return ChatGoogleGenerativeAI(
            model="gemini-pro", temperature=temp)

    def mixtral_groq(self, temp: float):
        """Mixtral llm operated by Groq"""
        return ChatGroq(temperature=temp, model_name="mixtral-8x7b-32768")

    def claude3_opus(self, temp: float):
        """Anthropic llm - most expensive
        Most powerful model for highly complex tasks
        """
        return ChatAnthropic(temperature=temp, model_name='claude-3-opus-20240229')

    def claude3_sonnet(self, temp: float):
        """Anthropic llm - 
        Ideal balance of intelligence and speed for enterprise workloads"""
        return ChatAnthropic(temperature=temp, model_name='claude-3-sonnet-20240229')

    def claude3_haiku(self, temp: float):
        """Anthropic llm - 
        Fastest and most cost-effective model for its intelligence category."""
        return ChatAnthropic(temperature=temp, model_name='claude-3-haiku-20240307')
