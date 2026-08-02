# 🚗 Iranian Automotive Dataset (2001–2026)

A comprehensive, structured dataset capturing the technical specifications, emission metrics, and feature sets of passenger cars manufactured by major Iranian automakers over a 25-year period. This dataset bridges the gap between scattered local data sources and a unified analytical format, suitable for market analysis, academic research, and machine learning applications.

---

## 📊 Dataset Overview

- **Time Span:** 2001 – 2026 (Gregorian) / 1380 – 1405 (Persian Solar)
- **Total Records:** 309 rows
- **Unique Models:** 27
- **Manufacturers Covered:** 3 (Iran Khodro, Saipa, Zamyad)
- **File Format:** CSV (UTF-8, comma-separated)
- **License:** Open Database License (ODbL) / MIT (choose per usage)

---

## 📁 File Structure

| Column Name | Description |
| :--- | :--- |
| `Year` | Gregorian production year (e.g., 2026) |
| `Shamsi_Year` | Persian solar calendar equivalent (e.g., 1405) |
| `Manufacturer` | Automaker name (e.g., `Iran Khodro`, `Saipa`, `Zamyad`) |
| `Model` | Vehicle model name; version information included in parentheses (e.g., `Dena (Turbo)`) |
| `Fuel_Type` | Primary fuel compatibility (`Petrol`, `CNG`, `Petrol / CNG`, `Petrol / Hybrid`) |
| `Engine_Type` | Detailed engine specifications, including displacement, cylinder layout, valve count, and turbocharging status |
| `Power_hp` | Maximum engine power output in metric horsepower |
| `Torque_Nm` | Peak engine torque in Newton-meters |
| `Fuel_Consumption_L100km` | Combined cycle fuel consumption (liters per 100 km) |
| `Acceleration_0_100_s` | 0–100 km/h acceleration time in seconds |
| `Top_Speed_kmh` | Maximum attainable speed in km/h |
| `CO2_Emission_g_km` | Estimated CO₂ emissions in grams per kilometer |
| `Emission_Standard` | European emission standard compliance (`Euro 2` to `Euro 6`) |
| `Score` | Composite quality/performance score (1–10) based on technical specs, safety, and market reputation |
| `Key_Options` | Notable safety, convenience, and drivetrain features (e.g., `ABS`, `ESC`, `6-Speed AT`) |
| `Image_URL` | Direct URL to a representative image of the vehicle (where available) |

---

## 📈 Data Summary & Statistics

| Metric | Value |
| :--- | :--- |
| **Earliest Year** | 2001 (Paykan, Peugeot 206, Samand, Pride) |
| **Latest Year** | 2026 (Ariya, Rira, Tara Turbo, Dena Turbo) |
| **Highest Power** | 292 hp (Rira Hybrid, 2024–2026) |
| **Lowest Power** | 63 hp (Pride, 2001–2020) |
| **Best Fuel Economy** | 5.5 L/100km (Rira Hybrid) |
| **Lowest CO₂** | 130 g/km (Rira Hybrid) |
| **Highest Score** | 9.5 (Rira Hybrid) |
| **Dominant Fuel** | Petrol (vast majority); hybrids introduced in 2024 |

### Model Diversity by Manufacturer
- **Iran Khodro:** 15 models (flagship: Tara, Dena, Rira)
- **Saipa:** 11 models (flagship: Shahin, Ariya, Saina)
- **Zamyad:** 1 model (Padra Plus)

---

## 🧪 Methodology & Data Sources

This dataset is a curated compilation aggregated from multiple open and authoritative Persian automotive references:

- **Primary Sources:** Persian automotive portals (e.g., bama.ir, khodro45.com), manufacturer brochures, and verified Wikipedia entries.
- **Imputation Strategy:** Values marked as `N/A` indicate that the exact figure was either unavailable or inconsistent across sources. For emissions, we applied a standard coefficient (`CO₂ ≈ Fuel_Consumption × 23.2`) to calculate estimates for missing values, ensuring logical consistency across the board.
- **Score Rationale:** The `Score` field (1–10) is a heuristic composite based on power-to-weight ratio, safety features (airbags, ESC), transmission type, and relative domestic market positioning. It serves as a quick quality indicator rather than a certified evaluation.

---

## ⚠️ Usage Notes & Limitations

1. **Estimates:** Some data points, especially for older models (pre-2010), are best-effort estimates derived from historical records.
2. **Inconsistencies:** Iranian manufacturers frequently release trim variants without distinct model names; where significant performance changes occurred (e.g., Dena Normal vs. Turbo), we split them into separate entries.
3. **Hybrid Data:** Hybrid models (Rira, Ariya) were launched recently; performance and emission figures are based on manufacturer claims and may vary in real-world testing.
4. **Image URLs:** Not all models have associated images; broken links may occur over time due to external hosting changes.

---

## 🛠️ Suggested Use Cases

- **Market Analysis:** Track the evolution of fuel consumption, power, and emissions across two decades.
- **Academic Research:** Study the adoption of Euro emission standards in developing automotive markets.
- **Predictive Modeling:** Build regression models to predict price, fuel efficiency, or emissions based on technical specs.
- **Dashboarding:** Ideal for building interactive visualizations (e.g., Power BI, Tableau) showing the Iranian automotive landscape over time.

---

## 🤝 How to Contribute

We welcome improvements to this dataset:

- Add missing models or trim levels with verifiable sources.
- Correct any erroneous technical specifications.
- Provide new image URLs for models without them.

Please fork the repository, make your changes, and submit a pull request with a clear description of your updates.


---

**Happy Analyzing!** 🚀
