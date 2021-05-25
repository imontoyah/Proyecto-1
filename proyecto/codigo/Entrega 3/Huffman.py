import heapq
import os


class HuffmanCoding:
	def __init__(self, path):
		""" It the constructor of the class HuffmanCoding which gets called when you make an instance of this class.

			:type path: csv file
		
			:rtype: None
		"""
		self.path = path
		self.heap = []
		self.codes = {}
		self.reverse_mapping = {}

	class HeapNode:
		def __init__(self, char, freq):
			""" It the constructor of the class HeapNode which gets called when you make an instance of this class.

				:rtype: None
				"""
			self.char = char
			self.freq = freq
			self.left = None
			self.right = None

		# defining comparators less_than and equals
		def __lt__(self, other):
			return self.freq < other.freq

		def __eq__(self, other):
			if(other == None):
				return False
			if(not isinstance(other)):
				return False
			return self.freq == other.freq

	# functions for compression:

	def make_frequency_dict(self, text):
			"""This function create a dicctionary where it store the frequencies of an specific character
			:type text: The csv file that contains the pixels of the image
			:param text:
		
			:raises: 
		
			:rtype: It returns the dictionary with the frequencies
			"""
			frequency = {}
			for character in text:
				if not character in frequency:
					frequency[character] = 0
				frequency[character] += 1
			return frequency

	def make_heap(self, frequency):
			""" This function builds a priority queue using a minHeap
			:type self: HeapNode

			:type frequency: dictionary of frequencies
			:param frequency: the node that we are going to store in the priority queue will be a dictionary of frequencies
		
			:raises: frequency does not content any information
		
			:rtype: priority queue
			"""
			for key in frequency:
				node = self.HeapNode(key, frequency[key])
				heapq.heappush(self.heap, node)

	def merge_nodes(self):
			""" Builds a Huffman Tree by selecting two min nodes and merging them
		
			:rtype: 
			"""
			while(len(self.heap)>1):
				node1 = heapq.heappop(self.heap)
				node2 = heapq.heappop(self.heap)

				merged = self.HeapNode(None, node1.freq + node2.freq)
				merged.left = node1
				merged.right = node2

				heapq.heappush(self.heap, merged)


	def make_codes_helper(self, root, current_code):
		""" It traverse the tree from the root to assign a code to the characters.

			:type root: HeapNode
			:param root: Is the root of the Huffman tree

			:type current_code: HeapNode
			:param current_code: It is the current node that tree is going to use
		
			:rtype: Huffman Tree traverse
		"""
		if (root == None):
				return

		if(root.char != None):
			self.codes[root.char] = current_code
			self.reverse_mapping[current_code] = root.char
			return

		self.make_codes_helper(root.left, current_code + "0")
		self.make_codes_helper(root.right, current_code + "1")


	def make_codes(self):
		""" It calls the make_codes_helper function to pass the parameters of root and current_code
		"""
		root = heapq.heappop(self.heap)
		current_code = ""
		self.make_codes_helper(root, current_code)


	def get_encoded_text(self, text):

		""" It encodes the given image
	
			:type text: string
			:param text: contains the file that is going to be encoded
		
			:rtype: string
		"""
		encoded_text = ""
		for character in text:
			encoded_text += self.codes[character]
		return encoded_text


	def pad_encoded_text(self, encoded_text):
		
		""" Description: The objective of this function is to fill the length of the final encoded bit streams
            adding some padding to the text. This is necessary in the case that the overall length of the final 
            econded text is not multiple of 8.

        :type encoded_text: String with the the codes of its character
        
        :rtype: String
        
        """
		extra_padding = 8 - len(encoded_text) % 8
		for i in range(extra_padding):
			encoded_text += "0"

		padded_info = "{0:08b}".format(extra_padding)
		encoded_text = padded_info + encoded_text
		return encoded_text


	def get_byte_array(self, padded_encoded_text):
		""" Description In this function the bits of the padded enconded yext are converted into bytes to reduce the 
        space. And finally, it return the array of bytes with the information for the compression process
        
        :rtype: byte array 
        """
		if(len(padded_encoded_text) % 8 != 0):
			print("Encoded text not padded properly")
			exit(0)

		b = bytearray()
		for i in range(0, len(padded_encoded_text), 8):
			byte = padded_encoded_text[i:i+8]
			b.append(int(byte, 2))
		return b


	def compress(self):
		""" Description This function calls the path that we created in the init, here we read the code and build a frequency dictionary of the characteres associated. 
			After that, it makes the priority queue using minHeap and it builds the huffman tree merging 2 min nodes.
			Followed by this, it traverse the tree from the root to assign a code to the characters. 
			Lastly, it encode the input text by replacing the characters with sequences of 0 and 1
	
			:type self: csv file

			:raises: file not found
		
			:rtype: binary file
		"""
		filename, file_extension = os.path.splitext(self.path)
		output_path = filename + ".bin"

		with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
			text = file.read()
			text = text.rstrip()

			frequency = self.make_frequency_dict(text)
			self.make_heap(frequency)
			self.merge_nodes()
			self.make_codes()

			encoded_text = self.get_encoded_text(text)
			padded_encoded_text = self.pad_encoded_text(encoded_text)

			b = self.get_byte_array(padded_encoded_text)
			output.write(bytes(b))

		print("Compressed")
		return output_path


	""" Functions to decompress: """


	def remove_padding(self, padded_encoded_text):
		""" Description: In the remove_padding function the idea is to eliminate the padding bits og the given string 
        to obtain the simply enconded text.
        :type encoded_text: bit string 
        :rtype: String
        """
		padded_info = padded_encoded_text[:8]
		extra_padding = int(padded_info, 2)

		padded_encoded_text = padded_encoded_text[8:] 
		encoded_text = padded_encoded_text[:-1*extra_padding]

		return encoded_text

	def decode_text(self, encoded_text):
		""" Description In de decode_text function you will read the bits and replace the valid Huffman Code
         bits with the character values in this case with the pixels values. 
        
        :type encoded_text: String 
        
        :rtype: String with the decoded text
        """
		current_code = ""
		decoded_text = ""

		for bit in encoded_text:
			current_code += bit
			if(current_code in self.reverse_mapping):
				character = self.reverse_mapping[current_code]
				decoded_text += character
				current_code = ""

		return decoded_text


	def decompress(self, input_path):
		""" Description: In this descomprees function you read the input path (the compress file) 
            and write the decompress file by removing the padd and decoding binary text (the codes). And also, 
            you save de decoded data in the aou file, getting the original data back 
        
        :type input_path: Binary file 
        
        :rtype: csv file
    	"""
		filename, file_extension = os.path.splitext(self.path)
		output_path = filename + "_decompressed" + ".txt"

		with open(input_path, 'rb') as file, open(output_path, 'w') as output:
			bit_string = ""

			byte = file.read(1)
			while(len(byte) > 0):
				byte = ord(byte)
				bits = bin(byte)[2:].rjust(8, '0')
				bit_string += bits
				byte = file.read(1)

			encoded_text = self.remove_padding(bit_string)

			decompressed_text = self.decode_text(encoded_text)
			
			output.write(decompressed_text)

		print("Decompressed")
		return output_path


#Code based on https://github.com/bhrigu123/huffman-coding
