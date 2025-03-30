Stock-Support-Resistance

📚 Project Overview

This project is a Python-based stock price analyzer that identifies Support and Resistance (S&R) levels using local extrema and moving averages. It generates buy, sell, or hold signals based on proximity to these key levels and visualizes results.

🚀 Features
 - Stock Data Retrieval: Retrieves NSE stock data using yfinance.

 - Moving Averages Calculation: Computes 50-day and 200-day moving averages.

 - Support & Resistance Detection: Identifies key levels with local minima and maxima.

 - Signal Generation: Provides buy/sell/hold suggestions based on price trends.

 - Output Files:

 - PNG Chart: Displays refined S&R levels.

 - Excel File: Contains stock data with the chart embedded.


🛠️ Tech Stack

 - Language: Python

 - Libraries:

    ->  pandas – For data manipulation

   ->  numpy – For numerical operations

   ->  matplotlib – For data visualization

   ->  yfinance – For retrieving stock data

   ->  scipy – For detecting local extrema

   ->  xlsxwriter – For exporting data to Excel


 File Structure
 
    Stock-Support-Resistance
    ├── sample_chart_img_op.png   # Sample output chart
    ├── sample_excel_op.xlsx      # Sample output Excel file
    ├── stock_analysis.py         # Main Python script
    └── README.md                 # Project documentation


▶️ Usage
1. Run the Script : 
    python stock_analysis.py
2. Enter the Stock Symbol:

Example: TCS, RELIANCE, INFY.

3. Check Output Files:

PNG chart and Excel file will be saved in the directory.


📊 Output Samples
 - Chart: TCS_Final_Support_Resistance.png (or any stock symbol entered)

 - Excel File: TCS_stock_data.xlsx (or any stock symbol entered)



💡 Applications : 
  - Swing trading and short-term trading strategies.

 - Stock price trend analysis for NSE-listed stocks.

⚠️ Important Notes
 - The analysis considers the last 1-year stock data to detect accurate S&R levels.

 - Designed specifically for NSE-listed stocks.

📝 License
 - This project is open-source and available under the MIT License.
