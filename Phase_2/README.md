# Persian Cars Analysts – Android App

<p align="center">
  <img src="https://img.shields.io/badge/platform-Android-green?style=for-the-badge" alt="Platform">
  <img src="https://img.shields.io/badge/Kivy-2.1.0-blue?style=for-the-badge" alt="Kivy">
  <img src="https://img.shields.io/badge/SQLite-lightgrey?style=for-the-badge" alt="SQLite">
  <img src="https://img.shields.io/badge/license-MIT%20%2F%20ODbL-yellow?style=for-the-badge" alt="License">
</p>

<p align="center">
  <strong>📱 Offline Android App for Browsing, Searching, and Analysing Iranian Cars (2001–2026)</strong><br>
  <em>Lightweight • Fast • Built with Kivy – Data synced from the Persian Cars Analysts dataset</em>
</p>

---

## 📖 About This App

This is an **Android application** built with [Kivy](https://kivy.org/) that provides a beautiful, offline-first interface for exploring the **Persian Cars Analysts** dataset. It downloads the dataset from the official GitHub repository on first launch, stores it in a local SQLite database, and keeps it up‑to‑date with a single tap.

The app mirrors the functionality of the interactive HTML dashboard (`virtualiza2_data.html`) but is optimised for mobile devices – smooth scrolling, image previews, instant search, and filterable results.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📥 **First‑run Auto‑Sync** | Downloads the latest CSV data from GitHub and stores it in SQLite |
| 🔄 **One‑Tap Update** | Refreshes the database with new records from the repository |
| 🔍 **Smart Search** | Search across all fields (manufacturer, model, fuel type, engine, etc.) |
| 🧹 **Filter by Field** | Filter results specifically by Manufacturer / Model / Fuel Type |
| 🖼️ **Vehicle Images** | Displays representative images for each car (if available) |
| 📊 **Compact Cards** | Each vehicle appears as a neat card showing: specs, score, engine type, key options |
| ⚡ **Lightweight** | No heavy dependencies – runs smoothly even on low‑end Android devices |
| 📁 **Offline First** | Once data is synced, the app works entirely offline |
| 🗄️ **SQLite Powered** | Efficient local storage with unique constraint and easy querying |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+** (for development & building)
- **Kivy 2.1.0** (and its dependencies)
- **Buildozer** (for packaging APK)
- **Android SDK** / **JDK** (managed by Buildozer)

### Quick Start (Development)

```bash
# Clone this repository
git clone https://github.com/LiamTaghizadeh/Persian_cars_Analysts.git
cd Persian_cars_Analysts/Phase_1/AndroidApp

# Install required packages
pip install kivy requests

# Run the app on your desktop (for testing)
python main.py
```

### Build APK (Android)

```bash
# Install buildozer if you haven't
pip install buildozer

# Initialise the buildozer spec file
buildozer init

# Build the debug APK (this takes a few minutes)
buildozer android debug deploy run

# The APK will be located in the bin/ folder:
# bin/PersianCars-1.0.0-debug.apk
```

---

## 📱 Screenshots (Mock‑up)

```
+---------------------------+
| 🚗 Iranian Cars 1380–1405 | 🔄  |
| [Search...  ] [Filter ▼]  |
| [🔍] [✕]                  |
| Count: 309 vehicles       |
|                           |
| +-----------------------+ |
| | 🖼️  | Iran Khodro    | |
| |     | Tara (Turbo)    | |
| |     | 1402 (2023)     | |
| |     | Fuel: Petrol    | |
| |     | ★★★★★ 8.7/10   | |
| |     | ⚡162hp 🔧215Nm | |
| |     | ⓿6.8L/100km    | |
| |     | 🚀9.2s 💨205km/h| |
| |     | Engine: 1.7L I4 | |
| |     | Options: ABS... | |
| +-----------------------+ |
| +-----------------------+ |
| | 🖼️  | Saipa           | |
| |     | Shahin (GT)     | |
| |     | 1403 (2024)     | |
| |     | ...             | |
| +-----------------------+ |
|         ...               |
+---------------------------+
```

> *The actual app uses Kivy’s native widgets and loads real images from the web.*

---

## 🗄️ Database Structure

The app uses a local **SQLite** database with the following schema:

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Auto‑increment primary key |
| `Year` | INTEGER | Production year (Gregorian) |
| `Shamsi_Year` | INTEGER | Production year (Solar Hijri) |
| `Manufacturer` | TEXT | Car manufacturer (`Iran Khodro`, `Saipa`, `Zamyad`) |
| `Model` | TEXT | Model name with trim (e.g., `Dena (Turbo)`) |
| `Fuel_Type` | TEXT | `Petrol`, `CNG`, `Petrol / CNG`, `Petrol / Hybrid` |
| `Engine_Type` | TEXT | **Detailed engine specification** (e.g., `1.6L I4, 16‑valve, Turbo`) |
| `Power_hp` | REAL | Horsepower |
| `Torque_Nm` | REAL | Torque in Newton‑meters |
| `Fuel_Consumption_L100km` | REAL | Combined fuel consumption (L/100 km) |
| `Acceleration_0_100_s` | REAL | 0‑100 km/h time (seconds) |
| `Top_Speed_kmh` | REAL | Maximum speed (km/h) |
| `CO2_Emission_g_km` | REAL | Estimated CO₂ emission (g/km) |
| `Emission_Standard` | TEXT | Euro standard (`Euro 2` – `Euro 6`) |
| `Score` | REAL | Composite quality score (1‑10) |
| `Key_Options` | TEXT | Safety & comfort features (e.g., `ABS, ESC, 6‑Speed AT`) |
| `Image_URL` | TEXT | Direct URL to vehicle image |

> **Unique constraint** on `(Year, Manufacturer, Model)` – prevents duplicate entries and simplifies updates.

---

## 🔧 How It Works

1. **First Launch** – The app checks if the `cars` table is empty. If so, it downloads the CSV from:
   ```
   https://raw.githubusercontent.com/LiamTaghizadeh/Persian_cars_Analysts/main/Phase_1/iranian_cars_final.csv
   ```
2. **Data Import** – The CSV is parsed, each row is inserted (or replaced) into the SQLite database.
3. **Local Storage** – All subsequent launches use the local SQLite data – no internet required.
4. **Update** – The user can tap the **🔄 Update** button at any time to re‑fetch the latest CSV and refresh the database.
5. **Search & Filter** – Users can type a query and optionally restrict the search to a specific column (Manufacturer, Model, or Fuel Type). The app filters the data in real time.
6. **Display** – Each car is presented as a card containing image, basic info, specs, engine type, and key options.

---

<p align="center">
  <em>Built with ❤️ for the Iranian automotive community</em>
</p>
