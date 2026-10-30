from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
load_dotenv()
def main() -> None:
    print("Hello from langchain-demo!")
    information="""Born into the wealthy Musk family in Pretoria,
      South Africa, Musk emigrated in 1989 to Canada;
        he has Canadian citizenship since his mother was born there.
          He received bachelor's degrees in 1997 from the University of Pennsylvania 
          before moving to California to pursue business ventures. In 1995,
          Musk co-founded Zip2, a web software company. Following its sale in 1999, 
          he co-founded X.com, an e-commerce payment system that merged with Confinit
          y in March 2000 to form PayPal. Musk also became an American citizen in 2002.
"""
    summary_template="""
given the information {information} about the person i want to create :
1.A short summary
2.two interestiing facts about them """
    summary_prompt_template=PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOllama(temperature=0,model="gpt-oss:20b ")  #open ai chat model
    chain=summary_prompt_template | llm
    response=chain.invoke({"information":information})
    print(response.content)

main()