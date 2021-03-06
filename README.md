# se-lab-agent-check

## This will be useful for observing metric behaviors and reproducing some monitor issues

This check will produce a variety of metrics that you can use to test the behaviors of metrics in monitors and dashboards. You can also make adjustments and break stuff to learn more about the different types of metrics.

## Setup

-   add this `lab.py` file to `checks.d/` and add a `lab.yaml` to `conf.d/`
-   Add 1 or more instances in the yaml file and specify tags or event settings:

```
instances:
  - tags:
    - breakfast:eggs
    - lunch:coffee
    - dinner:chocolate

  - tags:
    - breakfast:cereal
    - lunch:salad
    - dinner:steak
    min_collection_interval: 30
```

## Metrics

There are counts, rates, gauges for each of the following metrics

```
lab.steady1.<metric_type>
lab.steady0.<metric_type>
lab.rand10.<metric_type>
lab.randfract.<metric_type>
lab.increase_hourly_cycle.<metric_type>
lab.increase_daily_cycle.<metric_type>
lab.increase_weekly_cycle.<metric_type>
lab.sparse.<metric_type>
lab.sine.gauge #gauge only
lab.spikes.<metric_type>
```

## Service Checks

`lab.is_up`

-   Will be OK status while check is running

`lab.crit_every_10`

-   Will be mostly OK while check is running
-   Will send CRITICAL if the current minute is a multiple of 10

## Events

You can add events with the following configs.  They will inherit the tags for their respective instance:

```
instances:
  - tags:
    - breakfast:cereal
    - lunch:salad
    - dinner:steak
    send_events: True # default False
    event:
      title: 'Title of Event'
      text: 'Body of Event'
      alert_level: 'info'
      source_type_name: 'lab'
      priority: 'normal'
```

