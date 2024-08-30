


import os
os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"
from langchain.llms import  HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"#model version or type to be used

llm=HuggingFaceEndpoint(repo_id=repo_id,huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"],temperature=0.6)






def generate_name_menu(cuisine):
    
    prompt_template=PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurent for {cuisine} food. suggest me some fancy names"
    )
    name_chain=LLMChain(llm=llm,prompt=prompt_template,output_key="restaurant_name")
    prompt_template_items=PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest some menu intems for {restaurant_name}."""

    )
    food_items_chain=LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu_items")


    
    chain=SequentialChain(
        chains=[name_chain,food_items_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name","menu_items"]
    )
    response=chain({'cuisine':"Indian"})
    return response

if __name__=="__main__" :
    print(generate_name_menu("Italian")) 
   