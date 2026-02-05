import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager #importing class ResearchManager

load_dotenv(override=True)

#run function
#takes research query as input and streams each chunk piece by piece
async def run(query: str):
    async for chunk in ResearchManager().run(query): #.run() from ResearchManager
        yield chunk #yield - LLM generator updates UI progressively 

#Gradio interface with custom theme
with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research") #title heading
    query_textbox = gr.Textbox(label="What topic would you like to research?") #text input where users type their research topic
    run_button = gr.Button("Run", variant="primary") #button to start the research
    report = gr.Markdown(label="Report") #Markdown display area where results appear
    
    #click run button OR pressing enter in textbox => triggers run function, inputting query text, outputing the report
    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

#starts and opens it in browser
ui.launch(inbrowser=True)

