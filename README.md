# dat-editor

## Overview
`dat-editor` is a user-friendly application designed to handle and customize complex, large-sized DAT files that cannot be easily opened or manipulated in Microsoft Excel. With this tool, you can efficiently upload DAT files, select specific row ranges, view particular rows by entering IDs, and filter out fields using an intuitive right panel.

## Features
- **Upload DAT File**: Easily upload your DAT file to the application.
- **Select Row Range**: Choose the range of rows you want to view or edit.
- **View Specific Rows**: Enter an ID on the left panel to view specific rows.
- **Field Filtering**: Use the right panel to check/uncheck fields and filter the data according to your needs.

## Getting Started
Follow these steps to set up and run `dat-editor` on your local machine.

### Prerequisites
Ensure you have the following installed:
- [Python 3.x](https://www.python.org/)
- Required Python packages (listed in `requirements.txt`)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/dat-editor.git
    cd dat-editor
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
You can run the application by executing the `main.py` script:
```bash
python main.py
Alternatively, you can use PyInstaller to create an executable file:

Install PyInstaller:

bash
Copy code
pip install pyinstaller
Create the executable:

bash
Copy code
pyinstaller --onefile main.py
Run the executable:

bash
Copy code
dist/main
Usage
Upload a DAT File:
Click on the "Upload" button.
Select the DAT file from your local machine.
Select Row Range:
Use the row range selector to choose the specific range of rows you want to view or edit.
View Specific Rows:
Enter the row ID in the left panel to quickly navigate to and view a particular row.
Field Filtering:
Use the checkboxes in the right panel to filter the fields you want to display or hide.
Project Structure
gui.py: Handles the graphical user interface.
input_dat.py: Manages the input and processing of DAT files.
main.py: The main entry point of the application.
process.py: Contains the logic for processing and filtering the data.
Contributing
We welcome contributions! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions or suggestions, please feel free to reach out.

Happy Editing!

Feel free to customize it further based on any additional specifics or requirements you have for your project.
