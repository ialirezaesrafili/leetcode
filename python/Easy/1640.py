class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        # Create a mapping of starting elements to their corresponding pieces
        piece_map = {piece[0]: piece for piece in pieces}

        i = 0
        n = len(arr)

        while i < n:
            # Check if the current position matches the start of any piece
            if arr[i] not in piece_map:
                return False

            piece = piece_map[arr[i]]

            # Check if the piece matches the corresponding segment in arr
            if arr[i:i + len(piece)] != piece:
                return False

            # Move index by the length of the matched piece
            i += len(piece)

        return True
