```markdown
# Game-Analysis-API

Game-Analysis-API is a basketball analytics project designed to process game data, generate insightful predictions, and provide summaries of basketball plays using OpenAI's GPT models. The project integrates data-driven tools like the `hoopR` R package for basketball statistics and Python for machine learning and API interactions.

---

## Features

- **Basketball Data Processing:** Handles JSON-formatted play-by-play data for NBA and college basketball games.
- **GPT Integration:** Uses OpenAI's GPT models to generate natural language summaries and predictive insights based on game scenarios.
- **R Integration with `hoopR`:** Accesses robust basketball datasets for NBA and NCAA games through the `hoopR` package.
- **Custom Scripts:** Includes Python and R scripts for data preparation, analysis, and model integration.
- **API Automation:** Leverages OpenAI API for dynamic text generation tailored to basketball analytics.

---

## Installation

### Prerequisites
- Python 3.8+
- R and RStudio
- OpenAI API Key
- Required Python and R packages

### Steps to Set Up
1. Clone the repository:
   ```bash
   git clone https://github.com/abm312/Game-Analysis-API.git
   cd Game-Analysis-API
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key in the script:
   ```python
   openai.api_key = "your-openai-api-key"
   ```

---

## Usage

### Running the Python Script
1. Place your basketball game data in a JSON file (e.g., `nba_data.json`).
2. Execute the main Python script:
   ```bash
   python script2.py
   ```
3. The script will:
   - Load and process game data.
   - Format a GPT prompt based on play-by-play data.
   - Return predictions or summaries using OpenAI's API.

---

### Example

**Input:**
```json
{
  "period_display_value": "4th Quarter",
  "clock_display_value": "2:30",
  "text": "Player A scores a 3-pointer",
  "home_team_name": "Team X",
  "home_score": 102,
  "away_team_name": "Team Y",
  "away_score": 100
}
```

**Output:**
```plaintext
"In the 4th Quarter with 2:30 remaining, Player A scores a 3-pointer. Current score: Team X 102 - Team Y 100."
GPT Prediction: "This game is tightly contested. Team X should focus on defense to secure their lead."
```

---

## Repository Structure

```plaintext
Game-Analysis-API/
├── checker.py            # Script for validating data integrity.
├── code.R                # R script for data analysis with hoopR.
├── hoopr.Rproj           # RStudio project file for hoopR analysis.
├── keys.py               # File to store API keys securely.
├── script2.py            # Main Python script for GPT-based analysis.
├── requirements.txt      # List of Python dependencies.
└── README.md             # Project documentation.
```

---

## Fine-Tuning the Model

### Steps for Fine-Tuning
1. **Collect a Dataset:** Gather play-by-play data with desired outputs.
2. **Preprocess the Data:** Convert the dataset into JSONL format.
3. **Fine-Tune the Model:**
   ```bash
   openai api fine_tunes.create -t "training_data.jsonl" -m "gpt-3.5-turbo"
   ```
4. **Update the Script:**
   Replace the `model` parameter with your fine-tuned model ID:
   ```python
   response = openai.ChatCompletion.create(
       model="fine-tuned-model-id",
       messages=[{"role": "user", "content": prompt}],
       max_tokens=250
   )
   ```

---

## Future Improvements

- **Enhanced Visualization:** Add interactive charts for team and player performances.
- **Real-Time Predictions:** Integrate live data streams for real-time analysis.
- **Expanded Datasets:** Support additional leagues and historical data.
- **Fine-Tuned GPT Models:** Train models with domain-specific data for improved accuracy.

---

## Contribution

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes and push to the branch:
   ```bash
   git commit -m "Add new feature"
   git push origin feature-branch
   ```
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- OpenAI for providing the GPT models.
- `hoopR` for basketball data access.
- All contributors who helped build this project.
```
