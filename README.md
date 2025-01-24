# Library Management System

This project is a command-line interface (CLI) application built using Python, `pandas`, and `numpy`. It enables users to manage a library system efficiently, including adding and removing books, as well as maintaining a log of issued books. The data is stored in CSV files for easy handling and persistence.

## Features
- **Add Books**: Add new books to the library catalog.
- **Remove Books**: Remove books from the catalog.
- **Issue Books**: Record when books are issued to users.
- **Logs**: Maintain a log of all issued books in a `Issued_books.csv` file.
- **Persistent Data**: Library data is stored in a `library.csv` file.

## Project Files
1. **`project.py`**: Main Python script containing the logic for managing the library.
2. **`library.csv`**: CSV file that stores the library catalog.
3. **`Issued_books.csv`**: CSV file that logs all book issuance and return activities.

## Setup Instructions

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- `pandas` library
- `numpy` library

### Installation
1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/kartik-m39/Library-Management-System
   ```
2. Navigate to the project directory:
   ```bash
   cd Library-Management-System
   ```
3. Install the required dependencies:
   ```bash
   pip install pandas numpy
   ```

### Usage Guide
1. Run the Python script in the terminal:
   ```bash
   python project.py
   ```
2. Follow the on-screen instructions to perform actions such as adding, removing, or issuing books.
3. The library catalog (`Library.csv`) and issued books log (`Issued_books.csv`) will be automatically updated based on your actions.

## Future Scope
- **Database Integration**: Migrate the current CSV-based system to a SQL-based database for better scalability and efficiency.
- **GUI Implementation**: Develop a graphical user interface (GUI) for a more user-friendly experience.
- **Advanced Features**: Include features like user authentication, fine calculation for late returns, and more detailed reporting.

## Contribution
Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests

---

