# resume-generator
AI-powered resume utility to adapts your experience and skills to any job description and outputs a ready-to-send PDF.

This repo includes a command-line tool for local use and an HTTP service with API endpoints for integration into other applications.

## Contents

| File | Description |
|------|-------------|
| `CVUtils.py` | Core utility functions for resume filtering, rendering, and PDF generation |
| `example.py` | Minimal example showing how to use `CVUtils.py` directly |
| `local.py` | Command-line tool for quick local PDF generation |
| `service.py` | Flask API service to expose the utilities as HTTP endpoints |

## Requirements
- Python 3.8+
- GTK runtime (https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate (.venv/Scripts/Activate.ps1 in windows powershell)
pip install -r requirements.txt
```

## Usage as comand line tool
python local.py model[mini |nano | full] outputs[all | html| pdf] language[es | en]

Params: 
    model:
        mini: Short alias for gpt-5-mini to filter
        nano: Short alias for gpt-5.4-nano to filter
        full: Short alias for gpt-5.4 to filter
    outputs:
        all: Filter resume.cv with position.txt content > fill html template with the previous output > render pdf file
        html: filter resume.cv with position.txt content > fill html template with the previous output 
        pdf: take a previous redered output html file > render pdf file
    language:
        es: Force to ouput in spanish
        en: Force to ouput in english

## Example as comand line tool for all stages
fill the position content in files/position.txt
fill the resume data in files/resume.json

activate environment and then execute:
```bash
python run.py nano all en
```

## Example usage in local only filter and fill html template
```bash
python run.py nano html en
```

## usage as API Endpoints

All endpoints accept `POST` requests with a JSON body.

---
### `POST /filter`

Filters and adapts experience data to a specific job position using an AI model.

**Body:**
| Field | Type | Description |
|-------|------|-------------|
| `api_key` | string | OpenAI API key |
| `model` | string | Model size: `nano`, `mini`, or `full` |
| `lang` | string | Output language (e.g. `en`, `es`) |
| `position` | string | Job description or position title |
| `data` | object | Raw resume data in JSON format |

**Response:** JSON object with filtered raw resume data.

---

### `POST /html`

Generates an ATS-safe HTML resume from raw resume data.

**Body:**
| Field | Type | Description |
|-------|------|-------------|
| `data` | object | Raw resume data in JSON format |

**Response:** HTML string ready to render or convert to PDF.

---

### `POST /pdf`

Converts an HTML string into a PDF file.

**Body:**
| Field | Type | Description |
|-------|------|-------------|
| `data` | string | HTML content to convert |

**Response:** PDF file as binary content.