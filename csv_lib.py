import os
import json
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_tools():
    tools = [
        {
            "type": "function",
            "function": {
                "name": "summarize_email",
                "description": "Summarize email content.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "escalate_complaint": {
                            "type": "boolean",
                            "description": "Indicates if this email is serious enough to be immediately escalated for further review."
                        },
                        "level_of_concern": {
                            "type": "integer",
                            "description": "Rate the level of concern for the above content on a scale from 1-10",
                            "minimum": 1,
                            "maximum": 10
                        },
                        "overall_sentiment": {
                            "type": "string",
                            "description": "The sender's overall sentiment.",
                            "enum": ["Positive", "Neutral", "Negative"]
                        },
                        "supporting_business_unit": {
                            "type": "string",
                            "description": "The internal business unit that this email should be routed to.",
                            "enum": ["Sales", "Operations", "Customer Service", "Fund Management"]
                        },
                        "summary": {
                            "type": "string",
                            "description": "A brief one-line or two-line summary of the email."
                        }
                    },
                    "required": [
                        "escalate_complaint",
                        "level_of_concern",
                        "overall_sentiment",
                        "supporting_business_unit",
                        "summary"
                    ]
                }
            }
        }
    ]
    return tools

def get_csv_response(input_content):
    tools = get_tools()
    
    messages = [
        {"role": "system", "content": "You are an AI assistant that summarizes emails and extracts key information."},
        {"role": "user", "content": f"<content>{input_content}</content>\n\nPlease use the summarize_email function to generate the email summary JSON based on the content within the <content> tags."}
    ]
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # You may want to use a more capable model if available
        messages=messages,
        tools=tools,
        tool_choice={"type": "function", "function": {"name": "summarize_email"}}
    )
    
    # Extract the function call result
    function_call = response.choices[0].message.tool_calls[0].function
    tool_result_dict = json.loads(function_call.arguments)
    
    # Convert to DataFrame and CSV
    data_frame = pd.DataFrame.from_dict([tool_result_dict])
    csv = data_frame.to_csv(index=False)
    
    return data_frame, csv

# Example usage
if __name__ == "__main__":
    sample_email = """
    Dear Customer Service,
    
    I am writing to express my extreme dissatisfaction with the recent changes to your fund management policies. 
    The new fee structure is outrageous and seems designed to take advantage of long-term investors like myself.
    If this issue is not addressed immediately, I will be forced to withdraw all my investments and seek services elsewhere.
    
    I expect a response within 24 hours.
    
    Regards,
    John Doe
    """
    
    df, csv_output = get_csv_response(sample_email)
    print("DataFrame:")
    print(df)
    print("\nCSV Output:")
    print(csv_output)