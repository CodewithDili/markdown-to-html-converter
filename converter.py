import markdown
import os

def markdown_to_html(input_file, output_file):
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"The file {input_file} does not exist.")
        return

    # Read the Markdown file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Convert Markdown to HTML
    html = markdown.markdown(text)

    # Write the HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html)

    print(f"Markdown has been successfully converted to HTML and saved as {output_file}.")

if __name__ == "__main__":
    input_file = 'sample.md'  # The Markdown file you want to convert
    output_file = 'output.html'  # The HTML output file
    markdown_to_html(input_file, output_file)
