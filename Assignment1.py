from queue import Queue
import uuid


class Application:
    id_ = str(uuid.uuid4())

    def __init__(self, data: str):
        self.data = data


def generate_request(application_queue_: Queue, data: str) -> None:
    # Створити нову заявку
    # Додати заявку до черги
    application_data = Application(data)
    application_queue_.put(application_data)
    print(f"Data processing was queued for application {application_data.id_}")


def process_request(application_queue_: Queue):
    if application_queue_.empty():
        print("Queue is empty")
        return

    application_data = application_queue.get()
    print(f"Processed application {application_data.id_}")


if __name__ == "__main__":
    application_queue = Queue()

    while True:
        generate_request(
            application_queue,
            "New application data"
        )
        process_request(application_queue)
