import math

# ============================================================
# Daily Challenge: Pagination
# Instructions:
# Create a Pagination class that simulates a basic pagination system.
#
# Step 1: Create the Pagination class.
# Step 2: Implement __init__ with optional items and page_size.
#         - items defaults to None (empty list)
#         - page_size defaults to 10
#         - current_idx starts at 0
#         - calculate total number of pages using math.ceil
# Step 3: Implement get_visible_items() that returns items
#         on the current page using slicing.
# Step 4: Implement navigation methods:
#         - go_to_page(page_num): go to a specific page (1-indexed)
#           raises ValueError if out of bounds
#         - first_page(): go to the first page
#         - last_page(): go to the last page
#         - next_page(): go to the next page if not already last
#         - previous_page(): go back one page if not already first
#         All methods except go_to_page return self for chaining.
# Step 5 (Bonus): Add __str__() to display current page items
#                 each on a new line.
# ============================================================

class Pagination:
    def __init__(self, items=None, page_size=10):
        """
        Initialize the Pagination object.
        Parameters:
            items (list): list of items to paginate (default: None)
            page_size (int): number of items per page (default: 10)
        """
        if items is None:
            self.items = []
        else:
            self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        """Return the list of items visible on the current page."""
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        """
        Go to a specific page (1-indexed).
        Parameters: page_num (int): page number to navigate to
        Raises: ValueError if page_num is out of bounds
        """
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page {page_num} is out of bounds. Valid range: 1 to {self.total_pages}")
        self.current_idx = page_num - 1
        return self

    def first_page(self):
        """Go to the first page."""
        self.current_idx = 0
        return self

    def last_page(self):
        """Go to the last page."""
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        """Go to the next page if not already on the last page."""
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        """Go back one page if not already on the first page."""
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        """Return current page items each on a new line."""
        return "\n".join(str(item) for item in self.get_visible_items())


# ============================================================
# Tests
# ============================================================

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

# Bonus: method chaining
p.first_page()
print(p.next_page().next_page().next_page().get_visible_items())
# ['m', 'n', 'o', 'p']

# Bonus: __str__
p.first_page()
print(str(p))
# a
# b
# c
# d

# ValueError test
try:
    p.go_to_page(10)
except ValueError as e:
    print(e)

try:
    p.go_to_page(0)
except ValueError as e:
    print(e)