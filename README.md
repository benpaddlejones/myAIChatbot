# My AI Chatbot

A web-based AI chatbot built with Python Flask and Bootstrap.

## Description

An AI-powered chatbot that can have conversations with users. It responds to common questions and provides helpful information. Built as part of the TempeHS Computing Technology course.

## Getting Started

### Dependencies

- Python 3.11+
- Flask
- ChatterBot
- spaCy with en_core_web_sm model

### Installing

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Download spaCy model: `python -m spacy download en_core_web_sm`

### Executing program

```bash
source venv/bin/activate
python app.py
```
Then open http://localhost:5000 in your browser.

## Testing

### User Acceptance Testing Results

Tested on: February 2026
Tester: Student Name

| Test ID | Description | Status |
|---------|-------------|--------|
| TC-001 | Normal message response | ✅ Pass |
| TC-002 | Empty message handling | ✅ Pass |
| TC-003 | Message length validation | ✅ Pass |
| TC-004 | Crisis keyword detection | ✅ Pass |
| TC-005 | Disclaimer visibility | ✅ Pass |
| TC-006 | Message styling | ✅ Pass |

**Summary**: All 6 test cases passed. The chatbot meets all functional and non-functional requirements.

## Help

Common issues:
- If ChatterBot fails to load, ensure spaCy model is installed: `python -m spacy download en_core_web_sm`
- If port 5000 is in use, the server will show an error. Stop other processes using that port.

## Authors

Student Name  
[@studentusername](https://github.com/studentusername)

## Version History

- 0.2
  - Various bug fixes and optimizations
  - See [commit change]() or See [release history]() or see [branch]()
- 0.1
  - Initial Release

## License

This project is licensed under the GNU GPL v3.0 License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.

- [Github md syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [TempeHS Python Flask template](https://github.com/TempeHS/TempeHS_Python-Flask_DevContainer)
