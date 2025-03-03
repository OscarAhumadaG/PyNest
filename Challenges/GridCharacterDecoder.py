"""
Challenge: Grid Character Decoder

Objective:
The goal of this challenge is to extract and display a hidden message from a Google Doc containing a structured table.
The table includes character positions in a 2D grid, and the challenge requires reconstructing and printing the correctly
oriented characters to reveal the encoded message.

Input Specifications:
- The input is a publicly accessible Google Doc URL.
- The document contains a table with three columns:
  1. X Coordinate – The horizontal position of the character.
  2. Character – An uppercase letter to be placed in the grid.
  3. Y Coordinate – The vertical position of the character.

Output Specifications:
- The program should generate a visual representation of the grid with correctly positioned characters.
- The final output should display the decoded message by reading the letters in the correct order.

Technical Requirements:
- The solution must be implemented in Python (preferred) or JavaScript.
- External libraries can be used.
- The program should contain a function that:
  1. Accepts a Google Doc URL as an argument.
  2. Extracts the table data and processes it into a 2D grid.
  3. Prints the reconstructed message.

Example Test Case:
Using the following input document:
https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub

The expected output is a properly formatted grid of characters revealing the hidden message.
"""

import requests
from bs4 import BeautifulSoup


def fetch_data_from_google_doc(url):
    """
    Fetches the document from the Google Docs URL and returns the content.
    """
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch the document. Status code: {response.status_code}")
        return None

    return response.text


def build_grid_from_data(data):
    """
    Builds the 2D grid from the parsed data and returns the grid.
    """
    grid = {}
    max_x = 0
    max_y = 0

    # Using BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(data, 'html.parser')

    # Find the table
    table = soup.find('table')

    # Iterate over the rows of the table
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cols = row.find_all('td')

        if len(cols) != 3:
            continue  # Skip rows that do not have exactly 3 columns

        x = int(cols[0].text.strip())
        char = cols[1].text.strip()
        y = int(cols[2].text.strip())

        # Update max_x and max_y to determine grid dimensions
        max_x = max(max_x, x)
        max_y = max(max_y, y)

        # Place character at the specified position in the grid
        grid[(x, y)] = char

    # Initialize a grid with spaces (max_x + 1 and max_y + 1 for 0-based indexing)
    grid_2d = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill grid with characters
    for (x, y), char in grid.items():
        grid_2d[y][x] = char

    return grid_2d


def print_grid(grid_2d):
    """
    Prints the 2D grid in a human-readable format.
    """
    for row in grid_2d:
        print(''.join(row))


def create_staircase(url):
    """
    Main function to fetch data from Google Doc, build grid, and print the result.
    """
    data = fetch_data_from_google_doc(url)

    # Check if we got the content, and if the content has the data we expect
    if not data:
        print("No data fetched from the URL.")
        return

    grid_2d = build_grid_from_data(data)
    print_grid(grid_2d)


# URL provided for testing
url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'

# Run the function with the provided URL
create_staircase(url)

