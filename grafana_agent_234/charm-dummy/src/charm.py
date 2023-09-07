#!/usr/bin/env python3
# Copyright 2023 dummy
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Charm the service.

Refer to the following tutorial that will help you
develop a new k8s charm using the Operator Framework:

https://juju.is/docs/sdk/create-a-minimal-kubernetes-charm
"""

import logging
import os

import ops
from charms.grafana_agent.v0.cos_agent import COSAgentProvider
from charms.operator_libs_linux.v2 import snap
from ops.model import ActiveStatus, BlockedStatus, MaintenanceStatus

# Log messages can be retrieved using juju debug-log
logger = logging.getLogger(__name__)


class CharmDummyCharm(ops.CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)

        self.cos_agent_provider = COSAgentProvider(
            self, log_slots=["dummy-snap:ovs-logs", "dummy-snap:ovn-logs"]
        )

        self.framework.observe(self.on.install, self._on_install)

    def _on_install(self, event):
        self.unit.status = MaintenanceStatus("Installing charm software.")
        snap_path = str(self.model.resources.fetch("dummy-snap"))
        if not os.path.getsize(snap_path) > 0:
            self.unit.status = BlockedStatus("Missing dummy-snap resource.")
        logger.info("Installing snap...")
        snap.install_local(snap_path, dangerous=True)
        self.unit.status = ActiveStatus()


if __name__ == "__main__":  # pragma: nocover
    ops.main(CharmDummyCharm)  # type: ignore
