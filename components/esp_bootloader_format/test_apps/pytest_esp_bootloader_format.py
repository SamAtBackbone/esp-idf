# SPDX-FileCopyrightText: 2023 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0

import pytest
from pytest_embedded import Dut


@pytest.mark.esp32
<<<<<<<< HEAD:components/tcp_transport/test_apps/pytest_tcp_transport_ut.py
@pytest.mark.esp32c3
@pytest.mark.generic
def test_tcp_transport_client(dut: Dut) -> None:
========
@pytest.mark.generic
def test_esp_bootloader_format(dut: Dut) -> None:
>>>>>>>> a2d76ad38ad4be46bdc7ce2becab45fbe71ecc48:components/esp_bootloader_format/test_apps/pytest_esp_bootloader_format.py
    dut.expect_unity_test_output()
