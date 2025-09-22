from injector import Module, Binder, provider, singleton
import sqlite3

from environment import Environment
from sms.sms_sender import SmsSender
from sales_man import SalesMan
from phone_book.i_phone_book import IPhoneBook
from phone_book.phone_book import PhoneBook
from phone_book.phone_book_fake import PhoneBookFake
from phone_book.phone_number_validator import PhoneNumberValidator
from database.i_phone_book_repository import IPhoneBookRepository
from database.phone_book_file_repository import PhoneBookFileRepository
from database.phone_book_sqlite_repository import PhoneBookSqliteRepository


class AppModule(Module):
    def __init__(self, environment: Environment):
        self.environment = environment

    def configure(self, binder: Binder) -> None:    
        if self.environment == Environment.DEVELOPMENT:
            binder.bind(IPhoneBook, to=self.provide_phone_book_dev)

        elif self.environment == Environment.STAGING:
            binder.bind(IPhoneBookRepository, to=self.provide_file_repo)
            binder.bind(IPhoneBook, to=self.provide_phone_book_real)

        elif self.environment == Environment.PRODUCTION:
            binder.bind(sqlite3.Connection, to=self.provide_sqlite_connection)
            binder.bind(IPhoneBookRepository, to=self.provide_sqlite_repo)
            binder.bind(IPhoneBook, to=self.provide_phone_book_real)
        else:
            raise ValueError(f"Unknown environment: {self.environment}")

        binder.bind(SalesMan, to=self.provide_salesman)

    @provider
    @singleton
    def provide_phone_book_dev(
        self,
        validator: PhoneNumberValidator,
    ) -> IPhoneBook:
        return PhoneBookFake(validator)

    @provider
    @singleton
    def provide_phone_book_real(
        self,
        repo: IPhoneBookRepository,
        validator: PhoneNumberValidator,
    ) -> IPhoneBook:
        return PhoneBook(repo, validator)

    @provider
    @singleton
    def provide_file_repo(self) -> PhoneBookFileRepository:
        return PhoneBookFileRepository("phone_book.json")

    @provider
    @singleton
    def provide_sqlite_connection(self) -> sqlite3.Connection:
        return sqlite3.connect("phone_book.db")

    @provider
    @singleton
    def provide_sqlite_repo(
        self,
        conn: sqlite3.Connection,
    ) -> PhoneBookSqliteRepository:
        return PhoneBookSqliteRepository(conn)

    @provider
    def provide_salesman(
        self,
        sms_sender: SmsSender,
        phone_book: IPhoneBook,
    ) -> SalesMan:
        return SalesMan(sms_sender, phone_book)
