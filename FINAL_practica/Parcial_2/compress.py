class Compress():
    def compress(self, text):
        compressed = []
        values = {}
        index = 1
        lista = text.split(' ')

        for char in lista:
            if char not in values:
                values[char] = index
                index += 1

        for x in lista:
            if x in values:
                y = values[x]
                compressed.append(y)

        return compressed, values

    def uncompress(self, compressed, values):
        uncompressed = []
        reverse_values = {v: k for k, v in values.items()}

        for x in compressed:
            if x in reverse_values:
                uncompressed.append(reverse_values[x])

        return ' '.join(uncompressed)

    def read_file(self, file_name):
        with open(file_name, 'r') as file:
            return file.read()


if __name__ == "__main__":
    compress = Compress()