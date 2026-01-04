# Algorithmic Market Intelligence & Dynamic Pricing Engine (RPA)

### **Strategic Pricing Automation for High-Volume E-Commerce Operations**

> **Architectural Overview:** A Python-based Robotic Process Automation (RPA) system designed to scrape real-time market data, analyze competitor positioning, and autonomously adjust product pricing strategies to maximize Buy Box retention and inventory turnover.

---

### 🏗️ System Architecture

This solution bridges the gap between **Market Data (External)** and **Business Logic (Internal)** through a modular architecture:

| Module | Functionality | Technical Approach |
| :--- | :--- | :--- |
| **Market Surveillance** | Real-time competitor monitoring | `Selenium WebDriver` & `Requests` for DOM Parsing |
| **Anti-Blocking** | Bypassing WAF/Cloudflare limits | User-Agent rotation & Headless Browser emulation |
| **Pricing Engine** | Dynamic price calculation logic | Python-based heuristic algorithms based on sales velocity |
| **Data Connector** | CRUD operations & persistence | Optimized connection handling for local/cloud databases |

---

### 🛠️ Technical Stack

* **Core Logic:** `Python 3.x`
* **Web Automation (RPA):** `Selenium` (for dynamic JS-heavy sites like Hepsiburada)
* **Data Extraction:** `BeautifulSoup4` (for static HTML parsing)
* **Network:** `Requests` (High-performance HTTP calls)
* **Browser Automation:** `Chrome Driver` (Headless/GUI modes)

---

### ⚡ Key Capabilities

1.  **Polymorphic Scraping:**
    * Handles both **Static** (N11, Amazon) and **Dynamic/JS-Rendered** (Hepsiburada, Trendyol) DOM structures seamlessly.
2.  **Autonomous Decision Making:**
    * The `Pricing Logic` module evaluates sales rates vs. competitor pricing to trigger automatic discounts without human intervention.
3.  **Cross-Platform Integration:**
    * Unified interface for tracking SKUs across multiple fragmented marketplaces.

---

### 🚀 Operational Impact

* **Efficiency:** Eliminated manual price checking for hundreds of SKUs, saving ~20 hours/week.
* **Competitiveness:** Reduced reaction time to competitor price changes from hours to minutes.
* **Revenue Optimization:** Automated "Flash Discount" logic increased conversion rates for stagnant inventory.

---

### 📦 Installation & Setup

```bash
# Clone the repository
git clone [https://github.com/isikmuhamm/algorithmic-market-intelligence-rpa.git](https://github.com/isikmuhamm/algorithmic-market-intelligence-rpa.git)

# Install dependencies
pip install -r requirements.txt

# Run the Surveillance Module
python fiyat_dedektifi.py

# Run the Auto-Discount Engine
python otomatik_indirim.py

```

### ⚖️ Disclaimer

*This project was developed for internal operational optimization and educational purposes. It demonstrates capabilities in DOM parsing, automation, and algorithmic logic.*
