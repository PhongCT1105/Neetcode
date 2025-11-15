class Logger:

    """
    Logger system design that check if the message should be printed
    Algorithm:
        - Hash/dictionary: New log message come in at different timeframe.
            Strength: Quickly access the message in O(1) instead of O(N)
    """

    def __init__(self):
        """
        Atributes:
            - Hash map/Dict: 
                Key: message (str); Value: next possible timestamp (int)
        """
        self.log_db = {}
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Return True if message should be print at timestamp
        - if timestamp > current message timestamp -> True; else -> False
        """   
        if message not in self.log_db:
            self.log_db[message] = timestamp + 10
            return True

        if timestamp >= self.log_db[message]:
            self.log_db[message] = timestamp + 10
            return True
        
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
