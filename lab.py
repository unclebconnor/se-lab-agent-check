#Agent 6 required
from datadog_checks.checks import AgentCheck

import random, datetime, math

# content of the special variable __version__ will be shown in the Agent status page
__version__ = "1.0.0"


class Lab(AgentCheck):
	# Metric Functions
	GAUGE = AgentCheck.gauge
	COUNT = AgentCheck.count
	RATE = AgentCheck.rate
	MONOTONIC_COUNT = AgentCheck.monotonic_count

	# Metrics
	STEADY1 = {
		'lab.steady1.gauge': GAUGE,
		'lab.steady1.count': COUNT,
		'lab.steady1.rate': RATE,
		'lab.steady1.mc': MONOTONIC_COUNT
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

	INCREASE_HOURLY_CYCLE = {
		'lab.increase_hourly_cycle.gauge': GAUGE,
		'lab.increase_hourly_cycle.count': COUNT,
		'lab.increase_hourly_cycle.rate': RATE
	}

	INCREASE_DAILY_CYCLE = {
		'lab.increase_daily_cycle.gauge': GAUGE,
		'lab.increase_daily_cycle.count': COUNT,
		'lab.increase_daily_cycle.rate': RATE
	}

	INCREASE_WEEKLY_CYCLE = {
		'lab.increase_WEEKLY_cycle.gauge': GAUGE,
		'lab.increase_WEEKLY_cycle.count': COUNT,
		'lab.increase_WEEKLY_cycle.rate': RATE
	}

	SPARSE = {
		'lab.sparse.gauge': GAUGE,
		'lab.sparse.count': COUNT,
		'lab.sparse.rate': RATE
	}

	TRIG = {
		'lab.sine.gauge': GAUGE,
	}

	SPIKES = {
		'lab.spikes.gauge': GAUGE,
		'lab.spikes.count': COUNT,
		'lab.spikes.rate': RATE
	}

	def check(self, instance):
		# get configs
		tags = instance.get('tags',[])
		send_events = instance.get('send_events', False)

		# for the log
		counter = 0

		# some time helpers
		now = datetime.datetime.now()
		now_ts = datetime.datetime.now().strftime('%s')
		weekday = now.weekday() #0 - 6
		year = now.year
		month = now.month
		day = now.day
		hour = now.hour
		minute = now.minute
		second = now.second
		month_start = datetime.datetime(year,month,1)
		day_start = datetime.datetime(year,month,day)
		hour_start = datetime.datetime(year,month,day,hour)
		minute_start = datetime.datetime(year,month,day,hour)
		this_second = datetime.datetime(year,month,day,hour,second)

		seconds_this_month = (now - month_start).total_seconds()
		seconds_this_week = (now - day_start).total_seconds() + weekday * 86400
		seconds_this_day = (now - day_start).total_seconds()
		seconds_this_hour =  (now - hour_start).total_seconds()

		week_start = now - datetime.timedelta(seconds = seconds_this_week)


		# steady values of 1 g,c,r
		for metric_name, metric_func in self.STEADY1.iteritems():
			if "rate" in metric_name:
				metric_func(self, metric_name, second, tags=tags)
			elif "mc" in metric_name:
				metric_func(self, metric_name, second, tags=tags)
				self.log.info('Sent {} as a mc value'.format(second))
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
			rand_10 = random.random() * 10

			if "rate" in metric_name:
				val = (seconds_this_day + rand_10) * 20/3
				metric_func(self, metric_name, val, tags=tags)
			else:
				metric_func(self, metric_name, rand_10, tags=tags)

			counter += 1

		# random values between 0 - 1 for g,c,r
		# range will change with different min_collection_interval
		# rate will likely spike if you restart the agent and at the start of the month
		for metric_name, metric_func in self.RAND_FRACT.iteritems():
			rand_fract = random.random()

			if "rate" in metric_name:
				val = (seconds_this_day + rand_fract * 10) * 2/3
				metric_func(self, metric_name, val, tags=tags)
			else:
				metric_func(self, metric_name, rand_fract, tags=tags)

			counter += 1

		# generally increasing trends over an hour
		# shapes will vary
		for metric_name, metric_func in self.INCREASE_HOURLY_CYCLE.iteritems():
			number = round(minute/10) + 1

			if "rate" in metric_name:
				val = seconds_this_hour * (1 + (1/seconds_this_hour))
				metric_func(self, metric_name, val, tags=tags)
			else:
				metric_func(self, metric_name, number, tags=tags)

			counter += 1

		# generally increasing trends over a day
		# shapes will vary
		for metric_name, metric_func in self.INCREASE_DAILY_CYCLE.iteritems():
			number = round(hour*(1 + minute/60))

			if "rate" in metric_name:
				val = seconds_this_day * (1 + (1/seconds_this_day))
				metric_func(self, metric_name, val, tags=tags)
			else:
				metric_func(self, metric_name, number, tags=tags)

			counter += 1

		# generally increasing trends over a week
		# shapes will vary
		for metric_name, metric_func in self.INCREASE_WEEKLY_CYCLE.iteritems():
			number = round(day * (1 + hour/24))

			if "rate" in metric_name:
				seconds_this_week * (1 + (1/seconds_this_week))
				metric_func(self, metric_name, val, tags=tags)
			else:
				metric_func(self, metric_name, number, tags=tags)

			counter += 1

		# sparse metrics should show every half hour for about 5 min
		for metric_name, metric_func in self.SPARSE.iteritems():
			number = now.minute
			if number % 30 <= 5:
				metric_func(self, metric_name, number, tags=tags)
				counter += 1

		# just a sine function
		for metric_name, metric_func in self.TRIG.iteritems():
			val = 100 * math.sin(seconds_this_month / 100) + 100
			metric_func(self, metric_name, val, tags=tags)
			counter += 1

		# occasional spikes
		for metric_name, metric_func in self.SPIKES.iteritems():
			val = random.random() * 2

			if hour % 2 == 0 and minute % 7 == 0:
				val = hour * minute

			metric_func(self, metric_name, val, tags=tags)

			counter += 1

		## ======= SERVICE CHECKS ==========
		heartbeat_name = 'lab.is_up'
		heartbeat_status = 0
		self.service_check(heartbeat_name, heartbeat_status, tags=tags, message="Everything is OK")
		self.log.debug('Service Check {} has status {}'.format(heartbeat_name, heartbeat_status))

		sometimes_red_name = 'lab.crit_every_10'
		sometimes_red_status = 0
		if now.minute % 10 == 0:
			sometimes_red_status = 2
		self.service_check(sometimes_red_name, sometimes_red_status, tags=tags, message="Sometimes Red")
		self.log.debug('Service Check {} has status {}'.format(sometimes_red_name, sometimes_red_status))

		## ======= EVENT ==========
		if send_events:
			hostname = self.hostname
			event_title = instance.get('event_title', '')
			event_text = instance.get('event_text', '')
			event_alert_level = instance.get('event_alert_level', 'info')
			if event_alert_level not in ('error', 'warning', 'success', 'info'):
				event_alert_level = 'info'
			event_source_type_name = instance.get('event_source_type_name', 'lab')
			event_priority = instance.get('event_priority', 'normal')
			if event_priority not in ('normal', 'low'):
				event_priority = 'normal'
			ev = {
				'timestamp': now_ts,
				'event_type': 'lab',
				'host': hostname,
				'msg_title': event_title,
				'msg_text': event_text,
				'alert_type': event_alert_level,
				'source_type_name': event_source_type_name,
				'tags': tags,
				'priority': event_priority
			}
			self.event(ev)
			self.log.info('Sent event: {}'.format(ev))

		## to add
		## - other metric types
		## - some events
		## - Use min_collection_interval in multiple instances to "offset metrics"

     	## confirmation in agent log
  		self.log.info('Sent {} metrics to the agent'.format(counter))










  		## for the views <3