# Business Scraping Script

This Python script scrapes business details from [India Filings](https://www.indiafilings.com/) based on a user-provided business name or type. It retrieves information like the business name, registered address, and email and stores it in an Excel file.

## Requirements

Make sure you have Python installed. You will need to install the following dependencies:

- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML content.
- `pandas`: For handling data and exporting to Excel.
- `tqdm`: For showing a progress bar during scraping.
- `openpyxl`: Required for saving the data in `.xlsx` format.

## Installation

1. Clone or download the repository to your local machine.

2. Install the required dependencies using `pip`. You can do this by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

   This will install all the necessary packages listed in the `requirements.txt` file.

## Usage

1. Run the script using Python:

   ```bash
   python main.py
   ```

   Replace `main.py` with the actual name of your Python file.

2. The script will prompt you to enter a business name or type:

   ```
   Business name/type:
   ```

3. After entering the desired business name/type, the script will scrape the relevant business details from the website and save the data to an Excel file.

4. Once the process is complete, the Excel file will be saved with the name `<business_name>.xlsx` in the same directory.

## Example

```bash
$ python main.py
Business name/type: Consulting
Scraping Business Details: 100%|██████████████████████████| 50/50 [00:10<00:00, 4.96it/s]
Scraping completed. Data saved to Consulting.xlsx
```