OctoFit Tracker — Backend

Setup

1. Create a virtual environment:

```bash
python3 -m venv /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv
source /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/activate
pip install -r /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/requirements.txt
```

2. Run migrations and start server (after installing Django):

```bash
python /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/manage.py migrate
python /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/manage.py runserver 0.0.0.0:8000
```

Notes
- Use Django ORM for data operations; prefer `ps aux | grep mongod` to check MongoDB when needed.
