#Agent 6 required
from datadog_checks.checks import AgentCheck

import random, datetime

# content of the special variable __version__ will be shown in the Agent status page
__version__ = "1.0.0"


class Lab(AgentCheck):
	# Metric Functions
	GAUGE = AgentCheck.gauge
	COUNT = AgentCheck.count
	RATE = AgentCheck.rate

	# Metrics
	STEADY1 = {
		'lab.steady1.gauge': GAUGE,
		'lab.steady1.count': COUNT,
		'lab.steady1.rate': RATE
	}

	STEADY0 = {
		'lab.steady0.gauge': GAUGE,
		'lab.steady0.count': COUNT,
		'lab.steady0.rate': RATE
	}

	RAND_10 = {
		'lab.rand10.gauge': GAUGE,
		'lab.rand10.count': COUNT,
		'lab.rand10.rate': RATE 
	}

	RAND_FRACT = {
		'lab.randfract.gauge': GAUGE,
		'lab.randfract.count': COUNT,
		'lab.randfract.rate': RATE 
	}

	INCREASE_CYCLE = {
		'lab.increase_cycle.gauge': GAUGE,
		'lab.increase_cycle.count': COUNT,
		'lab.increase_cycle.rate': RATE
	}

	SPARSE = {
		'lab.sparse.gauge': GAUGE,
		'lab.sparse.count': COUNT,
		'lab.sparse.rate': RATE
	}

		

	def check(self, instance):
		tags = instance.get('tags',[])
		counter = 0 # for the log

		# some helpers
		now = datetime.datetime.now()
		month_start = datetime.datetime(now.year,now.month,1)

		# steady values of 1 g,c,r
		for metric_name, metric_func in self.STEADY1.iteritems():
			if "rate" in metric_name:
				metric_func(self, metric_name, now.second, tags=tags)
				counter += 1
			else:
				metric_func(self, metric_name, 1, tags=tags)
				counter += 1

		# steady values of 0 g,c,r		
		for metric_name, metric_func in self.STEADY0.iteritems():
			metric_func(self, metric_name, 0, tags=tags)
			counter += 1

		# random values between 1 - 10 for g,c,r
		# range will change with different min_collection_interval
		# rate will likely spike if you restart the agent and at the start of the month	
		for metric_name, metric_func in self.RAND_10.iteritems():
			rand_10 = random.random()*10

			if "rate" in metric_name:
				val = ((now - month_start).total_seconds() + rand_10) * 20/3
				metric_func(self, metric_name, val, tags=tags)
				counter += 1
			else:
				metric_func(self, metric_name, rand_10, tags=tags)
				counter += 1

		# random values between 0 - 1 for g,c,r
		# range will change with different min_collection_interval
		# rate will likely spike if you restart the agent and at the start of the month		
		for metric_name, metric_func in self.RAND_FRACT.iteritems():
			rand_fract = random.random()

			if "rate" in metric_name:
				val = ((now - month_start).total_seconds() + rand_fract) * 2/3
				metric_func(self, metric_name, val, tags=tags)
				counter += 1
			else:
				metric_func(self, metric_name, rand_fract, tags=tags)
				counter += 1

		# generally increasing trends over time
		# shapes will vary
		for metric_name, metric_func in self.INCREASE_CYCLE.iteritems():
			number = round(now.minute/10)
			hour = now.hour if now.hour != 0 else 1
			minute = now.minute if now.minute != 0 else 1
			second = now.second if now.second != 0 else 1   

			if "rate" in metric_name:
				val = hour * minute * second
				metric_func(self, metric_name, val, tags=tags)
				counter += 1
			else:
				metric_func(self, metric_name, number, tags=tags)
				counter += 1


		# sparese metrics should show every half hour for about 5 min
		for metric_name, metric_func in self.SPARSE.iteritems():
			number = now.minute
			if number % 30 <= 5:
				metric_func(self, metric_name, number, tags=tags)
				counter += 1	

		## to add
		## - long term patterns for anomaly seasonality
		## - wave patterns - maybe use seconds to draw sin wav	
		## - random spikes
		## - variety of service checks
		## - some events
		## - Use min_collection_interval in multiple instances to "offset metrics"
		## - export a dash to show all of these
     	
  		self.log.info('Sent {} metrics to the agent'.format(counter)) 










  		## for the views <3  	