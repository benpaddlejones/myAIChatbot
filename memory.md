# Activity Review Memory

## Goals

- Follow each LMS instruction step-by-step to replicate the student experience.
- Validate that every command and code block works in a fresh fork of the template repository.
- Track mismatches, missing context, or confusing directions for Year 7-9 students.
- Produce a final Markdown report listing only meaningful improvements to the LMS content and activities.

## Key Constraints

- Commit messages must follow `type: description` (TempeHS style guide).
- Final repository state must match the LMS directions exactly.
- Document issues factually; avoid unnecessary recommendations.
- Ensure `.gitignore` excludes `venv/` and `chatbot_database.sqlite3` before pushing.

## User Decisions

- Naming: Change instructions from `myAIBot` to `myAIChatbot` throughout
- Start: Do README updates from Lesson 1, skip GitHub UI forking steps
- ChatterBot: If it fails, suggest a simpler alternative library

## Current State (Start)

- README.md: Template format (needs updating per Lesson 1)
- requirements.txt: Flask, bcrypt, flask_wtf (no chatbot library yet)
- .gitignore: Comprehensive Python gitignore

## Issues Found

(Will populate as I work through lessons)

## Progress Tracking

- [ ] Lesson 1: Update README as instructed
- [ ] Lesson 2: Create venv, install packages, create app.py, first commit
- [ ] Lesson 3: Add ChatterBot/alternative, create templates/index.html placeholder
- [ ] Lesson 4: Build Bootstrap frontend
- [ ] Lesson 5: Add safety features (crisis detection, disclaimer)
- [ ] Lesson 6: Document UAT (manual testing)
- [ ] Lesson 7: Add pytest tests, sanitisation
