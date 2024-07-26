# How to Restore Deleted EFI System Partition in Windows

```bash
diskpart
list disk

select disk 0
list part
```

```
DISKPART> list part

  分区 ###       类型              大小     偏移量
  -------------  ----------------  -------  -------
  分区      1    系统                 100 MB  1024 KB
  分区      2    已保留                 16 MB   101 MB
  分区      3    主要                  99 GB   117 MB
  分区      4    恢复                 830 MB    99 GB
  分区      5    主要                 376 GB   100 GB
```

```bash
# Select the reserved partition to remove
select part 1
delete partition override
```

```batch
# manually create the EFI and MSR partitions to place the Windows bootloader files
select disk 0
create partition efi size=100

# Format EFI partition with FAT32
list partition
select partition 1
format quick fs=fat32 label="System"
assign letter=G

# create a 16MB MSR partition
create partition msr size=16
list partition
list vol
```

```bash
# Assign the drive letter to main Windows partition
select vol 1
assign letter=C
exit
```

```bash
# copy the UEFI boot environment files from the Windows system directory to the EFI boot partition and recreate the BCD bootloader configuration
bcdboot c:\windows /s G: /f UEFI
```

## Ref.

* [How to Restore Deleted EFI System Partition in Windows](https://woshub.com/how-to-repair-deleted-efi-partition-in-windows-7/)