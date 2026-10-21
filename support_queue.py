from collections import deque
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Ticket:
    id: int
    customer: str
    issue: str
    created: datetime


class SupportQueue:
    def __init__(self):
        self._q = deque()
        self._next_id = 1

    def submit(self, customer, issue):
        t = Ticket(self._next_id, customer, issue, datetime.now())
        self._next_id += 1
        self._q.append(t)  # enqueue: O(1)
        return t

    def next_ticket(self):
        return self._q.popleft() if self._q else None  # dequeue: O(1)

    def peek(self):
        return self._q[0] if self._q else None

    def __len__(self):
        return len(self._q)


if __name__ == "__main__":
    desk = SupportQueue()
    desk.submit("Ana", "Cannot log in")
    desk.submit("Ben", "Billing error")
    desk.submit("Cho", "App crashes")

    while len(desk):
        t = desk.next_ticket()
        print(f"Agent handling #{t.id}: {t.customer} - {t.issue}")
