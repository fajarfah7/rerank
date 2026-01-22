from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class ResponseError:
    code: str
    message: str
    
    def asdict(self) -> dict:
        return asdict(self)