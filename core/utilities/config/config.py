import json

from .vars import *

class Config():
        term: Terminal
        graph: GraphConfig
        conntable: ConnTable
        os: OSConfig
        hdw: HardwareConfig
        conn: SysConnection

        def __init__(self) -> None:
                """
                To Avoid Errors and try/except. Check if file exists and validate JSON syntax
                """
                self.config = json.loads(open("assets/config.json").read())
                self.parseTerminal()

        def parseTerminal(self) -> term:
                """
                Validate the Terminal structure in JSON!
                """
                self.term.size = self.config['Terminal']['size']
                self.term.title = self.config['Terminal']['title']
                self.term.description = self.config['Terminal']['description']
                self.term.version = self.config['Terminal']['version']
                self.term.motd = self.config['Terminal']['motd']

        def parseGraph(self) -> graph:
                self.graph.display = self.config['Graph']['display']
                self.graph.data_c = self.config['Graph']['data_c']
                self.graph.attacked_data_c = self.config['Graph']['attacked_data_c']
                self.graph.border_c = self.config['Graph']['border_c']

        def parseConnTable(self) -> conntable:
                self.conntable.display = self.config['Conn_Table']['display']
                self.conntable.text_c = self.config['Conn_Table']['text_c']
                self.conntable.border_c = self.config['Conn_Table']['border_c']
                self.conntable.header_text_c = self.config['Conn_Table']['header_text_c']

        def retrieveHardware(self) -> hdw:
                pass
