import os, json

from .vars import *

class Config():
        json_file_path = "assets/config.json"
        def __init__(self) -> None:
                if os.path.isfile(self.json_file_path) == False: return
                self.config = json.loads(open("assets/config.json").read())

                """
                        - Validate All Structures and fields (Return error if config is not structured correctly)
                        - Create a 'backup' system for config file along with the UI
                        - Create a function to restore the config file with empty values

                """
                self.term = self.parseTerminal()
                self.graph = self.parseGraph()
                self.conntable = self.parseConnTable()
                self.os =  self.parseOS()
                self.hdw = self.parseHardware()
                self.conn = self.parseConnection()

        def parseTerminal(self) -> Terminal:
                term = Terminal()
                term.size = self.config['Terminal']['size']
                term.title = self.config['Terminal']['title']
                term.description = self.config['Terminal']['description']
                term.version = self.config['Terminal']['version']
                term.motd = self.config['Terminal']['motd']

        def parseGraph(self) -> GraphConfig:
                graph = GraphConfig()
                graph.display = self.config['Graph']['display']
                graph.data_c = self.config['Graph']['data_c']
                graph.attacked_data_c = self.config['Graph']['attacked_data_c']
                graph.border_c = self.config['Graph']['border_c']

        def parseConnTable(self) -> ConnTable:
                conntable = ConnTable()
                conntable.display = self.config['Conn_Table']['display']
                conntable.text_c = self.config['Conn_Table']['text_c']
                conntable.border_c = self.config['Conn_Table']['border_c']
                conntable.header_text_c = self.config['Conn_Table']['header_text_c']

        def parseOS(self) -> OSConfig:
                os = OSConfig()
                os.display = self.config['OS_Display']['display']
                os.labels_c = self.config['OS_Display']['labels_c']
                os.value_c = self.config['OS_Display']['value_c']
                os.os_name_p = self.config['OS_Display']['os_name_p']
                os.os_kernel_p = self.config['OS_Display']['os_kernel_p']
                os.os_version_p = self.config['OS_Display']['os_version_p']
                os.shell_p = self.config['OS_Display']['shell_p']

        def parseHardware(self) -> HardwareConfig:
                hdw = HardwareConfig()
                hdw.display = self.config['Hardware']['display']
                hdw.labels_c = self.config['Hardware']['labels_c']
                hdw.value_c = self.config['Hardware']['value_c']
                hdw.cpu_count_p = self.config['Hardware']['cpu_count_p']
                hdw.cpu_name_p = self.config['Hardware']['cpu_name_p']
                hdw.cpu_cores_p = self.config['Hardware']['cpu_cores_p']
                hdw.cpu_usage_p = self.config['Hardware']['cpu_usage_p']
                hdw.gpu_name_p = self.config['Hardware']['gpu_name_p']
                hdw.gpu_cores_p = self.config['Hardware']['gpu_cores_p']
                hdw.gpu_usage_p = self.config['Hardware']['gpu_usage_p']
                hdw.memory_name_p = self.config['Hardware']['memory_name_p']
                hdw.memory_capacity_p = self.config['Hardware']['memory_capacity_p']
                hdw.memory_usage_p = self.config['Hardware']['memory_usage_p']
                hdw.memory_used_p = self.config['Hardware']['memory_used_p']
                hdw.memory_free_p = self.config['Hardware']['memory_free_p']
                hdw.hdd_name_p = self.config['Hardware']['hdd_name_p']
                hdw.hdd_capacity_p = self.config['Hardware']['hdd_capacity_p']
                hdw.hdd_used_p = self.config['Hardware']['hdd_used_p']
                hdw.hdd_free_p = self.config['Hardware']['hdd_free_p']
                hdw.hdd_usage_p = self.config['Hardware']['hdd_usage_p']
        
        def parseConnection(self) -> ConnectionConfig:
                conn = ConnectionConfig()
                conn.display = self.config['Connection']['display']
                conn.labels_c = self.config['Connection']['labels_c']
                conn.value_c = self.config['Connection']['value_c']
                conn.ip = self.config['Connection']['ip']
                conn.port = self.config['Connection']['port']
                conn.key = self.config['Connection']['key']
                conn.timeout = self.config['Connection']['timeout']
                conn.diaply = self.config['PPS']['display']
                conn.pps_p = self.config['PPS']['pps_p']
                conn.pps_label_c = self.config['PPS']['pps_label_c']
                conn.pps_value_c = self.config['PPS']['pps_value_c']