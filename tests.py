from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

        @pytest.fixture(autouse=True)
        def setup(self):
            """Создаем экземпляр BooksCollector перед каждым тестом."""
            self.collector = BooksCollector()


        @pytest.mark.parametrize("book_name", ["", "A" * 41])
        def test_add_new_book_invalid_name(self, book_name):
            """Проверяем, что книга не добавляется, если имя некорректно."""
            self.collector.add_new_book(book_name)
            assert book_name not in self.collector.get_books_genre()

        def test_set_book_genre(self):
            """Проверяем установку жанра для книги."""
            self.collector.add_new_book("1984")
            self.collector.set_book_genre("1984", "Фантастика")
            assert self.collector.get_book_genre("1984") == "Фантастика"

        def test_set_book_genre_invalid(self):
            """Проверяем, что жанр не устанавливается, если жанр некорректен."""
            self.collector.add_new_book("1984")
            self.collector.set_book_genre("1984", "Некорректный жанр")
            assert self.collector.get_book_genre("1984") == ''

        def test_get_books_with_specific_genre(self):
            """Проверяем получение книг с определённым жанром."""
            self.collector.add_new_book("1984")
            self.collector.set_book_genre("1984", "Фантастика")
            assert self.collector.get_books_with_specific_genre("Фантастика") == ["1984"]

        def test_get_books_for_children(self):
            """Проверяем, что книги с возрастным рейтингом отсутствуют в списке книг для детей."""
            self.collector.add_new_book("Сияние")
            self.collector.set_book_genre("Сияние", "Ужасы")
            self.collector.add_new_book("Приключения")
            self.collector.set_book_genre("Приключения", "Комедии")
            assert self.collector.get_books_for_children() == ["Приключения"]

        def test_add_book_in_favorites(self):
            """Проверяем добавление книги в Избранное."""
            self.collector.add_new_book("1984")
            self.collector.add_book_in_favorites("1984")
            assert "1984" in self.collector.get_list_of_favorites_books()

        def test_delete_book_from_favorites(self):
            """Проверяем удаление книги из Избранного."""
            self.collector.add_new_book("1984")
            self.collector.add_book_in_favorites("1984")
            self.collector.delete_book_from_favorites("1984")
            assert "1984" not in self.collector.get_list_of_favorites_books()

        def test_get_list_of_favorites_books(self):
            """Проверяем получение списка Избранных книг."""
            self.collector.add_new_book("1984")
            self.collector.add_book_in_favorites("1984")
            self.collector.add_new_book("Сияние")
            self.collector.add_book_in_favorites("Сияние")
            assert self.collector.get_list_of_favorites_books() == ["1984", "Сияние"]

        def test_get_book_genre(self):
            """Проверяем, что жанр книги возвращается корректно."""
            self.collector.add_new_book("1984")
            self.collector.set_book_genre("1984", "Фантастика")
            assert self.collector.get_book_genre("1984") == "Фантастика"
