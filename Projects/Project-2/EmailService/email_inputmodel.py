from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class EmailMessageDTO:
    to_emails: List[str]
    template_id: str
    dynamic_data: Dict[str, Any]
    subject: Optional[str] = None
    from_email: Optional[str] = None
    reply_to: Optional[str] = None
