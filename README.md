# 🤖 Algorithmic Market Intelligence RPA

### Strategic Pricing Automation for E-Commerce Operations

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)

---

## 📌 Overview

A comprehensive **Robotic Process Automation (RPA)** system designed to scrape real-time market data, analyze competitor positioning, and autonomously adjust product pricing strategies for Turkish e-commerce platforms.

> 💡 _Automate market research. Optimize pricing. Maximize revenue._

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Architecture](#%EF%B8%8F-architecture)
- [Modules](#-modules)
- [Installation](#%EF%B8%8F-installation)
- [Usage](#-usage)
- [Technical Stack](#%EF%B8%8F-technical-stack)
- [License](#%EF%B8%8F-license)

---

## 🏗️ Architecture

```mermaid
flowchart TB
    subgraph Input
        A[📊 Product Excel]
    end

    subgraph PriceDetective["🔍 Price Detective"]
        B[Selenium WebDriver]
        C[Multi-Platform Scraper]
        D[Price Aggregator]
    end

    subgraph Platforms["🛒 E-Commerce Platforms"]
        E1[Amazon TR]
        E2[Trendyol]
        E3[Hepsiburada]
        E4[N11]
        E5[Pazarama]
        E6[Ciceksepeti]
    end

    subgraph DiscountEngine["🏷️ Discount Automation"]
        F[Stock Analyzer]
        G[Sales Ratio Calculator]
        H[Dynamic Pricing Engine]
    end

    subgraph Output
        I[📈 Price Reports]
        J[📊 New Price List]
    end

    A --> B
    B --> C
    C --> E1 & E2 & E3 & E4 & E5 & E6
    E1 & E2 & E3 & E4 & E5 & E6 --> D
    D --> I
    A --> F
    F --> G
    G --> H
    H --> J
```

---

## 📦 Modules

This monorepo contains two independent automation modules:

### 🔍 [Price Detective](price-detective/)

Real-time competitor price monitoring across 6 major Turkish e-commerce platforms.

| Feature                    | Description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| 🔄 Multi-Platform Scraping | Amazon TR, N11, Trendyol, Hepsiburada, Pazarama, Ciceksepeti |
| 🛡️ Anti-Detection          | Cloudflare bypass & bot protection evasion                   |
| 📊 Statistical Analysis    | Min, Average, Max price calculations                         |
| 📁 Dual Output             | TXT reports + Excel summaries                                |

```bash
cd price-detective
python price_detective.py
```

---

### 🏷️ [Discount Automation](discount-automation/)

Dynamic pricing engine based on stock levels and sales velocity.

| Stock Level  | Low Sales | Medium Sales | High Sales |
| ------------ | --------- | ------------ | ---------- |
| ≤ 3 (Low)    | 10%       | -            | 5%         |
| 4-9 (Normal) | 15%       | 10%          | 5%         |
| ≥ 10 (High)  | 30%       | 20%          | 10%        |

```bash
cd discount-automation
python automatic_discount.py
```

---

## ⚙️ Installation

### Prerequisites

| Requirement    | Version                 |
| -------------- | ----------------------- |
| Python         | 3.8+                    |
| Chrome Browser | Latest                  |
| ChromeDriver   | Matching Chrome version |

### Quick Start

```bash
# Clone the repository
git clone https://github.com/isikmuhamm/algorithmic-market-intelligence-rpa.git
cd algorithmic-market-intelligence-rpa

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

### Price Surveillance

```bash
# Navigate to price detective module
cd price-detective

# Run the scraper
python price_detective.py
```

**Input:** `urunler.xlsx` (Product list with codes and names)  
**Output:** `urunler_sonuc.xlsx` + `output/*.txt`

### Automatic Discounting

```bash
# Navigate to discount automation module
cd discount-automation

# Run the pricing engine
python automatic_discount.py
```

**Input:** `urun_satis_adetleri_oranlari_stoklari.xlsx`  
**Output:** `yeni_satis_fiyatlari.xlsx`

---

## 🛠️ Technical Stack

| Category            | Technologies                           |
| ------------------- | -------------------------------------- |
| **Core Logic**      | Python 3.8+                            |
| **Web Automation**  | Selenium WebDriver (Headless Chrome)   |
| **Data Extraction** | BeautifulSoup4, Requests               |
| **Data Processing** | Pandas, OpenPyXL                       |
| **Anti-Detection**  | User-Agent rotation, Cloudflare bypass |

### Key Capabilities

| Capability                  | Description                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------- |
| 🔄 **Polymorphic Scraping** | Handles static (Amazon, N11) and dynamic JS-rendered (Trendyol, Hepsiburada) pages |
| 🤖 **Autonomous Decisions** | Evaluates sales velocity vs. stock to trigger automatic discounts                  |
| 🌐 **Cross-Platform**       | Unified tracking across fragmented marketplaces                                    |

---

## ⚖️ License

This project is licensed under the **MIT License**.

---

<div align="center">

**Designed & Developed by [@isikmuhamm](https://github.com/isikmuhamm)**

_Intelligent automation for competitive e-commerce_ 🚀

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat-square&logo=github)](https://github.com/isikmuhamm)

</div>
