# project_reader.py

from helpers import (
    get_quote, 
    get_int_list, 
    get_hex_list,
    get_token_key, 
    is_null_token
)

from project import Project
from track import Track 

class ProjectReader:
    def __init__(self):
        self.current_pattern = 0 

        self.dispatch = {}
        self.init_dispatch()

    def init_dispatch(self):
        for key in ["TITLE", "AUTHOR","COPYRIGHT"]:
            self.dispatch[key] = self._handle_info

        self.dispatch["COMMENT"] = self._handle_comment

        for key in ["MACHINE", "FRAMERATE", "EXPANSION", "VIBRATO", "SPLIT", "N163CHANNELS"]:
            self.dispatch[key] = self._handle_global_settings
            
        self.dispatch["TRACK"] = self._handle_track
        self.dispatch["COLUMNS"] = self._handle_columns
        self.dispatch["ORDER"] = self._handle_order
        self.dispatch["PATTERN"] = self._handle_pattern
        self.dispatch["ROW"] = self._handle_row
    
    def _handle_info(self, project: "Project", line: str) -> None:
        tag = line.split()[0].lower()
        quote = get_quote(line)
        setattr(project, tag, quote)

    def _handle_comment(self, project: "Project", line: str) -> None:
        tag = line.split()[0].lower()
        quote = get_quote(line)
        project.comments.append(quote)
    
    def _handle_global_settings(self, project: "Project", line: str) -> None:
        tag = line.split()[0].lower()
        value = int(line.split()[-1])
        setattr(project, tag, value)

    def _handle_track(self, project: "Project", line: str) -> None:
        pattern, speed, tempo = list(map( int, line.split()[1:4]))

        quote = get_quote(line)

        track = Track(pattern, speed, tempo, quote)
        project.tracks.append(track)

    def _handle_columns(self, project: "Project", line: str) -> None:
        if not project.tracks:
            return 
        track = project.tracks[-1] 

        eff_cols = get_int_list(line)
        track.eff_cols = eff_cols
        track.num_cols = len(eff_cols)

    def _handle_order(self, project: "Project", line: str) -> None:
        if not project.tracks:
            return 
        track = project.tracks[-1] 
        
        frame = int(line.split()[1], 16)
        lst = get_hex_list(line)
        track.orders[frame] = lst 

    def _handle_pattern(self, project: "Project", line: str) -> None:
        if not project.tracks:
            return 
        track = project.tracks[-1] 
        
        pattern = int(line.split()[1], 16)
        self.current_pattern = pattern 

    def _handle_row(self, project: "Project", line: str) -> None:
        if not project.tracks: return 
        track = project.tracks[-1] 
        row = int(line.split()[1], 16)
        tokens = [token.strip() for token in line.split(":")[1:]]
        for col, token in enumerate(tokens):
            if is_null_token(token): continue
            token_key = get_token_key(self.current_pattern, row, col)
            track.tokens[token_key] = token

    def _process_line(self, project, line):
        tag = line.split()[0].upper()
        func = self.dispatch.get(tag)
        if not func:
            return

        try:
            func(project, line)
        except Exception as e:
            print("[ERROR] LINE: {}".format(line))

    def read(self, project, input_file):
        with open(input_file, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line[0] == '#':
                    continue
                self._process_line(project, line)

