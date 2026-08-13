# Persian Cars Analysts

<p align="center">
  <img src="https://img.shields.io/badge/Persian_Cars-2001--2026-blue?style=for-the-badge" alt="Persian Cars Dataset">
  <img src="https://img.shields.io/badge/Records-309-brightgreen?style=for-the-badge" alt="Records">
  <img src="https://img.shields.io/badge/Models-27-orange?style=for-the-badge" alt="Models">
</p>

<p align="center">
  <strong>📊 Comprehensive Analysis & Dataset of Iranian Cars from 2001 to 2026</strong><br>
  <em>A structured, high-quality dataset covering technical specs, emissions, and features of vehicles produced in Iran</em>
</p>

---

## 🚗 About The Project

**Persian Cars Analysts** is a data-driven project built to collect, standardize, and analyze the technical specifications of Iranian-made vehicles from **2001 to 2026** (Solar Hijri years 1380 to 1405). This dataset bridges the gap between scattered local resources and provides a unified analytical format for **market analysis, academic research, and machine learning applications**.

### ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📅 **Time Span** | 2001 – 2026 (25 years) |
| 🏭 **Manufacturers** | Iran Khodro, Saipa, Zamyad |
| 🚘 **Unique Models** | 27 distinct models |
| 📊 **Total Records** | 309 records |
| 📁 **File Format** | CSV (UTF-8) |
| 📜 **Licensing** | ODbL / MIT |

---

## 📁 Dataset Structure

| Column | Description |
|--------|-------------|
| `Year` | Production year (Gregorian) |
| `Shamsi_Year` | Production year (Solar Hijri) |
| `Manufacturer` | Automaker name (`Iran Khodro`, `Saipa`, `Zamyad`) |
| `Model` | Model name with trim level (e.g., `Dena (Turbo)`) |
| `Fuel_Type` | Fuel type (`Petrol`, `CNG`, `Petrol / CNG`, `Petrol / Hybrid`) |
| `Engine_Type` | Detailed engine specs including displacement, cylinder layout, valve count, and turbo status |
| `Power_hp` | Maximum engine power output (horsepower) |
| `Torque_Nm` | Maximum engine torque (Newton-meters) |
| `Fuel_Consumption_L100km` | Combined fuel consumption (Liters per 100 km) |
| `Acceleration_0_100_s` | 0–100 km/h acceleration time (seconds) |
| `Top_Speed_kmh` | Maximum attainable speed (km/h) |
| `CO2_Emission_g_km` | Estimated CO₂ emissions (grams per kilometer) |
| `Emission_Standard` | European emission standard (`Euro 2` through `Euro 6`) |
| `Score` | Composite quality/performance score (1–10) based on specs, safety, and market reputation |
| `Key_Options` | Highlighted safety, comfort, and drivetrain features (e.g., `ABS`, `ESC`, `6-Speed AT`) |
| `Image_URL` | Direct link to a representative vehicle image |

---

## 📊 Interesting Stats & Figures

| Stat | Value |
|------|-------|
| **Oldest Year** | 2001 (Paykan, Peugeot 206, Samand, Pride) |
| **Newest Year** | 2026 (Aria, Rira, Tara Turbo, Dena Turbo) |
| **Highest Power** | 292 hp (Rira Hybrid, 2024–2026) |
| **Lowest Power** | 63 hp (Pride, 2001–2020) |
| **Best Fuel Economy** | 5.5 L/100km (Rira Hybrid) |
| **Lowest CO₂** | 130 g/km (Rira Hybrid) |
| **Highest Score** | 9.5 (Rira Hybrid) |
| **Dominant Fuel** | Petrol (vast majority); Hybrids introduced from 2024 onward |

### Model Distribution by Manufacturer

- **Iran Khodro:** 15 models (Flagships: Tara, Dena, Rira)
- **Saipa:** 11 models (Flagships: Shahin, Aria, Saina)
- **Zamyad:** 1 model (Padra Plus)

---

## 🛠️ Methodology & Data Sources

This dataset is the result of collecting and merging data from several reputable Persian automotive sources:

- **Primary Sources:** Persian automotive portals (e.g., bama.ir, khodro45.com), manufacturer brochures, and official technical documentation.
- **Collection Method:** Manual and automated data extraction, cross-referencing, format unification, and consistency validation.
- **Quality Assurance:** Cross-checking inconsistencies, removing outliers, and normalizing measurement units.

---

## 🚀 Installation & Usage

### Prerequisites
- Python 3.7+
- pandas, numpy, matplotlib (for analysis and visualization)

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/LiamTaghizadeh/Persian_cars_Analysts.git
cd Persian_cars_Analysts

# Install dependencies (optional)
pip install pandas numpy matplotlib seaborn
```



<p align="center">
  <em>Built with ❤️ for the Iranian automotive industry</em>
</p>
