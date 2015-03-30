from __future__ import division
import argparse

weight={'kg':1,'tonne':1000,'g':0.001,'pound':0.45}
length={'m':1,'km':1000,'dm':0.1,'cm':0.01,'mm':0.001,'inch':25.4,'foot':0.305,'yard':0.914
,'mile':1609}
time={'second':1,'minute':60,'hour':3600}
dics=[weight,length,time]

class uconvert:
	def convert(self,src,dest,amount):
		found=False
		for dic in dics:
			if src in dic and dest in dic:
				found=True
		if found:
			if src in weight:
				units=weight
			if src in length:
				units=length
			if src in time:
				units=time
			c=amount*units[src]/units[dest]
			print '%s %s=%s %s' %(amount,src,c,dest)
		else:
			print "error"
	def main(self):
		parser = argparse.ArgumentParser(description='Demo')
		parser.add_argument('amount',help='verbose flag' )
		parser.add_argument('src',help='verbose flag' )
		parser.add_argument('dest',help='verbose flag' )
 		args = parser.parse_args()
 		self.convert(args.src,args.dest,float(args.amount))
 
if __name__ == '__main__':
	uconvert().main()

