"""
Textbook Resale Marketplace
----------------------------
A desktop GUI application built with Python and Tkinter that allows students
to list, browse, search, and get fair price recommendations for used textbooks.

Author: Faiza Shaukat
"""

import tkinter as tk
from tkinter import ttk, messagebox


class Book:
    """Represents a single textbook listing in the marketplace."""

    def __init__(self, title, author, condition, price, seller):
        self.title = title
        self.author = author
        self.condition = condition
        self.price = float(price)
        self.seller = seller


class TextbookMarketplace:
    """Main application class that builds and manages the Tkinter GUI."""

    def __init__(self, root):
        self.root = root
        self.root.title("Textbook Resale Marketplace")
        self.root.geometry("850x700")
        self.books = []

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        self.tab_add = ttk.Frame(self.notebook)
        self.tab_view = ttk.Frame(self.notebook)
        self.tab_search = ttk.Frame(self.notebook)
        self.tab_recommend = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_add, text="Add Book")
        self.notebook.add(self.tab_view, text="View All")
        self.notebook.add(self.tab_search, text="Search")
        self.notebook.add(self.tab_recommend, text="Price Recommendation")

        self.setup_add_tab()
        self.setup_view_tab()
        self.setup_search_tab()
        self.setup_recommend_tab()

    def setup_add_tab(self):
        frame = ttk.Frame(self.tab_add, padding=20)
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text="Title:").grid(row=0, column=0, sticky='w', pady=5)
        self.title_entry = ttk.Entry(frame, width=40)
        self.title_entry.grid(row=0, column=1, pady=5)
        self.title_entry.bind('<KeyRelease>', self.update_recommendation_live)

        ttk.Label(frame, text="Author:").grid(row=1, column=0, sticky='w', pady=5)
        self.author_entry = ttk.Entry(frame, width=40)
        self.author_entry.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Condition:").grid(row=2, column=0, sticky='w', pady=5)
        self.condition_combo = ttk.Combobox(
            frame, values=["New", "Like New", "Good", "Fair", "Poor"], width=37
        )
        self.condition_combo.grid(row=2, column=1, pady=5)
        self.condition_combo.current(0)

        ttk.Label(frame, text="Price (Rs):").grid(row=3, column=0, sticky='w', pady=5)
        self.price_entry = ttk.Entry(frame, width=40)
        self.price_entry.grid(row=3, column=1, pady=5)

        ttk.Label(frame, text="Seller Name:").grid(row=4, column=0, sticky='w', pady=5)
        self.seller_entry = ttk.Entry(frame, width=40)
        self.seller_entry.grid(row=4, column=1, pady=5)

        self.recommend_label = ttk.Label(
            frame, text="💡 Enter title to see recommended price", foreground="blue"
        )
        self.recommend_label.grid(row=5, column=0, columnspan=2, pady=10)

        add_btn = ttk.Button(frame, text="Add Book", command=self.add_book)
        add_btn.grid(row=6, column=0, columnspan=2, pady=10)

    def update_recommendation_live(self, event=None):
        title = self.title_entry.get().strip()
        if not title:
            self.recommend_label.config(text="💡 Enter title to see recommended price")
            return
        same_title = [b for b in self.books if b.title.lower() == title.lower()]
        if same_title:
            avg = sum(b.price for b in same_title) / len(same_title)
            self.recommend_label.config(
                text=f"✅ Recommended price: Rs. {avg:.2f} (based on {len(same_title)} books)"
            )
        else:
            self.recommend_label.config(text="ℹ️ No similar books. Default suggestion: Rs. 500")

    def add_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        condition = self.condition_combo.get()
        price_text = self.price_entry.get().strip()
        seller = self.seller_entry.get().strip()

        if not title or not author or not price_text or not seller:
            messagebox.showwarning("Missing Info", "Please fill in all fields.")
            return
        try:
            price = float(price_text)
        except ValueError:
            messagebox.showerror("Invalid Price", "Price must be a number.")
            return

        book = Book(title, author, condition, price, seller)
        self.books.append(book)

        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.seller_entry.delete(0, tk.END)
        self.condition_combo.current(0)

        self.recommend_label.config(text="✅ Book added! You can add another.")
        self.refresh_view()

    def setup_view_tab(self):
        frame = ttk.Frame(self.tab_add, padding=10)
        frame.pack(fill='both', expand=True)

        self.tree = ttk.Treeview(
            frame, columns=("Title", "Author", "Condition", "Price", "Seller"), show='headings'
        )
        for col, width in [("Title", 150), ("Author", 150), ("Condition", 100),
                            ("Price", 100), ("Seller", 150)]:
            self.tree.heading(col, text=col if col != "Price" else "Price (Rs)")
            self.tree.column(col, width=width)

        scrollbar = ttk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

    def refresh_view(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for book in self.books:
            self.tree.insert(
                "", tk.END,
                values=(book.title, book.author, book.condition, f"{book.price:.2f}", book.seller)
            )

    def setup_search_tab(self):
        frame = ttk.Frame(self.tab_search, padding=20)
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text="Search keyword:").grid(row=0, column=0, pady=5)
        self.search_entry = ttk.Entry(frame, width=40)
        self.search_entry.grid(row=0, column=1, pady=5)
        search_btn = ttk.Button(frame, text="Search", command=self.perform_search)
        search_btn.grid(row=0, column=2, padx=10, pady=5)

        self.search_tree = ttk.Treeview(
            frame, columns=("Title", "Author", "Condition", "Price", "Seller"), show='headings'
        )
        for col, width in [("Title", 150), ("Author", 150), ("Condition", 100),
                            ("Price", 100), ("Seller", 150)]:
            self.search_tree.heading(col, text=col if col != "Price" else "Price (Rs)")
            self.search_tree.column(col, width=width)

        scrollbar = ttk.Scrollbar(frame, orient='vertical', command=self.search_tree.yview)
        self.search_tree.configure(yscrollcommand=scrollbar.set)
        self.search_tree.grid(row=1, column=0, columnspan=3, sticky='nsew', pady=10)
        scrollbar.grid(row=1, column=3, sticky='ns')

        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)

    def perform_search(self):
        keyword = self.search_entry.get().strip().lower()
        if not keyword:
            messagebox.showinfo("Search", "Please enter a keyword.")
            return
        matches = [b for b in self.books if keyword in b.title.lower() or keyword in b.author.lower()]
        for row in self.search_tree.get_children():
            self.search_tree.delete(row)
        for book in matches:
            self.search_tree.insert(
                "", tk.END,
                values=(book.title, book.author, book.condition, f"{book.price:.2f}", book.seller)
            )
        if not matches:
            messagebox.showinfo("Search", "No matching books found.")

    def setup_recommend_tab(self):
        frame = ttk.Frame(self.tab_recommend, padding=20)
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text="Enter book title:").pack(pady=5)
        self.rec_title_entry = ttk.Entry(frame, width=40)
        self.rec_title_entry.pack(pady=5)
        rec_btn = ttk.Button(frame, text="Get Recommended Price", command=self.show_recommendation)
        rec_btn.pack(pady=5)

        self.rec_result_label = ttk.Label(
            frame, text="Result will appear here", font=('Arial', 12), foreground="green"
        )
        self.rec_result_label.pack(pady=20)

    def show_recommendation(self):
        title = self.rec_title_entry.get().strip()
        if not title:
            messagebox.showwarning("Error", "Please enter a title.")
            return
        same_title = [b for b in self.books if b.title.lower() == title.lower()]
        if same_title:
            avg = sum(b.price for b in same_title) / len(same_title)
            self.rec_result_label.config(
                text=f"📊 Average price for '{title}': Rs. {avg:.2f} (based on {len(same_title)} books)"
            )
        else:
            self.rec_result_label.config(
                text=f"📖 No books found for '{title}'. Suggested price: Rs. 500"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = TextbookMarketplace(root)
    root.mainloop()
