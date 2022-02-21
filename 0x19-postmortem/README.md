# 0x19. Post mortem

On September 29, 2021 the system failure occurred. For 24 hours I was unable to access my Linux distribution. The root cause of the outage was running the python3 command.

## Timeline
- 9:00 - user noticed that the Linux system does not work , does not start .
- 17:00 - after looking for ways to solve the problem without having to reinstall the distribution, the user tried to reinstall Ubuntu.
- 20:00 - the user decides to reboot the computer in the hope that the reboot will allow him to find the recovery operating system.
- 21:00 - After searching the BIOS and UEFI, the user determines that the distribution is unrecoverable and boots the computer into Windows 10.
- 22:00 - investigates further to see if there is a way to fix the problem from the command line and decides that the easiest course of action is to update the operating system on a USB and reinstall the operating system.
- 23:00 - the operating system is reinstalled from the USB and all functionality is restored to the configuration with Windows 11.

## Root Cause
The user executed too many sudo commands.

## Resolution
User had to reinstall the operating system from USB and upgrade.

## Corrective/Preventive Action
The user will now investigate further what will happen before running any commands on their machine.
