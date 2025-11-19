import re
import os

# Define file names
INPUT_FILE_NAME = "source_text.txt"
OUTPUT_FILE_NAME = "extracted_emails.txt"

def create_example_file(filename):
    """Creates a sample file for testing if it doesn't exist."""
    if not os.path.exists(filename):
        print(f"Creating a sample file '{filename}' for demonstration...")
        sample_content = (
            "Hello, this is a document with various contacts.\n"
            "You can reach me at john.doe@example.com for general inquiries.\n"
            "For urgent matters, please use support@company-xyz.org.\n"
            "Contact our sales team: sales@widgetcorp.io or sales-backup@widgetcorp.io\n"
            "This text has some false positives like test.txt and not_email@.com but we only want valid ones.\n"
            "Another email: user123@sub.domain.net\n"
        )
        try:
            with open(filename, 'w') as f:
                f.write(sample_content)
            print(f"Sample content written to '{filename}'.")
        except IOError:
            print(f"Error: Could not create the sample file {filename}.")
            return False
    return True

def extract_emails_from_file(input_filename, output_filename):
    """
    Reads the input file, extracts emails using regex, and writes them to the output file.
    
    Key Concepts Used: re, file handling
    """
    
    # 1. Read the input file content
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"\n❌ Error: Input file '{input_filename}' not found.")
        print("Please ensure the file exists in the same directory.")
        return
    except IOError:
        print(f"\n❌ Error: Could not read file '{input_filename}'. Check permissions.")
        return

    # 2. Key Concept: Regular Expressions (re)
    # Regex to match a standard email pattern:
    # [A-Za-z0-9._%+-]+   <- one or more word characters, periods, etc.
    # @                 <- the @ symbol
    # [A-Za-z0-9.-]+     <- domain name (letters, numbers, periods)
    # \.                <- a literal period
    # [A-Z|a-z]{2,}       <- top-level domain (e.g., com, net, org)
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    
    # Find all matches in the content
    found_emails = re.findall(email_pattern, content)
    
    # 3. Use a set to store unique emails (removes duplicates automatically)
    unique_emails = set(found_emails)
    
    # 4. Write the unique emails to the output file
    try:
        # Key Concept: file handling
        with open(output_filename, 'w') as f:
            for email in sorted(list(unique_emails)):
                f.write(email + '\n')
        
        print("\n" + "="*50)
        print(f"✅ Automation Complete!")
        print(f"Total unique emails found: **{len(unique_emails)}**")
        print(f"Emails successfully saved to **{output_filename}**")
        print(f"Emails found: {', '.join(sorted(list(unique_emails)))}")
        print("="*50)
        
    except IOError:
        print(f"\n❌ Error: Could not write to the file '{output_filename}'. Check permissions.")


if __name__ == "__main__":
    # Ensure the input file exists for testing
    if create_example_file(INPUT_FILE_NAME):
        extract_emails_from_file(INPUT_FILE_NAME, OUTPUT_FILE_NAME)