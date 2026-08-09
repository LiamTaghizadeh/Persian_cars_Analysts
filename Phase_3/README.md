# 🚗 Persian Cars Analysts — Phase 3

**Interactive Web-Based Dashboard for Iranian Car Data Analysis & Comparison**

Phase 3 of the Persian Cars Analysts project delivers a fully interactive, client-side web application for exploring, visualizing, and comparing technical specifications of Iranian automobiles. This phase transitions the analytical backend into a user-friendly frontend experience, enabling data-driven decision-making for car buyers, enthusiasts, and automotive researchers.

---

## 📊 Project Overview

The Iranian automotive market is complex, with diverse manufacturers, models, and generational changes spanning from 1380 to 1405 (2001–2026). This dashboard simplifies the decision-making process by providing:

- **Side-by-side vehicle comparisons** with detailed technical specifications
- **Radar chart visualizations** for normalized performance metrics
- **Comprehensive vehicle exploration** with filtering by manufacturer, model, and year

All data is sourced from the Persian Cars Analysts dataset, curated and cleaned through Phases 1 and 2 of this project.

---

## 🗂️ Phase 3 Components

| File | Description |
|------|-------------|
| `compare_cars.html` | Interactive comparison tool for two vehicles. Select manufacturers, models, and production years to view technical specs side-by-side, visualize differences with a radar chart, and compare available features. |
| `virtualiza2_data.html` | Data exploration and visualization dashboard. Browse the full vehicle catalog, view aggregated statistics, and explore trends across manufacturers and model years. |
| `README.md` | This documentation file. |

---

## 🔧 Features

### 1. Vehicle Comparison (`compare_cars.html`)

- **Dual-vehicle selector**: Choose two cars independently from the database
- **Dynamic filtering**: Manufacturers populate models; models populate available years
- **Specification table**: Compare technical data (engine, dimensions, performance, etc.)
- **Radar chart**: Normalized visualization of key metrics for at-a-glance comparison
- **Features list**: Side-by-side equipment and option comparison
- **Swap button**: Quickly interchange the two vehicles
- **Reset functionality**: Clear selections with one click

### 2. Data Visualization (`virtualiza2_data.html`)

- **Full vehicle listing**: Browse all cars in the dataset
- **Interactive filters**: Refine by manufacturer, model year, or other attributes
- **Analytical insights**: View aggregated statistics and trends
- **Responsive design**: Works seamlessly on desktop and mobile devices

---

## 🛠️ Technology Stack

- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Visualization**: Chart.js or similar for radar/bar charts
- **Data Format**: JSON (embedded or fetched from external sources)
- **Deployment**: Static hosting — no server required

---

## 📁 Data Source

All vehicle data is sourced from the **Persian Cars Analysts** dataset, compiled through:

- **Phase 1**: Web scraping and data collection from Iranian automotive sources
- **Phase 2**: Data cleaning, normalization, and enrichment
- **Phase 3**: Visualization and interactive exploration

The dataset covers Iranian car manufacturers including (but not limited to):
- Iran Khodro (IKCO)
- Saipa
- Pars Khodro
- Bahman Group
- And others

**Temporal coverage**: 1380 to 1405 (2001–2026)

---

## 🚀 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Edge, Safari)
- Internet connection (for CDN-hosted chart libraries, if applicable)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/LiamTaghizadeh/Persian_cars_Analysts.git
   ```
2. Navigate to Phase 3:
   ```bash
   cd Persian_cars_Analysts/Phase_3
   ```
3. Open either HTML file directly in your browser:
   ```bash
   open compare_cars.html   # macOS
   start compare_cars.html  # Windows
   xdg-open compare_cars.html # Linux
   ```

> **Note**: No build tools or package managers are required — this is a pure static web application.

---

## 📈 Use Cases

- **Car buyers**: Compare potential purchases across brands and model years
- **Automotive journalists**: Quickly visualize and present specification differences
- **Researchers**: Analyze trends in the Iranian automotive industry over time
- **Enthusiasts**: Explore the full catalog of Iranian-produced vehicles

---

## 🔮 Future Enhancements (Phase 4+)

- [ ] Price prediction modeling using historical data
- [ ] Fuel efficiency and cost-of-ownership calculators
- [ ] Export comparison results as PDF or image
- [ ] Multi-language support (Persian/English)
- [ ] Integration with real-time market price APIs
- [ ] User accounts and saved comparisons

---

## 🤝 Contributing

Contributions are welcome! Please see the main repository guidelines for contribution workflows.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](https://github.com/LiamTaghizadeh/Persian_cars_Analysts/blob/main/LICENSE) file for details (if available).

---

## 👤 Author

**Liam Taghizadeh** — [GitHub Profile](https://github.com/LiamTaghizadeh)

---

## 🙏 Acknowledgments

- All data contributors and scrapers from Phases 1 and 2
- The Iranian automotive community for public data availability
- Open-source charting libraries that power the visualizations

---

## 📞 Contact

For questions, suggestions, or collaboration inquiries, please open an issue on the repository or reach out via GitHub.

---

**Persian Cars Analysts** — *Making Iranian automotive data accessible, visual, and actionable.*
```

---

## 📝 Summary of What We're Doing

**Phase 3** of the Persian Cars Analysts project is the **visualization and interaction layer** of a larger data pipeline. Here's what we're accomplishing:

| Aspect | Description |
|--------|-------------|
| **The Problem** | Iranian car data is scattered, unstructured, and difficult to compare across manufacturers and model years. |
| **Our Solution** | A curated, cleaned dataset (Phases 1–2) now powers an interactive web dashboard (Phase 3) that lets users explore and compare vehicles intuitively. |
| **The Tools** | Pure HTML/CSS/JavaScript with charting libraries — no backend required, making it instantly deployable and accessible. |
| **The Outcome** | Users can make informed decisions, researchers can spot trends, and enthusiasts can explore the full landscape of Iranian automobiles from 2001 to 2026. |

This phase represents the **culmination** of the data engineering work done earlier — transforming raw scraped data into a polished, user-facing product that delivers real value.
