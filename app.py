from pkg import book_tools


def main():

    books = book_tools.read_books("books.json")

    while True:
        print("\n--- 簡易書籍管理系統 ---")
        print("1. 顯示全部書籍")
        print("2. 新增書籍")
        print("3. 查詢書籍")
        print("4. 變更借閱狀態")
        print("5. 顯示最後 3 筆書籍與統計")
        print("6. 匯出書籍資料")
        print("7. 離開系統")
        print("-" * 24)

        choice = input("請選擇功能：").strip()

        match choice:
            case "1":
                # 顯示全部書籍
                print("\n--- 顯示全部書籍 ---")
                book_tools.show_books(books)

            case "2":
                # 新增書籍
                while True:
                    book_id = input("請輸入書籍編號：").strip()
                    if not book_id:
                        print("書籍編號不能為空，請重新輸入。")
                        continue
                    if any(book["id"] == book_id for book in books):
                        print("書籍編號已存在，請重新輸入。")
                        continue
                    break

                while True:
                    title = input("請輸入書名：").strip()
                    if not title:
                        print("書名不能為空，請重新輸入。")
                        continue
                    break

                while True:
                    author = input("請輸入作者：").strip()
                    if not author:
                        print("作者不能為空，請重新輸入。")
                        continue
                    break

                while True:
                    price_input = input("請輸入價格：").strip()
                    try:
                        price = int(price_input)
                        if price <= 0:
                            print("價格須為大於 0 的整數，請重新輸入。")
                            continue
                        break
                    except ValueError:
                        print("價格須為大於 0 的整數，請重新輸入。")

                new_book = {
                    "id": book_id,
                    "title": title,
                    "author": author,
                    "price": price,
                    "borrowed": False
                }
                books.append(new_book)
                print("新增成功！")
            case "3":
                # 查詢書籍
                while True:
                    keyword = input("請輸入書名關鍵字：").strip()
                    if not keyword:
                        print("關鍵字不能為空，請重新輸入。")
                        continue
                    break
                result = book_tools.search_books(books, keyword)
                print("\n--- 查詢結果 ---")
                if result:
                    book_tools.show_books(result)
                else:
                    print("查無符合的書籍")

            case "4":
                # 變更借閱狀態
                book_id = input("請輸入書籍編號：").strip()
                found = False
                for book in books:
                    if book["id"] == book_id:
                        found = True
                        book["borrowed"] = not book["borrowed"]
                        status = "已借出" if book["borrowed"] else "可借閱"
                        print(f"「{book['title']}」的狀態已變更為：{status}")
                        break
                if not found:
                    print("查無此書籍編號")

            case "5":
                # 顯示最後 3 筆書籍與統計
                book_tools.show_last_three_and_stats(books)

            case "6":
                # 匯出書籍資料
                try:
                    book_tools.write_books(books, "output.json")
                    print(f"已匯出 {len(books)} 筆書籍資料至 output.json。")
                except OSError as e:
                    print(f"檔案寫入發生錯誤：{e}")

            case "7":
                # 離開系統
                print("系統已退出。")
                break

            case _:
                print("輸入錯誤，請輸入 1～7 的選項。")


# 程式啟動的開關
if __name__ == "__main__":
    main()
