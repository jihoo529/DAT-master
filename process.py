class Process:
    def __init__(self, type, input_path, headers, checked_headers, output_path, doc_IDs, row_from, row_to):
        self.type = type
        self.input_path = input_path
        self.headers = headers
        self.checked_headers = sorted(checked_headers, key=lambda x: headers.index(x))
        self.output_path = None
        self.header_idx = [headers.index(item) for item in checked_headers if item in headers]
        self.output_dat = []
        self.output_path = output_path
        if doc_IDs: self.doc_IDs = [f'þ{val}þ' for val in doc_IDs]
        else: self.doc_IDs = doc_IDs
        self.row_from = row_from
        self.row_to = row_to
        self.count = self.count_lines(input_path)

    def count_lines(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            for count, _ in enumerate(file):
                pass
            return count
        
    def process(self):
        deli = ''
        if self.type=='csv':
            deli = '\t'
        elif self.type=='dat':
            deli = '\x14'

        with open(self.input_path, 'r', encoding='utf-8', errors='ignore') as file:
            line_no = 0

            if self.row_to and self.row_from:
                self.row_from = int(self.row_from)
                self.row_to = int(self.row_to)
            elif self.row_from and not self.row_to:
                self.row_from = int(self.row_from)
                self.row_to = int(self.count)
            elif not self.row_from and self.row_to:
                self.row_from = 1
                self.row_to = int(self.row_to)

            for line in file:
                if line_no == 0:
                    line_no += 1
                    continue
                if self.row_from and line_no < self.row_from:
                    line_no += 1
                    continue
                if self.row_to and line_no > self.row_to:
                    break
                values_list = line.strip().split('\x14')
                if self.doc_IDs!='' and values_list[0] not in self.doc_IDs: #if there is docID provided, then skip docIDs not provided by user
                    continue
                if self.checked_headers: #if there is checked headers
                    new_values = [values_list[idx] for idx in self.header_idx]
                    values_list = new_values
                if deli=='\t':
                    unwrapped_values = [v.strip('þ') for v in values_list]
                    values_list = unwrapped_values
                self.output_dat.append(deli.join(values_list))
            
                line_no += 1
            if self.checked_headers:
                checked_headers = self.checked_headers
                if deli=='\t':
                    unwrap_headers = [h.strip('þ') for h in checked_headers]
                    checked_headers = unwrap_headers
                self.output_dat.insert(0, deli.join(checked_headers))
            else:
                headers = self.headers
                if deli=='\t':
                    unwrap_headers = [h.strip('þ') for h in headers]
                    headers = unwrap_headers
                self.output_dat.insert(0, deli.join(headers))

    def write_file(self):
        try:
            count = 0
            with open(self.output_path, 'w', encoding='utf-8', errors='ignore') as file:
                for line in self.output_dat:
                    file.write(line + '\n')
                    count += 1
            return count
        except Exception as e:
            print("Failed to write file:", e)
            return False