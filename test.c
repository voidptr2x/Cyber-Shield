#include <stdio.h>
#include <sys/ioctl.h>
#include <linux/hdreg.h>

int main(void) {
    int fd;
    struct hd_driveid info;

    fd = open("/dev/sda", O_RDONLY);
    ioctl(fd, HDIO_GET_IDENTITY, &info);

    printf("Model: %s\n", info.model);
    printf("Serial Number: %s\n", info.serial_no);
    printf("Firmware Revision: %s\n", info.fw_rev);
    printf("Capacity: %llu\n", (unsigned long long)info.lba_capacity);

    close(fd);
    return 0;
}
