import csv
from jinja2 import Template  # You might need to install the 'jinja2' library

# Load the HTML template
with open('email_template.html', 'r') as template_file:
    template_content = template_file.read()
    email_template = Template(template_content)

# Read employee data from CSV and generate email signatures
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        # Define fields from the CSV row
        name = row['Name']
        job_title = row['Job Title']
        email = row['Email']
        phone = row['Phone']
        
        # Render the email signature using the template
        email_signature = email_template.render(
            name=name,
            job_title=job_title,
            email=email,
            phone=phone
        )
        
        # Save the email signature to a file
        signature_filename = f'{name.replace(" ", "_").lower()}_signature.html'
        with open(signature_filename, 'w') as signature_file:
            signature_file.write(email_signature)

print("Email signatures generated successfully.")
