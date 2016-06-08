class read:
	def __init__(self,id,seq,quality):
		try:
			self.id = id
			self.seq=seq
			self.qual = quality
			if quality and len(seq) != len(quality):
				raise Exception('unequal length of seqence and quality')
			self.len = len(seq)
		except Exception as err:
			print(err)	
	def getid(self):
		return self.id
	def getseq(self):
		return self.seq
	def getqual(self):
		return self.qual
	def __repr__(self):
		return '{0}\n{1}\n+\n{2}'.format(self.id, self.seq ,self.qual)	
	def __str__(self):
		return self.__repr__()
	def __len__(self):
		return self.len	


