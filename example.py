import json
import logging
import os
from constants import CONTEXT, MODEL_NANO
from CVutils import read_text_file, save_bytes, filter_data, fill_template, html_to_pdf

api_key = os.getenv("OPENAI_API_KEY")
position = read_text_file("files/position.txt")
resume_file = read_text_file("files/resume.json")
resume_file = json.loads(resume_file)

#STEP 1: generate fited resume file to position description
filtered_data = filter_data(api_key, MODEL_NANO, position, "en", resume_file, CONTEXT)

# #STEP 2: fill html template with previous fited resume file
template = read_text_file('files/atsSafeTemplate.html')  
html_rendered = fill_template(filtered_data, template)

#STEP 3: generate pdf file with html template filled
pdf_rendered = html_to_pdf(html_rendered)
save_bytes(pdf_rendered, "output/resume.pdf")