"""
Using a list for Row & Column Positioning and RGB Colors!

Any var ending with _c can be multiple color code types. RGB, HEX, or Builtin-Variable Color Code ('{RED}')
"""
class Terminal:
    size: list # Rows: size[0], column[1]
    title: str
    description: str
    version: str
    motd: str

class GraphConfig:
    display: bool
    graph_layout_p: list
    graph_p: list
    data_c: str
    attacked_data_c: str
    border_c: str

class ConnTableConfig:
    display: bool
    border_c: str
    text_c: str
    header_text_c: str

class OSConfig:
    display: bool
    labels_c: str
    value_c: str

    os_name_p: str
    os_kernel_p: str
    os_version_p: str
    shell_p: str

class HardwareConfig:
    display: bool
    labels_c: str
    value_c: str

    cpu_count_p: str
    cpu_name_p: str
    cpu_cores_p: str
    cpu_usage_p: str
    gpu_name_p: str
    gpu_cores_p: str
    gpu_usage: str

    memory_type_p: str
    memory_capacity_p: str
    memory_usage_p: str
    memory_used_p: str
    memory_free_p: str

    hdd_name_p: str
    hdd_capacity_p: str
    hdd_used_p: str
    hdd_free_p: str
    hdd_usage_p: str

class ConnectionConfig:
    display: bool
    labels_c: str
    value_c: str

    ip: str
    port: str
    key: str
    timeout: str
    wifi_adapter_p: str
    ms_p: str
    download_speed_p: str
    upload_speed_p: str
    nload_stats_p: str