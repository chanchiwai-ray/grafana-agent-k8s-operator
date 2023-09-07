1. run `snapcraft` in dummy-snap to build the snap
2. run `charmcraft pack` in dummy-charm to build the charm
3. deploy charms, in charm-dummy
	- run `juju deploy ./charm-dummy_ubuntu-22.04-amd64.charm --resource dummy-snap="../snap-dummy/dummy-snap_0.1_amd64.snap"`
	- run `juju deploy grafana-agent --channel latest/edge`
4. relate charms
	- `juju relate grafana-agent charm-dummy`
5. when all are settle check, in the unit
	- `cat /etc/grafana-agent.yaml`
	- `cat /var/lib/snapd/mount/snap.grafana-agent.fstab`

You should see grafana-agent.yaml has duplicated log configs
