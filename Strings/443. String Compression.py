# Medium
# https://leetcode.com/problems/string-compression/
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        # read and write to mark where we are reading and writing from.
        #  Both operations will be done left to right alternately: 
        # we will read a contiguous group of characters, 
        # then write the compressed version to the array. 
        # At the end, the position of the write head will be the length of the answer that was written.
        read, write = 0, 0
        while read < len(chars):
            count = 1
            while read + 1 < len(chars) and chars[read + 1] == chars[read]:
                count += 1
                read += 1
            chars[write] = chars[read]
            write += 1
            read += 1
            # print(write, read)
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            if write > read:
                read += write - read
        return write
