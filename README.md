# resume-generator
AI-powered resume utility to adapts your experience and skills to any job description and outputs a ready-to-send PDF.

This repo includes a utility library for resume adaptation, a command-line tool for local use, and an HTTP service for integration into other applications.

These utilities use OpenAI models during the filtering stage, so an OpenAI API key is required.

To run it locally in a simple way, you can execute the `local.py` script.

The process consists of 3 main steps:

1. **Experience adaptation**
   
   **Input:**
   - JSON object with your experience data
   - Job description

   **Output:**
   - JSON object with your experience data adapted to the job posting

2. **HTML generation**
   
   **Input:**
   - JSON object with your experience data
   - Jinja2 template using an ATS-friendly format

   **Output:**
   - Jinja2 template rendered as HTML

3. **PDF generation**
   
   **Input:**
   - Jinja2 template rendered as HTML

   **Output:**
   - HTML rendered as PDF

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
- OpenAI API key.

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate (.venv/Scripts/Activate.ps1 in windows powershell)
pip install -r requirements.txt
```
Add an `OPENAI_API_KEY` environment variable with your OpenAI API key.

## Usage

### Command Line

```bash
python local.py <model> <output> <language>
```

### Parameters

#### `model`
Model used to adapt the resume content.

| Value | Description |
|---|---|
| `mini` | Alias for `gpt-5-mini` |
| `nano` | Alias for `gpt-5.4-nano` |
| `full` | Alias for `gpt-5.4` |

#### `output`
Defines which stages of the pipeline will be executed.

| Value | Description |
|---|---|
| `all` | Filter `resume.cv` using `position.txt`, render the HTML template, and generate the final PDF |
| `html` | Filter `resume.cv` using `position.txt` and render the HTML template |
| `pdf` | Take a previously rendered HTML file and generate the PDF |

#### `language`
Forces the output language.

| Value | Description |
|---|---|
| `es` | Output in Spanish |
| `en` | Output in English |

### Example

```bash
python local.py mini all en
```

## Example as comand line tool for all stages
fill the position content in files/position.txt
fill the resume data in files/resume.json

activate environment and then execute:
```bash
python local.py nano all en
```

## Example usage in local only filter and fill html template
```bash
python local.py nano html en
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