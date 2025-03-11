from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Task:
    uid: str
    type_: str
    started_at: datetime
    done_at: datetime
    lead_time: timedelta

    def is_valuable(self) -> bool:
        return self.type_ in {'STORY', 'TASK'}

    def is_bug(self) -> bool:
        return self.type_ == 'BUG'

    def is_tech(self) -> bool:
        return self.type_ in {'TECH', 'DISCOVERY'}
