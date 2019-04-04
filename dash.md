Use this to install a basic dash to visualize the metrics in this check

```
api_key=<>
app_key=<>

curl  -X POST -H "Content-type: application/json" \
-d '{
	"title": "Lab Metrics",
	"widgets": [{
		"definition": {
			"widgets": [{
				"definition": {
					"requests": [{
						"q": "avg:lab.steady0.gauge{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.steady0.gauge over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.steady0.count{*}.as_count()",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.steady0.count over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.steady0.rate{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.steady0.rate over *"
				}
			}],
			"layout_type": "ordered",
			"type": "group",
			"title": "Steady 0"
		}
	}, {
		"definition": {
			"widgets": [{
				"definition": {
					"requests": [{
						"q": "avg:lab.steady1.gauge{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.steady1.gauge over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.steady1.count{*}.as_count()",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "bars"
					}],
					"type": "timeseries",
					"title": "Avg of lab.steady1.count over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.steady1.rate{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.steady1.rate over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "sum:lab.steady1.mc{*}.as_count()",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Sum of lab.steady1.mc over *"
				}
			}],
			"layout_type": "ordered",
			"type": "group",
			"title": "Steady 1"
		}
	}, {
		"definition": {
			"widgets": [{
				"definition": {
					"requests": [{
						"q": "avg:lab.rand10.gauge{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.rand10.gauge over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.rand10.count{*}.as_count()",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "bars"
					}],
					"type": "timeseries",
					"title": "Avg of lab.rand10.count over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.rand10.rate{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.rand10.rate over *"
				}
			}],
			"layout_type": "ordered",
			"type": "group",
			"title": "Random 1 - 10"
		}
	}, {
		"definition": {
			"widgets": [{
				"definition": {
					"requests": [{
						"q": "avg:lab.randfract.gauge{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.randfract.gauge over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.randfract.count{*}.as_count()",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "bars"
					}],
					"type": "timeseries",
					"title": "Avg of lab.randfract.count over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.randfract.rate{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.randfract.rate over *"
				}
			}],
			"layout_type": "ordered",
			"type": "group",
			"title": "Random Fraction"
		}
	}, {
		"definition": {
			"widgets": [{
				"definition": {
					"requests": [{
						"q": "avg:lab.increase_hourly_cycle.gauge{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.increase_hourly_cycle.gauge over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.increase_hourly_cycle.count{*}.as_count()",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "bars"
					}],
					"type": "timeseries",
					"title": "Avg of lab.increase_hourly_cycle.count over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.increase_hourly_cycle.rate{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.increase_hourly_cycle.rate over *"
				}
			}],
			"layout_type": "ordered",
			"type": "group",
			"title": "Steady Increase Hourly Cycle"
		}
	}, {
		"definition": {
			"widgets": [{
				"definition": {
					"requests": [{
						"q": "avg:lab.increase_daily_cycle.gauge{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.increase_daily_cycle.gauge over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.increase_daily_cycle.count{*}.as_count()",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "bars"
					}],
					"type": "timeseries",
					"title": "Avg of lab.increase_daily_cycle.count over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.increase_daily_cycle.rate{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.increase_daily_cycle.rate over *"
				}
			}],
			"layout_type": "ordered",
			"type": "group",
			"title": "Steady Increase Daily Cycle"
		}
	}, {
		"definition": {
			"widgets": [{
				"definition": {
					"requests": [{
						"q": "avg:lab.increase_WEEKLY_cycle.gauge{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.increase_WEEKLY_cycle.gauge over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.increase_WEEKLY_cycle.count{*}.as_count()",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "bars"
					}],
					"type": "timeseries",
					"title": "Avg of lab.increase_WEEKLY_cycle.count over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.increase_WEEKLY_cycle.rate{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.increase_WEEKLY_cycle.rate over *"
				}
			}],
			"layout_type": "ordered",
			"type": "group",
			"title": "Steady Increase Weekly Cycle"
		}
	}, {
		"definition": {
			"widgets": [{
				"definition": {
					"requests": [{
						"q": "avg:lab.sparse.gauge{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.sparse.gauge over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.sparse.count{*}.as_count()",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "bars"
					}],
					"type": "timeseries",
					"title": "Avg of lab.sparse.count over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.sparse.rate{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.sparse.rate over *"
				}
			}],
			"layout_type": "ordered",
			"type": "group",
			"title": "Sparse"
		}
	}, {
		"definition": {
			"widgets": [{
				"definition": {
					"requests": [{
						"q": "avg:lab.spikes.gauge{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.spikes.gauge over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.spikes.count{*}.as_count()",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "bars"
					}],
					"type": "timeseries",
					"title": "Avg of lab.spikes.count over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.spikes.rate{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.spikes.rate over *"
				}
			}, {
				"definition": {
					"requests": [{
						"q": "avg:lab.sine.gauge{*}",
						"style": {
							"line_width": "normal",
							"palette": "dog_classic",
							"line_type": "solid"
						},
						"display_type": "line"
					}],
					"type": "timeseries",
					"title": "Avg of lab.sine.gauge over *"
				}
			}],
			"layout_type": "ordered",
			"type": "group",
			"title": "Other Metrics"
		}
	}, {
		"definition": {
			"widgets": [{
				"definition": {
					"group": "breakfast:eggs,dinner:chocolate,lunch:coffee,host:COMP10192.local",
					"title": "lab.is_up (local mac)",
					"tags": ["*"],
					"group_by": [],
					"type": "check_status",
					"check": "lab.is_up",
					"grouping": "check"
				}
			}, {
				"definition": {
					"group": "breakfast:eggs,dinner:chocolate,lunch:coffee,host:COMP10192.local",
					"title": "lab.crit_every_10 (local mac)",
					"tags": ["*"],
					"group_by": [],
					"type": "check_status",
					"check": "lab.crit_every_10",
					"grouping": "check"
				}
			}],
			"layout_type": "ordered",
			"type": "group",
			"title": "Checks"
		}
	}],
	"layout_type": "ordered"
}' \
"https://api.datadoghq.com/api/v1/dashboard?api_key=${api_key}&application_key=${app_key}"
```
