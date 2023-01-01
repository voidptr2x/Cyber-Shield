import json

from .vars import *

class Config():

        def __init__(self) -> None:
                """
                To Avoid Errors and try/except. Check if file exists and validate JSON syntax
                """
                self.term = Terminal()
                self.graph = GraphConfig()
                self.conntable = ConnTable()
                self.os = OSConfig()
                self.hdw = HardwareConfig()
                self.conn = SysConnection()
                self.config = json.loads(open("assets/config.json").read())
                self.parseTerminal()

        def parseTerminal(self) -> Terminal:
                """
                Validate the Terminal structure in JSON!
                """
                self.term.size = self.config['Terminal']['size']
                self.term.title = self.config['Terminal']['title']
                self.term.description = self.config['Terminal']['description']
                self.term.version = self.config['Terminal']['version']
                self.term.motd = self.config['Terminal']['motd']

        def parseGraph(self) -> GraphConfig:
                self.graph.display = self.config['Graph']['display']
                self.graph.data_c = self.config['Graph']['data_c']
                self.graph.attacked_data_c = self.config['Graph']['attacked_data_c']
                self.graph.border_c = self.config['Graph']['border_c']

        def parseConnTable(self) -> ConnTable:
                self.conntable.display = self.config['Conn_Table']['display']
                self.conntable.text_c = self.config['Conn_Table']['text_c']
                self.conntable.border_c = self.config['Conn_Table']['border_c']
                self.conntable.header_text_c = self.config['Conn_Table']['header_text_c']

        def retrieveOS(self) -> OSConfig:
                self.os.labels_c = self.config['OS_Display']['labels_c']
                self.os.value_c = self.config['OS_Display']['value_c']
                self.os.os_name_p = self.config['OS_Display']['os_name_p']
                self.os.os_kernel_p = self.config['OS_Display']['os_kernel_p']
                self.os.os_version_p = self.config['OS_Display']['os_version_p']
                self.os.shell_p = self.config['OS_Display']['shell_p']

        def retrieveHardware(self) -> HardwareConfig:
                self.hdw.labels_c = self.config['Hardware']['labels_c']
                self.hdw.value_c = self.config['Hardware']['value_c']
                self.hdw.cpu_count_p = self.config['Hardware']['cpu_count_p']
                self.hdw.cpu_name_p = self.config['Hardware']['cpu_name_p']
                self.hdw.cpu_cores_p = self.config['Hardware']['cpu_cores_p']
                self.hdw.cpu_usage_p = self.config['Hardware']['cpu_usage_p']
                self.hdw.gpu_name_p = self.config['Hardware']['gpu_name_p']
                self.hdw.gpu_cores_p = self.config['Hardware']['gpu_cores_p']
                self.hdw.gpu_usage_p = self.config['Hardware']['gpu_usage_p']
                self.hdw.memory_name_p = self.config['Hardware']['memory_name_p']
                self.hdw.memory_capacity_p = self.config['Hardware']['memory_capacity_p']
                self.hdw.memory_usage_p = self.config['Hardware']['memory_usage_p']
                self.hdw.memory_used_p = self.config['Hardware']['memory_used_p']
                self.hdw.memory_free_p = self.config['Hardware']['memory_free_p']
                self.hdw.hdd_name_p = self.config['Hardware']['hdd_name_p']
                self.hdw.hdd_capacity_p = self.config['Hardware']['hdd_capacity_p']
                self.hdw.hdd_used_p = self.config['Hardware']['hdd_used_p']
                self.hdw.hdd_free_p = self.config['Hardware']['hdd_free_p']
                self.hdw.hdd_usage_p = self.config['Hardware']['hdd_usage_p']
        
        def retrieveConnection(self) -> SysConnection:
                self.conn.labels_c = self.config['Connection']['labels_c']
                self.conn.value_c = self.config['Connection']['value_c']
                self.conn.ip = self.config['Connection']['ip']
                self.conn.port = self.config['Connection']['port']
                self.conn.key = self.config['Connection']['key']
                self.conn.timeout = self.config['Connection']['timeout']