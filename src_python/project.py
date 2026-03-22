# project.py

class Project:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.copyright = ""
        self.comments = []

        self.machine = 0
        self.framerate = 0
        self.expansion = 0
        self.vibrato = 1
        self.split = 32
        self.n163channels = 0

        self.tracks = []
    
    def to_dict(self) -> dict:
        track_dicts = [track.to_dict() for track in self.tracks]

        return {
            "title": self.title,
            "author": self.author,
            "copyright": self.copyright,
            "comments": self.comments,
            "machine": self.machine,
            "framerate": self.framerate,
            "expansion": self.expansion,
            "vibrato": self.vibrato,
            "split": self.split,
            "n163channels": self.n163channels,
            "tracks": track_dicts
        }
