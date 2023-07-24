class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        s = image[sr][sc]
        self.a(image, sr, sc, color, s)
        return image

    def a(self, image, sr, sc, color, s):
        if sr < 0 or sc < 0 or sc > len(image[0]) - 1 or sr > len(image) - 1 or image[sr][sc] == color or image[sr][sc] != s:
            return
        image[sr][sc] = color
        self.a(image, sr + 1, sc, color, s)
        self.a(image, sr + -1, sc, color, s)
        self.a(image, sr, sc + 1, color, s)
        self.a(image, sr, sc - 1, color, s)