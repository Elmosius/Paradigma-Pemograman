# Load konten dari halaman web setiap jam, memastikan tetap uptodate

from __future__ import annotations
from threading import Timer
import datetime
from urllib.request import urlopen
import pickle
from typing import Any

class URLPolling:
    def __init__(self, url: str) -> None:
        self.url = url
        self.content = ""
        self.last_updated: datetime.datetime
        self.timer: Timer
        self.update()
        
    def update(self) -> None:
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self) -> None:
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()
        
    def __getstate__(self) -> dict[str, Any]:
        pickleable_state = self.__dict__.copy()
        if "timer" in pickleable_state:
            del pickleable_state["timer"]
        return pickleable_state
    
    def __setstate__(self, pickleable_state: dict[str,Any])-> None:
        self.__dict__ = pickleable_state
        self.schedule()
        
def main():
    print("Menserialisasi isi url http:/dusty.philips.codes...")
    poll = URLPolling("http://dusty.phillips.codes")
    pickle_bytes = pickle.dumps(poll)
    del poll
    recovered_poller = pickle.loads(pickle_bytes)
    print(recovered_poller.contents)
    print("Selesai...")
    
if __name__ == "__main__":
    main()