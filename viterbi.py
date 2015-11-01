import numpy as np

class Viterbi(object):
	"""docstring for ClassName"""
	def __init__(self,pi,trans,emission):
		self.pi = pi
		self.trans=trans
		self.emission=emission
		self.num_of_states=pi.shape[0]
		#print self.num_of_states



	def decode(self,observations):
		self.num_of_observations=len(observations)
		#print self.num_of_observations

		trellis=np.zeros((self.num_of_states,self.num_of_observations))
		bckptr=np.zeros((self.num_of_states,self.num_of_observations), 'int32') * -1
		opt_state=[]
		
		#initialise
		trellis[:,0]= self.pi * self.emission[observations[0]-1]
		
		opt_state.append((trellis[:,0]).argmax(0))
		
		#trellis[:,1]= trellis[:,0] * self.emission[observations[1]-1]
		#print ((trellis[:,0]*np.reshape(self.emission[observations[1]-1] ,(self.num_of_states,1))).T *self.trans).T
		#print ((trellis[:,0]*np.reshape(self.emission[observations[1]-1] ,(self.num_of_states,1))).T *self.trans).T.argmax(1)
		print 'Levels:'
		for t in range(1,self.num_of_observations):
			trellis[:,t]=((trellis[:,t-1]*np.reshape(self.emission[observations[t]-1] ,(self.num_of_states,1))).T *self.trans).T.max(1)
			print trellis[:,t]
			bckptr[:,t]=((trellis[:,t-1]*np.reshape(self.emission[observations[t]-1] ,(self.num_of_states,1))).T *self.trans).T.argmax(1)
			#print bckptr[:,t]
			#opt_state.append((trellis[:,t]).argmax(0))
		tokens = [trellis[:, -1].argmax()]
		
		for i in range(self.num_of_observations-1, 0, -1):
			tokens.append(bckptr[tokens[-1], i])
		for i in tokens[::-1]:
			if i==1:
				print 'COLD'
			else:
				print 'HOT'
		




