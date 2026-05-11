import json
import logging
import sys
import os
from constants import CONTEXT, MODEL_NANO, MODEL_MINI, MODEL_FULL
from CVutils import read_text_file, save_text, save_bytes, filter_data, fill_template, html_to_pdf

api_key = os.getenv("OPENAI_API_KEY")
position = read_text_file("files/position.txt")
resume_file = read_text_file("files/resume.json")
resume_file = json.loads(resume_file)

if len(sys.argv) != 4:
    logging.info("PARAMS NEEDED: model(mini,nano,full) outputs(all, html, pdf) language(es, en) ")
    sys.exit()

models   = {"nano": MODEL_NANO, "mini":MODEL_MINI, "full": MODEL_FULL}
model   = models[sys.argv[1]]
outputs = sys.argv[2] 
lang    = sys.argv[3]  

output_filename = 'output/resume'

if outputs == "all":
    filtered_data = filter_data(api_key, MODEL_NANO, position, lang , resume_file, CONTEXT)
    template = read_text_file('files/atsSafeTemplate.html')  
    html_rendered = fill_template(filtered_data, template)
    pdf_rendered = html_to_pdf(html_rendered)
    save_bytes(pdf_rendered, f"{output_filename}.pdf")

if outputs == "html":
    filtered_data = filter_data(api_key, MODEL_NANO, position, lang , resume_file, CONTEXT)
    template = read_text_file('files/atsSafeTemplate.html')  
    html_rendered = fill_template(filtered_data, template)
    save_text(html_rendered, f"{output_filename}.html")

if outputs == "pdf":
    html_rendered = read_text_file(f"{output_filename}.html")  
    pdf_rendered = html_to_pdf(html_rendered)
    save_bytes(pdf_rendered, f"{output_filename}.pdf")