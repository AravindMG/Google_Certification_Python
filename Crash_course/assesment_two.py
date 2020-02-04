def size_partition():
    disk_size = 16 * 1024 * 1024 * 1024
    sector_size = 512
    sector_amount =  disk_size * sector_size
    print(sector_amount)


if __name__ == "__main__":
    size_partition()