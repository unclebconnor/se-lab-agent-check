# se-lab-agent-check

## This will be useful for some tasks

This check will produce a variety of metrics that you can use to test the behaviors of metrics in monitors and dashboards. You can also make adjustments and break stuff to learn more about the different types of metrics.

## Setup

-   add this `lab.py` file to `checks.d/` and add a `lab.yaml` to `conf.d/`
-   Add 1 or more instances in the yaml file and specify tags (only option for now):

```
instances:
  - tags:
    - breakfast:eggs
    - lunch:coffee
    - dinner:chocolate
```

## Metrics

There are counts, rates, gauges for each of the following metrics

```
lab.steady1.<metric_type>
lab.steady0.<metric_type>
lab.rand10.<metric_type>
lab.randfract.<metric_type>
lab.increase_cycle.<metric_type>
lab.sparse.<metric_type>
```

...more coming soon
