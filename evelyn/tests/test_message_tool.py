from brain.tools import message_tool


def test_send_text_defaults_to_dry_run(monkeypatch):
    monkeypatch.delenv("EVELYN_ALLOW_SEND", raising=False)
    result = message_tool.handle("send_text", {"contact": "wife", "message": "on my way"})
    assert "DRY RUN" in result
    assert "on my way" in result


def test_send_text_raises_without_real_provider_when_allowed(monkeypatch):
    monkeypatch.setenv("EVELYN_ALLOW_SEND", "true")
    try:
        message_tool.handle("send_text", {"contact": "wife", "message": "hey"})
        assert False, "expected NotImplementedError"
    except NotImplementedError:
        pass
