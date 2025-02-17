import gspread
from oauth2client.service_account import ServiceAccountCredentials
from youtube_transcript_api import YouTubeTranscriptApi
import time

# Google Sheets API Setup
SPREADSHEET_ID = "1JvaDTagk5P7xogc8JFcsCpjuQd5M4Sitkg5S4z-VK9Q"  # Replace with your Google Sheet ID
CREDENTIALS_FILE = "xyz.json"  # Your service account key file

# Authenticate & connect to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)

# Open Google Sheet using ID
sheet = client.open_by_key(SPREADSHEET_ID).sheet1  # Use first sheet

# Function to extract video ID from URL
def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]  # Handle extra parameters
    return None

# Function to fetch YouTube transcript
def get_transcript(video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        return "Invalid URL"

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = "\n".join([entry["text"] for entry in transcript])
        return transcript_text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to update Google Sheets automatically
def update_sheet():
    rows = sheet.get_all_values()  # Fetch all rows
    for i, row in enumerate(rows[1:], start=2):  # Skip header row (start at row 2)
        youtube_link = row[0]  # Column A (YouTube link)
        transcript = row[1] if len(row) > 1 else ""  # Column B (Transcript)

        if youtube_link and not transcript:  # If a link is present and transcript is missing
            print(f"📌 Processing: {youtube_link}")
            transcript_text = get_transcript(youtube_link)
            sheet.update_cell(i, 2, transcript_text)  # Write transcript to Column B
            print(f"✅ Updated Row {i} with Transcript")

            time.sleep(2)  # Avoid hitting API rate limits

# Run the function to update the sheet
update_sheet()

# Print all available Google Sheets for debugging
sheets = client.openall()
print("🔹 Available Google Sheets:")
for s in sheets:
    print(f"- {s.title}")
