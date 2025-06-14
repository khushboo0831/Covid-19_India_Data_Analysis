### COVID-19 India Statewise Data Analysis

📌 **Project Overview**
This project offers a detailed Exploratory Data Analysis (EDA) and visualization of India’s statewise COVID-19 data to evaluate the pandemic’s spread, severity, and outcomes. By integrating statistical summaries, interactive geospatial maps, and correlation analysis, it aims to provide meaningful insights that can guide healthcare policy and public awareness.

---

### 🎯 **Objectives**

* Clean and preprocess real-time COVID-19 statewise data
* Analyze and visualize trends in confirmed, active, discharged, and fatal cases
* Study ratio-based metrics (death, recovery, active) across states
* Use interactive visualizations to draw comparative insights
* Detect patterns using correlation and geographic heatmaps

---

### 📂 **Dataset Details**

* **Source**: Real-world COVID-19 India Statewise CSV dataset
* **Total Records**: All Indian states and union territories
* **Key Attributes**:

  * `State/UTs` – State or union territory name
  * `Total Cases`, `Active`, `Discharged`, `Deaths`
  * `Active Ratio`, `Discharge Ratio`, `Death Ratio` (in %)

---

### ⚙️ **Tools & Libraries Used**

* **Python**, **Pandas**, **NumPy** – Data wrangling
* **Matplotlib**, **Seaborn**, **Plotly Express** – Visualizations
* **GeoJSON & Plotly Choropleth** – Map-based interactive charts

---

### 📊 **Key Analysis & Visuals**

#### ✅ **Data Preprocessing**

* Removed duplicate entries and standardized long state names
* Handled missing values and ensured numerical consistency
* Computed additional ratio-based metrics for deeper insights

#### 🖼️ **Visualizations Included**

* **Bar Plots**: Top states by cases and deaths
* **Pie Charts**: Share of cases, deaths, and recoveries
* **Scatter Plots**: Active vs Death ratios, Total vs Active
* **Heatmaps**: Feature correlation matrix
* **Choropleth Maps**: Visual statewise distribution on India’s map
* **Pair Plots**: Metric relationships
* **Histograms**: Spread of ratios across states

---

### 📈 **Statistical Highlights**

* **Most Affected**: Maharashtra (highest total cases)
* **Least Affected**: Lakshadweep, Daman & Diu
* **Highest Active Ratio**: Mizoram
* **Highest Death Ratio**: Punjab (\~2.72%)
* **Best Recovery Rates**: Multiple states with over 98% discharge ratio
* 50%+ of total cases are concentrated in just a few key states

---

### 💡 **Future Enhancements**

* Integrate time-series trends for dynamic monitoring
* Add vaccination and testing data for broader context
* Deploy dashboard using **Streamlit** or **Dash**
* Extend to predictive modeling for forecasting case growth

---

### 👩‍💻 **Author**

**Khushboo Verma**
This project showcases the use of Python-based EDA, geospatial visualization, and health data analysis for making informed, data-driven decisions during a public health crisis.

