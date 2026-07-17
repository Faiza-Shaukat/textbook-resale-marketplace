# 📚 Textbook Resale Marketplace

A desktop GUI application built with **Python** and **Tkinter** that helps students buy and sell used textbooks within their campus community. Sellers can list books, buyers can search listings, and the app automatically suggests a fair resale price based on existing listings for the same title.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

---

## ✨ Features

- **Add Book Listings** — Sellers can list a textbook with title, author, condition, price, and seller name.
- **Live Price Suggestion** — As you type a title, the app instantly shows the average price of similar listings already in the system.
- **View All Listings** — Browse every book currently listed in a clean, sortable table view.
- **Search** — Find books instantly by title or author keyword.
- **Price Recommendation Engine** — Get a fair, data-driven price recommendation for any title based on existing listings, or a sensible default (Rs. 500) if no similar books exist.
- **Input Validation** — Friendly warnings for missing fields or invalid price entries.

---

## 🖼️ Screenshots

### Add Book Form
Sellers fill in book details, with a live price suggestion updating as they type.

![Add Book Form](screenshots/add_book_form.png)

### Book Added Confirmation
Once submitted, the new listing appears instantly in the table below the form.

![Book Added Confirmation](screenshots/book_added_confirmation.png)

### Multiple Listings View
All listed books, from multiple sellers, displayed together in one organized view.

![View All Books](screenshots/view_all_books.png)

---

## 🛠️ Tech Stack

| Component        | Technology       |
|-------------------|-----------------|
| Language          | Python 3         |
| GUI Framework     | Tkinter (`ttk` widgets) |
| Architecture      | Object-Oriented Programming (OOP) |
| Data Storage      | In-memory list (session-based) |

---

## 📂 Project Structure

```
TextbookMarketplace/
│
├── textbook_marketplace.py   # Main application source code
├── README.md                 # Project documentation
├── LICENSE                   # MIT License
├── .gitignore                # Ignored files for Git
└── screenshots/               # App screenshots used in this README
    ├── add_book_form.png
    ├── book_added_confirmation.png
    └── view_all_books.png
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher (Tkinter is included with standard Python installations)

### Installation & Running

```bash
# Clone the repository
git clone https://github.com/<your-username>/textbook-resale-marketplace.git

# Navigate into the project folder
cd textbook-resale-marketplace

# Run the application
python textbook_marketplace.py
```

No external dependencies are required — the project uses only Python's built-in `tkinter` module.

---

## 🧩 How It Works

1. **Add Book tab** — Enter the book's details. As soon as you type a title that matches an existing listing, the app shows a live-updating recommended price.
2. **View All tab** — See every book listed so far in a scrollable table.
3. **Search tab** — Type any keyword to filter listings by title or author.
4. **Price Recommendation tab** — Enter any book title to get an average price based on current listings, or a default suggestion if it's a new title.

---

## 🔍 Core Concepts Used

- Object-Oriented Programming (`Book` and `TextbookMarketplace` classes)
- Tkinter `ttk.Notebook` for tabbed navigation
- `ttk.Treeview` for tabular data display
- Event-driven programming (`<KeyRelease>` binding for live updates)
- List comprehensions for filtering and searching
- Basic input validation and user feedback via `messagebox`

---

## 📌 Future Improvements

- Persistent storage using SQLite or a JSON file
- Book image uploads
- Buyer contact/messaging system
- Category-based filtering (by subject/course)

---

## 👩‍💻 Author

**Faiza Shaukat**
BS Artificial Intelligence, University of Haripur
Built as part of a software development internship project.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
