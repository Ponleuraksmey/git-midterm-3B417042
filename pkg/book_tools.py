import json
from typing import List, Dict, Any


# read_books function
def read_books(file_name: str) -> List[Dict[str, Any]]:
    """
    Reads a JSON file containing book information and returns a list of dictionaries

    Parameters:
        file_name (str): The name of the JSON file to read.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, each representing a book.
    """
    try:
        with open(file_name, "r", encoding="utf-8")as file:
            books = json.load(file)
            return books
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 '{file_name}'。")

    except json.JSONDecodeError:
        print(f"錯誤：'{file_name}' 的 JSON 格式不正確。")

    except OSError as e:
        print(f"檔案讀取發生錯誤：{e}")


# write_books function
def write_books(books: List[Dict[str, Any]], file_name: str) -> None:
    """
    Writes a list of book dictionaries to a JSON file.

    Parameters:
        books (List[Dict[str, Any]]): A list of dictionaries, each representing a book.
        file_name (str): The name of the JSON file to write to.

    """
    try:
        with open(file_name, "w", encoding="utf-8")as file:
            json.dump(books, file, ensure_ascii=False, indent=4)
    except OSError as e:
        print(f"檔案寫入發生錯誤：{e}")

        
def show_books(books: List[Dict[str, Any]]) -> None:
    """
    Displays the list of books in a readable format.

    Parameters:
        books (List[Dict[str, Any]]): A list of dictionaries, each represent a book.
    """

    if not books:
        print("目前沒有書籍資料")
        return

    print(f"{'編號':<4}  {'書籍編號':<8}  {'書名':<16}  {'作者':<10}  {'價格':>8}  {'狀態'}")
    for index, book in enumerate(books, start=1):
        status = "已借出" if book["borrowed"] else "可借閱"
        print(
            f"{index:>4}  {book['id']:<8}  {book['title']:<16}  "
            f"{book['author']:<10}  {book['price']:>8,}  {status}"
        )


def search_books(
        books: List[Dict[str, Any]], keyword: str
) -> List[Dict[str, Any]]:
    """
    Searches for books that match the given keyword in their title or author.

    Parameters:
        books (List[Dict[str, Any]]): A list of dictionaries, each represent a book.
        keyword (str): The keyword to search for.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries representing the matching books
    """

    keyword_lower = keyword.strip().lower()
    result = [
        book for book in books if keyword_lower in book["title"].lower()
        ]
    return result


def show_last_three_and_stats(books: List[Dict[str, Any]]) -> None:
    """
    Displays the last three books added to the list and some statistics about the books.

    Parameters:
        books (List[Dict[str, Any]]): A list of dictionaries, each represent a book.
    """

    if not books:
        print("目前沒有書籍資料")
        return

    print("--- 最後 3 筆書籍 ---")
    last_three_books = books[-3:]
    show_books(last_three_books)

    total_count = len(books) 
    borrowed_count = sum(1 for book in books if book["borrowed"])
    available_count = total_count - borrowed_count
    total_price = sum(book["price"] for book in books)
    average_books_price = total_price / total_count if total_count > 0 else 0.0

    print("\n--- 書籍統計 ---")
    print(f"書籍總數：{total_count}")
    print(f"可借閱：{available_count}")
    print(f"已借出：{borrowed_count}")
    print(f"價格合計：{total_price:,} 元")
    print(f"平均價格：{average_books_price:.2f} 元")
