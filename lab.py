#Agent 6 required
from datadog_checks.checks import AgentCheck

from six import iteritems
import random, datetime

# content of the special variable __version__ will be shown in the Agent status page
__version__ = "1.0.0"


class Lab(AgentCheck):
	GAUGE = AgentCheck.gauge
	COUNT = AgentCheck.count
	RATE = AgentCheck.rate

	STEADY1 = {
		'steady_gauge_1': ('lab.steady1.gauge', GAUGE),
		'steady_count_1': ('lab.steady1.count', COUNT),
		'steady_rate_1': ('lab.steady1.rate', RATE)
	}

	STEADY0 = {
		'steady_gauge_0': ('lab.steady0.gauge', GAUGE),
		'steady_count_0': ('lab.steady0.count', COUNT),
		'steady_rate_0': ('lab.steady0.rate', RATE)
	}

	RAND_10 = {
		'rand_gauge_10': ('lab.rand10.gauge', GAUGE),
		'rand_count_10': ('lab.rand10.count', COUNT),
		'rand_rate_10': ('lab.rand10.rate', RATE) 
	}

	RAND_FRACT = {
		'rand_gauge_fract': ('lab.randfract.gauge', GAUGE),
		'rand_count_fract': ('lab.randfract.count', COUNT),
		'rand_rate_fract': ('lab.randfract.rate', RATE) 
	}

	INCREASE_CYCLE = {
		'increase_cycle_gauge': ('lab.increase_cycle.gauge', GAUGE),
		'increase_cycle_count': ('lab.increase_cycle.count', COUNT),
		'increase_cycle_rate': ('lab.increase_cycle.rate', RATE)
	}

	SPARSE = {
		'sparse_gauge': ('lab.sparse.gauge', GAUGE),
		'sparse_count': ('lab.sparse.count', COUNT),
		'sparse_rate': ('lab.sparse.rate', RATE)
	}

		

	def check(self, instance):
		tags = instance.get('tags',[])
		counter = 0 # for the log

		# some helpers
		now = datetime.datetime.now()
		month_start = datetime.datetime(now.year,now.month,1)

		# steady values of 1 g,c,r
		for key_name, (metric_name, metric_func) in iteritems(self.STEADY1):
			metric_func(self, metric_name, 1, tags=tags)
			counter += 1

		# steady values of 0 g,c,r	
		for key_name, (metric_name, metric_func) in iteritems(self.STEADY0):
			metric_func(self, metric_name, 0, tags=tags)
			counter += 1

		# random values between 1 - 10 for g,c,r
		# range will change with different min_collection_interval
		# rate will likely spike if you restart the agent and at the start of the month	
		for key_name, (metric_name, metric_func) in iteritems(self.RAND_10):
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
		for key_name, (metric_name, metric_func) in iteritems(self.RAND_FRACT):
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
		for key_name, (metric_name, metric_func) in iteritems(self.INCREASE_CYCLE):
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
		for key_name, (metric_name, metric_func) in iteritems(self.SPARSE):
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
     	
  		self.log.info('Sent {} metrics to the agent'.format(counter)) 










  		## for the views <3  	