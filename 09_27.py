import csv

class Content:
    def __init__(self, title, menu_name, author_nickname, annotation):
        self.title = title
        self.menu_name = menu_name
        self.author_nickname = author_nickname
        self.annotation = annotation

    def __repr__(self):
        return f"Content(title='{self.title}', menu_name='{self.menu_name}', author_nickname='{self.author_nickname}', annotation='{self.annotation}')"


class User:
    def __init__(self, nickname):
        self.nickname = nickname
        self.contents = []

    def add_content(self, content):
        self.contents.append(content)

    def get_content_count(self):
        return len(self.contents)

    def __repr__(self):
        return f"User(nickname='{self.nickname}', content_count={self.get_content_count()})"


class ContentManager:
    def __init__(self):
        self.users = {}
        self.contents = []

    def add_user(self, nickname):
        self.users[nickname] = User(nickname)

    def add_content(self, nickname, title, menu_name, annotation):
        author_nickname = nickname
        content = Content(title, menu_name, author_nickname, annotation)
        self.contents.append(content)
        if nickname in self.users:
            self.users[nickname].add_content(content)
        else:
            user = User(nickname)
            user.add_content(content)
            self.users[nickname] = user

    def delete_content(self, title):
        for content in self.contents:
            if content.title == title:
                self.contents.remove(content)
                if content.author_nickname in self.users:
                    self.users[content.author_nickname].contents.remove(content)
                print(f"Content '{title}' deleted.")
                return
        print(f"Content '{title}' not found.")

    def modify_content(self, old_title, new_title, menu_name, annotation):
        for content in self.contents:
            if content.title == old_title:
                content.title = new_title
                content.menu_name = menu_name
                content.annotation = annotation
                print(f"Content '{old_title}' modified.")
                return
        print(f"Content '{old_title}' not found.")

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Menu Name', 'Author Nickname', 'Annotation'])
            for content in self.contents:
                writer.writerow([content.title, content.menu_name, content.author_nickname, content.annotation])
        print("Data saved to", filename)

    def load_from_csv(self, filename):
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add_content(row['Author Nickname'], row['Title'], row['Menu Name'], row['Annotation'])
        print("Data loaded from", filename)

    def list_contents(self):
        for content in self.contents:
            print(content)

    def list_users(self):
        for user in self.users.values():
            print(user)


def main():
    manager = ContentManager()

    while True:
        print("\n1. Добавить пользователя")
        print("2. Добавить контент")
        print("3. Удалить контент")
        print("4. Изменить контент")
        print("5. Сохранить в файл CSV")
        print("6. Загрузить из файла CSV")
        print("7. Показать контент")
        print("8. Показать пользователей")
        print("9. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            nickname = input("Введите ник пользователя: ")
            manager.add_user(nickname)

        elif choice == '2':
            nickname = input("Введите ник автора: ")
            title = input("Введите название контента: ")
            menu_name = input("Введите название меню: ")
            annotation = input("Введите аннотацию: ")
            manager.add_content(nickname, title, menu_name, annotation)

        elif choice == '3':
            title = input("Введите название контента для удаления: ")
            manager.delete_content(title)

        elif choice == '4':
            old_title = input("Введите старое название контента: ")
            new_title = input("Введите новое название контента: ")
            menu_name = input("Введите новое название меню: ")
            annotation = input("Введите новую аннотацию: ")
            manager.modify_content(old_title, new_title, menu_name, annotation)

        elif choice == '5':
            filename = input("Введите имя файла для сохранения (с расширением .csv): ")
            manager.save_to_csv(filename)

        elif choice == '6':
            filename = input("Введите имя файла для загрузки (с расширением .csv): ")
            manager.load_from_csv(filename)

        elif choice == '7':
            print("Список контента:")
            manager.list_contents()

        elif choice == '8':
            print("Список пользователей:")
            manager.list_users()

        elif choice == '9':
            break

        else:
            print("Неверный выбор! Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()
