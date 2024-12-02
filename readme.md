
# Financial Management System

A comprehensive and user-friendly Financial Management System built using **Streamlit**, designed to help users effectively manage and analyze their finances. The system provides an intuitive dashboard, advanced financial insights, and tools to optimize income and expenses.

---

## **Features**

### **1. Dashboard**
- Interactive overview of your finances.
- Visualizations for income and expenses.
- Real-time metrics:
  - **Total Income**
  - **Total Expenses**
  - **Net Income**

### **2. Transactions**
- Add, manage, and view transactions.
- Categorize transactions as **Income** or **Expense**.
- Recent transactions displayed in an easy-to-use table.

### **3. Reports**
- Generate detailed financial reports:
  - **Income Statement**
  - **Category Analysis**
  - **Custom Reports**
- Export data as a CSV for offline use.

### **4. Accounts**
- Manage multiple accounts:
  - Categories: **Assets**, **Liabilities**, **Income**, and **Expenses**.
  - Add and organize accounts easily.

### **5. AI Insights (Gemini Integration)**
- AI-powered financial analysis:
  - **Spending Trends**: Identify patterns in your transactions.
  - **Cost-saving Suggestions**: AI-based recommendations for better financial planning.

### **6. Settings**
- Configure your default **currency** and **date format**.
- Export transaction data for backup or analysis.

---

## **Technology Stack**

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Visualization**: [Plotly](https://plotly.com/)
- **Data Management**: Pandas
- **AI Module**: Gemini-based insights
- **Configuration**: dotenv for environment variables

---

## **Installation Guide**

### **Prerequisites**
- Python 3.7 or later installed on your system.
- Streamlit installed (`pip install streamlit`).

---

### **Steps to Set Up**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/financial-manager.git
   cd financial-manager
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   ```bash
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

4. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**
   - Create a `.env` file in the root of the project directory.
   - Add the following variables:
     ```plaintext
     DEFAULT_CURRENCY=USD
     DATE_FORMAT=MM/DD/YYYY
     ```

6. **Run the Application**
   ```bash
   streamlit run app.py
   ```

7. **Access the App**
   - Open your browser and go to `http://localhost:8501`.

---

## **Usage**

1. Navigate through the sidebar to access:
   - **Dashboard**: Get an overview of your finances.
   - **Transactions**: Add or review past transactions.
   - **Reports**: Generate and analyze financial data.
   - **AI Insights**: Gain actionable suggestions to optimize your spending.
   - **Settings**: Customize app configurations.

2. Add transactions and let the AI module provide insights for improved financial management.

---

## **Folder Structure**

```
financial_manager/
├── .env                # Environment variables
├── .gitignore          # Ignore unnecessary files
├── app.py              # Main application entry point
├── requirements.txt    # Python dependencies
├── utils/              # Helper modules
│   ├── __init__.py     # For module support
│   ├── ai_module.py    # AI insights logic
│   ├── data_handler.py # Transaction and data management logic
│   ├── charts.py       # Visualization creation logic
│   ├── config.py       # Configuration handler
```

---

## **Key Functionalities**

### **Dashboard**
- Real-time summaries and visualizations.
- Easy-to-understand financial metrics.

### **Reports**
- AI-driven financial summaries.
- Exportable custom reports.

### **AI-Powered Insights**
- Gain actionable financial advice based on your habits.

---

## **Contributing**

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature-name"`.
4. Push to the branch: `git push origin feature-name`.
5. Create a pull request.

---

## **License**

This project is licensed under the **GPL License**. See the `LICENSE` file for details.

---

## **Screenshots**

### **Dashboard Overview**
![Dashboard](https://via.placeholder.com/800x400?text=Dashboard+Screenshot)

### **AI Insights**
![AI Insights](https://via.placeholder.com/800x400?text=AI+Insights+Screenshot)

---

## **Contact**

For questions or support, feel free to contact:
- **Email**: 23207001@apsit.edu.in
- **GitHub**: [your-username](https://github.com/HarshTambade)

```

---

