from demo.run_demo import _load_mock_output, _run_live


def test_mock_demo_fixture_loads_expected_report() -> None:
    output = _load_mock_output()

    assert output["subject"] == "booking"
    assert output["diagnosis"]["root_cause"] == "TOOL_MISUSE"
    assert output["fixes"]


def test_live_demo_runs_booking_pipeline() -> None:
    output = _run_live(subject="booking", store="memory", timeout_s=5.0)

    assert output["mode"] == "live"
    assert output["subject"] == "booking"
    assert output["diagnosis"]["root_cause"] == "TOOL_MISUSE"
    assert output["fixes"]
