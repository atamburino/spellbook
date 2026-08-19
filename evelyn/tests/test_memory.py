from brain.memory import Memory


def test_remember_and_get_fact(tmp_path):
    memory = Memory(tmp_path / "test.db")
    memory.remember_fact("wife's name", "Sam")
    assert memory.get_fact("wife's name") == "Sam"


def test_remember_fact_overwrites(tmp_path):
    memory = Memory(tmp_path / "test.db")
    memory.remember_fact("gym day", "Monday")
    memory.remember_fact("gym day", "Tuesday")
    assert memory.get_fact("gym day") == "Tuesday"
    assert len(memory.all_facts()) == 1


def test_get_fact_missing_returns_none(tmp_path):
    memory = Memory(tmp_path / "test.db")
    assert memory.get_fact("nope") is None


def test_recent_turns_in_order(tmp_path):
    memory = Memory(tmp_path / "test.db")
    memory.log_turn("user", "hello")
    memory.log_turn("evelyn", "hi there")
    turns = memory.recent_turns()
    assert [t.content for t in turns] == ["hello", "hi there"]


def test_recall_matches_keyword(tmp_path):
    memory = Memory(tmp_path / "test.db")
    memory.log_turn("user", "what's on my calendar for the gym")
    memory.log_turn("user", "text my wife I'm running late")
    results = memory.recall("gym")
    assert len(results) == 1
    assert "gym" in results[0].content


def test_recall_empty_query_falls_back_to_recent(tmp_path):
    memory = Memory(tmp_path / "test.db")
    memory.log_turn("user", "hello")
    results = memory.recall("")
    assert len(results) == 1
