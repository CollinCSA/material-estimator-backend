# Material Estimator Backend

## Setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Place your `creds.json` in the same directory.

3. Run the app:

```
python app.py
```

## API

- `GET /projects` – returns all projects from the Google Sheet
- `POST /save_project` – saves a new project (JSON payload)

## Example JSON for /save_project

```
{
  "Project ID": "CSA-001",
  "Project Name": "Mesa Site A",
  "Structure Type": "Type 1",
  "Materials": "EMT 1\" - 80'; LT 1\" - 45'",
  "Total Cost": "$1,250",
  "Best Vendor Map": "{\"EMT 1\": \"IES\"}",
  "Notes": "Urgent turnaround"
}
```