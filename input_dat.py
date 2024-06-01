class DAT:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def count_lines(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            for count, _ in enumerate(file):
                pass
            return count
        
    def read_headers(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                first_line = file.readline().strip()
                headers = first_line.split('\x14')  # Splitting by ASCII 20 (File Separator)
                return headers
        except Exception as e:
            print(f"Failed to read headers from {self.filepath}: {e}")
            return []