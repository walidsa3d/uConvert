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
				units=dic
				c=amount*units[src]/units[dest]
				return '%s %s=%s %s' %(amount,src,c,dest)
		return "Units must belong to the same category"
	def main(self):
		parser = argparse.ArgumentParser(description='Demo')
		parser.add_argument('amount',help='Amount to be converted' )
		parser.add_argument('src',help='Source Unit' )
		parser.add_argument('dest',help='Destination Unit' )
 		args = parser.parse_args()
 		print self.convert(args.src,args.dest,float(args.amount))
 
if __name__ == '__main__':
	uconvert().main()

