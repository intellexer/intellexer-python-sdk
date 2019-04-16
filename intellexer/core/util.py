import io


class ChainStream(io.RawIOBase):
	# https://stackoverflow.com/a/50770511
	def __init__(self, *streams):
		self.leftover = b''
		self.stream_iter = iter(streams)
		try:
			self.stream = next(self.stream_iter)
		except StopIteration:
			self.stream = None

	def readable(self):
		return True

	def _read_next_chunk(self, max_length):
		# Return 0 or more bytes from the current stream, first returning all
		# leftover bytes. If the stream is closed returns b''
		if self.leftover:
			return self.leftover
		elif self.stream is not None:
			return self.stream.read(max_length).encode()
		else:
			return b''

	def readinto(self, b):
		buffer_length = len(b)
		chunk = self._read_next_chunk(buffer_length)
		while len(chunk) == 0:
			# move to next stream
			try:
				self.stream = next(self.stream_iter)
				chunk = self._read_next_chunk(buffer_length)
			except StopIteration:
				# No more streams to chain together
				self.stream = None
				return 0  # indicate EOF
		output, self.leftover = chunk[:buffer_length], chunk[buffer_length:]
		b[:len(output)] = output
		return len(output)
