class Webpage:

    def __init__(self, url: str, left=None, right=None):
        self.url = url
        self.left = left
        self.right = right

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Webpage(url=homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        node = Webpage(url=url, left=self.curr)
        self.curr.right = node

        # Update the current node 
        self.curr = self.curr.right

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.left:
            self.curr = self.curr.left
            steps -= 1

        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.right:
            self.curr = self.curr.right
            steps -= 1
        
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
