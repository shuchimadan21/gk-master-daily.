# GK Master Daily

A daily general-knowledge page for students: ten headlines, two AI-in-education
updates, Delhi-NCR weather, city AQI, a quiz and an assembly mode.

- `index.html` is the page.
- `editions/YYYY-MM-DD.json` holds one day's content; `editions/index.json` lists the days.
- After adding an edition file, run `python3 tools/update_index.py`.

The site is static: publish the repository root (no build step).
