# MailMind

MailMind is an AI-powered email analysis tool that summarizes content, assesses sentiment, and routes messages intelligently. Using OpenAI's API, it extracts key information, determines urgency, and provides actionable insights to streamline your inbox management and enhance communication efficiency.

## Features

- Email content summarization
- Sentiment analysis
- Urgency assessment
- Intelligent routing to business units
- CSV output for easy integration

## Requirements

- Python 3.7+
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/bdeva1975/MailMind.git
   cd MailMind
   ```

2. Install required packages:
   ```
   pip install openai pandas python-dotenv
   ```

3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Import the necessary functions:
   ```python
   from mailmind import get_csv_response
   ```

2. Use the `get_csv_response` function to analyze an email:
   ```python
   email_content = """
   Dear Customer Service,
   
   I am writing to express my extreme dissatisfaction with the recent changes to your fund management policies. 
   The new fee structure is outrageous and seems designed to take advantage of long-term investors like myself.
   If this issue is not addressed immediately, I will be forced to withdraw all my investments and seek services elsewhere.
   
   I expect a response within 24 hours.
   
   Regards,
   John Doe
   """
   
   df, csv_output = get_csv_response(email_content)
   print(df)
   print(csv_output)
   ```

## Output

The function returns a pandas DataFrame and a CSV string containing the following information:

- Escalation status (boolean)
- Level of concern (1-10)
- Overall sentiment (Positive/Neutral/Negative)
- Supporting business unit
- Brief summary

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for providing the powerful GPT models
- Pandas library for data manipulation

## Contact

For any questions or feedback, please open an issue in the GitHub repository.
