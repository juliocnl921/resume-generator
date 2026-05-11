import json
from jinja2 import Template
import os
import logging
from weasyprint import HTML
import openai

logging.basicConfig(level=logging.INFO)

def read_text_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        template = f.read()
        return template

def save_text(content, filename):
    with open(filename, "w", encoding='utf-8') as f:
        f.write(content)

def save_bytes(content, filename):
    with open(filename, "wb") as f:
        f.write(content)

def filter_data(api_key, model, position, lang, data, context):

    in_english = (lang == "en")

    data['contact_title']    = "Contact"    if in_english else "Contacto"
    data['skills_title']     = "Skills"     if in_english else "Habilidades"
    data['experience_title'] = "Experience" if in_english else "Experiencia"
    data['education_title']  = "Education"  if in_english else "Educación"

    data_str = json.dumps(data)

    context = f"{context}\nIMPORTANTE:\nRedacta en ingles" if in_english else context

    user_input = f"""CV:
        {data_str}
        VACANTE:
        {position}
        """
    
    logging.info("FILTERING.......")
    logging.info(f"cv:{data_str[0:50]}")
    logging.info(f"position:{position[0:50]}")

    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": user_input}
        ]
    )

    logging.info("llm was called")

    output_text = response.choices[0].message.content

    output = json.loads(output_text)
    
    return output

def fill_template(data, template):
    html = Template(template).render(
        fullname=data["fullname"],
        title=data["title"],
        summary=data["summary"],
        contact_title=data["contact_title"],
        email=data["email"],
        phone=data["phone"],
        profile=data["profile"],
        experience_title = data["experience_title"],
        experience = data["experience"],
        education_title = data["education_title"],
        education = data["education"],
        skills_title = data["skills_title"],
        skills = data["skills"],
    )

    logging.info(f"filled current template")

    return html
    
def html_to_pdf(html):
   return HTML(string=html).write_pdf()