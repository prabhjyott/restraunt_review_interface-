import tkinter as tk
from tkinter import messagebox

class RestaurantReviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Review")
        self.root.geometry("700x600")
        self.root.config(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self.root, text="Restaurant Review", font=("Arial", 32, "bold"), bg="#f0f0f0", fg="#333333")
        self.title_label.pack(pady=20)

        # Frame for Inputs
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=20)

        # Restaurant Name
        self.restaurant_label = tk.Label(input_frame, text="Restaurant Name:", font=("Arial", 18), bg="#f0f0f0", fg="#333333")
        self.restaurant_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.restaurant_entry = tk.Entry(input_frame, font=("Arial", 18), width=40, bd=2, relief=tk.GROOVE)
        self.restaurant_entry.grid(row=0, column=1, padx=10, pady=10)

        # Review
        self.review_label = tk.Label(input_frame, text="Review:", font=("Arial", 18), bg="#f0f0f0", fg="#333333")
        self.review_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.review_text = tk.Text(input_frame, font=("Arial", 18), width=50, height=8, bd=2, relief=tk.GROOVE)
        self.review_text.grid(row=1, column=1, padx=10, pady=10)

        # Rating
        self.rating_label = tk.Label(input_frame, text="Rating (1-5):", font=("Arial", 18), bg="#f0f0f0", fg="#333333")
        self.rating_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.rating_entry = tk.Entry(input_frame, font=("Arial", 18), width=10, bd=2, relief=tk.GROOVE)
        self.rating_entry.grid(row=2, column=1, padx=10, pady=10)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit Review", font=("Arial", 18, "bold"), command=self.submit_review, bg="#007BFF", fg="white", bd=2, relief=tk.GROOVE, activebackground="#0056b3")
        self.submit_button.pack(pady=10)

        # Display Reviews Button
        self.display_button = tk.Button(self.root, text="Display Reviews", font=("Arial", 18, "bold"), command=self.display_reviews, bg="#28A745", fg="white", bd=2, relief=tk.GROOVE, activebackground="#218838")
        self.display_button.pack(pady=10)

    def submit_review(self):
        restaurant = self.restaurant_entry.get()
        review = self.review_text.get("1.0", tk.END).strip()
        rating = self.rating_entry.get()

        if not restaurant or not review or not rating:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Rating must be an integer between 1 and 5.")
            return

        with open("reviews.txt", "a") as file:
            file.write(f"Restaurant: {restaurant}\nReview: {review}\nRating: {rating}\n\n")
        messagebox.showinfo("Success", "Review submitted successfully!")

        self.restaurant_entry.delete(0, tk.END)
        self.review_text.delete("1.0", tk.END)
        self.rating_entry.delete(0, tk.END)

    def display_reviews(self):
        try:
            with open("reviews.txt", "r") as file:
                reviews = file.read()
        except FileNotFoundError:
            messagebox.showinfo("No Reviews", "No reviews found.")
            return

        review_window = tk.Toplevel(self.root)
        review_window.title("Reviews")
        review_window.geometry("700x500")
        review_window.config(bg="#f0f0f0")

        review_label = tk.Label(review_window, text="Reviews", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333333")
        review_label.pack(pady=10)

        review_text = tk.Text(review_window, font=("Arial", 16), width=80, height=15, bd=2, relief=tk.GROOVE)
        review_text.pack(padx=10, pady=10)
        review_text.insert(tk.END, reviews)
        review_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantReviewApp(root)
    root.mainloop()