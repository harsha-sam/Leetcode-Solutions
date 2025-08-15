class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total_beams = 0
        prev_security_devices = 0
        for i in range(len(bank)):
            security_devices = bank[i].count("1")
            if security_devices > 0:
                total_beams += prev_security_devices * security_devices
                prev_security_devices = security_devices
        return total_beams
