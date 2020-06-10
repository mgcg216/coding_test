nrfjprog --family NRF52 --halt
nrfjprog --family NRF52 --eraseall
nrfjprog --family NRF52 --program s140_nrf52_6.1.0_softdevice.hex 
nrfjprog.exe --reset --program nrf52840_bledongle_bootloader_S140.hex --family NRF52 
nrfjprog --pinreset
FwUpdateApp.exe COM41 DONGLEPK NGP_pub_key.txt
