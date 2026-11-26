# CrewAI Travel Planner Agent

A beginner CrewAI project: type a city and a **Travel Planner** agent (powered by Anthropic Claude) suggests exactly 3 places to visit there.

Built for Week 4, Day 3 of the GenAI course.

## How it works

- **Agent**: `Local Travel Planner`, with a role, goal and backstory that steer it towards short, practical advice for first-time visitors.
- **Task**: asks for exactly 3 places in the city, with an `expected_output` that forces a clean numbered list.
- **Crew**: one agent, one task, run with `crew.kickoff(inputs={"city": city})`.

## Setup

Requires Python 3.10 to 3.13.

```bash
python -m venv venv

# Windows (PowerShell)
venv\Scripts\Activate.ps1
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file next to `travel_planner.py` (copy `.env.example`):

```
ANTHROPIC_API_KEY=your-key-here
# MODEL=anthropic/claude-haiku-5-5
```

`MODEL` is optional. The default is `anthropic/claude-haiku-5-5`.
The `.env` file is git-ignored, so your key is never committed.

## Run

```bash
python travel_planner.py
```

Example:

```
Which city? Jaipur
1. Amber Fort - hilltop fort with mirrored halls, go early
2. Hawa Mahal - the pink facade, best in morning light
3. City Palace - royal courtyards and a textile museum
```

The verbose agent output is shown above the final answer.

## Files

| File | Purpose |
| --- | --- |
| `travel_planner.py` | Agent, task, crew and run logic |
| `requirements.txt` | Python dependencies |
| `.env.example` | Template for your API key file |
| `.gitignore` | Keeps `.env`, `venv/` and caches out of git |
